# CVF GC-018 Baseline - EAIC-KR T1 Primary Source Intake

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-22

Batch ID: CVF-EAIC-KR-T1

dispatchBaseHead: `6ce93ecd2`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: worker role selected by operator through manual copy/paste

## Purpose

Authorize one bounded, read-only primary-source intake for the four CRITICAL
external-agent invocation-control knowledge gaps: launch admission, process
identity, cumulative budget, and unknown usage. The worker produces a
reconciled evidence ledger without invoking an agent, provider, API, CLI, MCP
tool, or executable process under study.

## Scope / Target / Owner Boundary

Risk ceiling: R0 documentation and public-source evidence only.

Allowed scope:

- read current CVF authority named by this packet;
- retrieve public documentation from the allowlisted official source roots;
- use public web search only to locate an exact page within those roots;
- paraphrase relevant source semantics and capture stable citation metadata;
- create exactly the two worker-owned outputs named by the work order;
- run repository-local read-only checks and governance gates.

Forbidden scope:

- agent CLI/MCP invocation, separate agent dispatch, provider/model execution,
  API request, account login, API key, service token, or quota consumption;
- process launch, termination experiment, live proof, browser automation,
  source-repository clone, package install, or executable download;
- runtime, source, test, checker, hook, standard, roadmap, registry, session,
  handoff, public-sync, deployment, or production mutation;
- treating one provider or host as the required CVF implementation target;
- copying long passages or storing private/account-only content;
- staging, committing, pushing, merging, publishing, deleting, or renaming.

## Operator-Approved Source Classes And Roots

The worker may use only public pages under these official roots. Redirects
must terminate inside the same organization-owned root family.

| Source class | Approved root | Intended evidence | Provider-neutral boundary |
| --- | --- | --- | --- |
| current agent-host documentation | `https://docs.anthropic.com/`; `https://support.anthropic.com/` | Claude Code process/session surface and subscription visibility | representative current host only; no default-provider decision |
| current agent-host documentation | `https://developers.openai.com/codex/`; `https://help.openai.com/` | Codex CLI process/session surface and subscription visibility | representative current host only; no default-provider decision |
| protocol specification | `https://modelcontextprotocol.io/specification/` | MCP lifecycle, progress, cancellation, and identity semantics | protocol evidence, not runtime-control proof |
| operating-system process control | `https://learn.microsoft.com/windows/win32/procthread/job-objects` | Windows process-tree ownership and termination primitives | OS primitive only; no agent-host conformance inference |
| runtime process control | `https://nodejs.org/docs/latest/api/child_process.html` | Node child-process identifiers, signals, and cancellation surface | runtime primitive only; no descendant-tree guarantee by itself |
| portable process semantics | `https://pubs.opengroup.org/onlinepubs/` | POSIX process groups, sessions, and signals | portability comparison only; Windows remains separately classified |

Third-party blogs, search-result summaries, social posts, generated answers,
provider-local memory, and chat history may help locate a page but must not
appear as accepted evidence.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T0 accepted | `docs/reviews/CVF_EAIC_KR_T0_COMPLETION_2026-07-22.md`; material correction commit `77d75ef93` | accepted knowledge map identifies exact CRITICAL gaps | SATISFIED |
| operator source approval | operator response `dong y` on 2026-07-22 to the proposed bounded T1 official-source intake | approval must precede network retrieval | SATISFIED |
| invocation moratorium | parent roadmap and T0 completion keep external invocation parked | T1 must remain research-only | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source-intake`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class source-intake --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Dependency Release Evidence; Source Verification Block; External Knowledge Intake Routing; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm dispatch shape after checker-source read-ahead and scaffold generation |
| claimBoundary | checker compliance proves packet structure only, not external-source correctness or knowledge sufficiency |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id EAIC-KR-T1 --title "External Agent Invocation Control Primary Source Intake" --date 2026-07-22 --base 6ce93ecd2 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "EAIC-KR T0 accepted and operator approved bounded T1 intake" --stdout` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact authority, source roots, scope, evidence, output, and stop rules |
| checkerReadAheadConfirmation | applicable checker constants and regex-sensitive fields were inspected before this file was written |
| docOnlyNewFields | sourceAuthorityClass; accessModeClass; domainReadinessDisposition; sourceVolatility |
| claimBoundary | dispatch authoring provenance only; no runtime or provider behavior claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1 objective is primary-source reconciliation | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Work Plan T1 row | `T1` | EAIC-KR roadmap | ACCEPT |
| T1 requires T0 acceptance and operator source approval | VALUE_SET | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules | `T1` | EAIC-KR roadmap | ACCEPT |
| four domains are CRITICAL | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Knowledge Gap And Source Acquisition Map rows 1, 2, 5, and 6 | `Acquisition priority` | T0 knowledge map | ACCEPT |
| current knowledge remains insufficient for architecture | VALUE_SET | `docs/reviews/CVF_EAIC_KR_T0_COMPLETION_2026-07-22.md` | Risk / Corrective Action | `PARKED_KNOWLEDGE_GAP` | T0 completion review | ACCEPT |
| external knowledge remains advisory until reconciled | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core | `Central Core` | external knowledge chain map | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| planned path collision | `Test-Path` returned false for baseline, work order, ledger, worker return, and completion review before authoring | ACCEPT |
| batch-token collision | `rg -n "EAIC.KR.T1.PRIMARY.SOURCE.INTAKE|EAIC-KR-T1" docs CVF_SESSION` returned no prior T1 artifact | ACCEPT |
| source-field collision | planned doc-only fields are declared in this baseline and must not be represented as current runtime fields | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | approved official public sources -> per-source authority ledger -> overlap and novelty comparison -> per-domain readiness decision -> reviewer acceptance or continued park |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_source_intake_decision_packet_preflight.py` |
| Owner surface | `docs/reference/external_agent_invocation_control/` family |
| Disposition | ADAPT external primary knowledge into a CVF-owned evidence ledger; do not import implementation |
| Claim boundary | source intake only; no source becomes CVF runtime authority without later ratification and implementation proof |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: official sources will clarify process and protocol
primitives but may leave subscription-session usage opaque and may not provide
an end-to-end cumulative budget owner.

Evidence Comparison Requirement: compare each accepted source against the T0
gap question and record confirmed, narrowed, contradicted, or unresolved.

Contradiction Handling Requirement: conflicting provider, protocol, OS, and
runtime semantics remain separate; do not normalize them by inference.

Claim Update Requirement: return one domain-level terminal disposition and one
overall T1 recommendation without releasing T2 automatically.

## Baseline Decision

`DISPATCH_READY`

The T0 dependency and source-class checkpoint are satisfied. This decision
releases only manual dispatch of the paired no-commit T1 research worker.

## Verification / Evidence

- dispatch base: clean worktree at `6ce93ecd2`;
- planned-path `Test-Path`: all five planned material and closure paths absent
  before authoring;
- exact batch-token search: no prior EAIC-KR-T1 artifact;
- pre-dispatch autorun must pass before the packet is handed to the worker.

## Claim Boundary

This baseline authorizes a bounded public-source intake and two uncommitted
documentation outputs. It does not authorize agent invocation, provider use,
account access, implementation, architecture ratification, live proof,
public-sync, or a lift of the invocation moratorium.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private knowledge-readiness intake with no public implementation or
release evidence.
