# CVF GC-018 - EARC-T1 External Agent Review Packet Template

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize a bounded reference/template tranche that turns the EARC roadmap into
reusable external-agent review packet material.

## Scope

In scope:

- create a stable external-agent review packet template;
- create a stable authoring checklist for review packets;
- create one bounded sample packet for workflow-chain, MCP, and workspace
  review context;
- update the external-agent review folder index;
- update the EARC roadmap tranche state and GC-051 corpus registry entry.

Out of scope:

- public-sync;
- publishing or copying private provenance files to the public repository;
- MCP implementation;
- workspace runtime state mutation;
- provider or live API calls;
- raw external package import;
- public, production, release, or external-facing readiness claims.

## Source Verification

| Claimed item | Source file | Verified section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EARC-T1 target requires a reusable packet template, authoring checklist, and bounded sample packet. | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | `## T1 Target Shape` | `CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md`; `CVF_EXTERNAL_AGENT_REVIEW_AUTHORING_CHECKLIST.md`; bounded sample packet | EARC roadmap | ACCEPT |
| External-agent review requests require bounded context packets with source-of-truth, public/private boundary, workflow-chain map, authority surfaces, non-authority surfaces, output shape, and claim boundary. | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md` | `## Required External Review Context` | required context packet fields | external-agent review context standard | ACCEPT |
| Public/simple workflow vocabulary is display or education vocabulary unless mapped to governed CVF workflow-chain semantics. | `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md` | `## Public / Simple Vocabulary`; `## Internal Governed Workflow-Chain Surfaces` | public/simple vocabulary boundary | workflow-chain public review context | ACCEPT |
| Stable foundation files belong in indexed `docs/reference/<family>/` folders, while execution artifacts are dated. | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | `## Artifact Classes`; `## Date Policy` | stable foundation folder rule | foundation storage standard | ACCEPT |
| External review context work does not authorize public-sync, publication, runtime execution, provider calls, or readiness claims. | `docs/reference/external_agent_review/README.md` | `## Scope / Target / Owner Boundary`; `## Claim Boundary` | external-agent review folder owner boundary | external-agent review front door | ACCEPT |

## Decision

Proceed with a stable reference/template tranche. EARC-T1 may create durable
foundation files under `docs/reference/external_agent_review/` and dated
execution evidence under the baselines, work orders, and reviews folders.

## Evidence / Verification

| Evidence | Expected result |
|---|---|
| `python governance/compat/generate_corpus_scan_registry.py --generate` | Registry aggregate updates from source entries |
| `python governance/compat/generate_corpus_scan_registry.py --check` | Registry aggregate matches sources |
| `git diff --check` | Diff hygiene passes |
| `python governance/compat/run_worker_return_fast_gate.py` | Reviewer-fast checks pass |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 6bab8960 --head HEAD --enforce` | Material commit shape is bounded |
| Pre-commit hook | Required local governance checks pass |

## Claim Boundary

This GC-018 authorizes reference/template work only. It does not authorize
public-sync, MCP implementation, provider/live calls, workspace runtime
mutation, raw external package import, or readiness claims.

## Work Order

The authorized work order is:

`docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T1_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE_FOR_CODEX_2026-06-18.md`
