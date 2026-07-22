# CVF External Agent Invocation Control Reference Front Door

Status: ACTIVE_REFERENCE_FRONT_DOOR

Memory class: POINTER_RECORD

docType: reference

Date: 2026-07-22

EPISTEMIC_PROCESS_NA_WITH_REASON: this is a pointer/front-door index of the
folder's stable references, not an evidence-comparison artifact; it makes no
expected-result, comparison, contradiction, or claim-update assertion of its
own.

## Purpose

This folder stores the stable knowledge-mapping surface for external-agent
CLI/MCP invocation control. It records what current CVF-governed sources
prove, what they do not prove, and which primary knowledge is missing before
any future control architecture may be designed. It is not a runtime control
surface, not a launcher, and not authority to invoke an external agent.

## Scope / Applies-To

Applies to CVF-EAIC-KR tranche T0 and any later reader who needs a
repository-local starting point before extending, contradicting, or
re-scoping the knowledge-readiness work. It supports the active global
execution moratorium recorded in
`docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md`.

Does not apply to runtime implementation, provider/API/account-subscription
use, MCP live invocation, agent CLI launch, public-sync, or a moratorium
lift. Those remain gated behind fresh operator authorization and later
tranches T1-T5 of
`docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`.

## Owner Surface

Target: stable navigation for the nine-domain knowledge gap and source
acquisition map produced by CVF-EAIC-KR-T0.

Owner boundary: this folder stores documentation-only knowledge mapping. The
invocation-control audit, the knowledge-readiness roadmap, the paired GC-018
baseline, and the provider-neutral provider/model assignment roadmap remain
the owning authority artifacts in their existing paths. This folder does not
duplicate, supersede, or extend their authority.

## Current References

| Reference | Use |
| --- | --- |
| `CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Nine-domain authority ledger, terminal gap classification, and bounded source-acquisition manifest for external-agent invocation control. |

## Related Surfaces

- `docs/audits/CVF_AGENT_CLI_MCP_INVOCATION_CONTROL_SYSTEM_CHAIN_REASSESSMENT_2026-07-20.md` - predecessor audit and active global execution moratorium.
- `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` - parent roadmap and tranche release rules.
- `docs/roadmaps/CVF_OPERATOR_APPROVED_PROVIDER_MODEL_ASSIGNMENT_AND_INVOCATION_RECEIPT_ROADMAP_2026-07-20.md` - subordinate provider/model assignment roadmap, parked by the same reassessment.
- `docs/baselines/CVF_GC018_EAIC_KR_T0_AUTHORITATIVE_KNOWLEDGE_SOURCE_MAP_2026-07-22.md` - paired dispatch baseline for this T0 tranche.
- `docs/reviews/CVF_EAIC_KR_T0_WORKER_RETURN_2026-07-22.md` - worker return evidence for this T0 tranche.

## Required Use

Before proposing any external-agent invocation-control architecture,
implementation, or live proof, read the knowledge gap and source acquisition
map in this folder together with the predecessor audit's Decision /
Recommendation. Do not treat a `PARTIAL` or `OWNED` domain row as sufficient
to lift the global execution moratorium; only a fresh explicit operator
decision after sufficient primary-source intake can do that.

Provider-native internal reasoning, exploration, task decomposition, context
management, and internal subagents inside one authorized parent session are
not external invocation surfaces. CVF governs the parent scope, separately
dispatched sessions, external boundaries, aggregate envelope, mutations, and
outcome evidence without approving each internal step.

If the knowledge map still contains a critical missing or opaque domain, keep
the roadmap parked. Do not force architecture or implementation merely to
advance a tranche. A later operator-approved intake may absorb bounded external
knowledge through the canonical external-knowledge chain.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON: this front door indexes CVF-governed evidence and a bounded acquisition manifest; it ingests no new external source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this folder and the paired T0 knowledge gap map |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | later primary-source intake requires a fresh operator-approved T1 tranche; until then the lane remains parked for insufficient knowledge |

## Claim Boundary

This front door claims only that the listed file is the current stable
knowledge-mapping surface in this folder. It does not verify runtime
effectiveness, external-agent control, provider behavior, implementation
readiness, public readiness, or a lift of the global execution moratorium.
