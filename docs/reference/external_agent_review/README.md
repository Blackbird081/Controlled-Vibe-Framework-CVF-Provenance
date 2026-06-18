# CVF External Agent Review Reference Front Door

Memory class: POINTER_RECORD

Status: ACTIVE_INDEX

docType: reference

## Purpose

Provide the stable front door for preparing external-agent review context.
External agents may review public CVF surfaces, copied handoff packages, or
operator-provided examples, but CVF remains the source of truth.

This folder exists so external agents do not mistake simplified public product
vocabulary for the internal governed workflow-chain system.

## Scope / Target / Owner Boundary

Target: external-agent review packets, public-context summaries, and
non-canonical package absorption.

Owner boundary: this folder owns context-shaping guidance only. It does not
authorize public-sync, publication, external repository mutation, runtime
execution, provider calls, or production/readiness claims.

## Central Rule

CVF is the origin. External repositories and external-agent packages are
reference material only.

Useful patterns may be absorbed only after they are mapped to CVF-owned
contracts, source authority, claim boundaries, and current workflow-chain
semantics.

## Current References

| Reference | Role |
|---|---|
| `CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md` | Standard for giving external agents enough context to review CVF without exposing private provenance source. |
| `CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md` | Canonical distinction between public/simple workflow vocabulary and internal governed workflow-chain system. |
| `CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md` | Stable packet template for external-agent review requests. |
| `CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md` | Authoring checklist and red-flag screen before sending a packet to an external agent. |
| `CVF_EXTERNAL_AGENT_REVIEW_SAMPLE_PACKET_WORKFLOW_MCP_WORKSPACE.md` | Bounded sample packet for workflow-chain, MCP, and workspace review context. |
| `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Stable workflow for classifying returned external-agent output before CVF acts on it. |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | CVF-owned absorption map for the local external workspace package copied into the repo root. |
| `docs/reference/mcp_gateway/README.md` | MCP Gateway local view for future MCP tool ingress work. |
| `docs/reference/agent_workspace/README.md` | Agent workspace local view for future workspace state/runtime work. |

## Authoring Flow

1. Read this front door and the context standard.
2. Start from `CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`.
3. Run the checks in `CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`.
4. Use `CVF_EXTERNAL_AGENT_REVIEW_SAMPLE_PACKET_WORKFLOW_MCP_WORKSPACE.md` as
   the bounded example for workflow-chain, MCP, and workspace review context.
5. After the external agent returns output, classify every returned item through
   `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` before creating a
   finding, standard, roadmap, work order, review, reference artifact, or
   operator decision.

## Required Read Trigger

Read this folder when a task:

- asks an external agent to evaluate CVF architecture, workflow chains, MCP, or
  workspace design;
- prepares public or semi-public context for external review;
- absorbs a copied external package, repo idea, or review packet;
- notices an external agent treating a public/simple lifecycle as internal CVF
  workflow-chain authority;
- needs to decide what can be public context without publishing private
  provenance files.

## Claim Boundary

This front door is a reference index. It does not make private provenance files
public, and it does not authorize public-sync or external-facing readiness.
