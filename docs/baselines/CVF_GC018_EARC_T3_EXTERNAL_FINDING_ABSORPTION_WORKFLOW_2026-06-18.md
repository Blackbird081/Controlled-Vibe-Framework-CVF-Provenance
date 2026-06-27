# CVF GC-018 - EARC-T3 External Finding Absorption Workflow

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize a bounded foundation tranche that defines how CVF absorbs returned
external-agent output after an external review packet is used.

## Scope

In scope:

- create a stable external-agent finding absorption workflow under
  `docs/reference/external_agent_review/`;
- update the external-agent review front door, packet template, and authoring
  checklist so future agents route returned output through the workflow;
- update the EARC roadmap tranche state;
- update GC-051 corpus registry coverage;
- author a completion review.

Out of scope:

- public-sync or public repository edits;
- publishing private provenance files;
- implementing MCP tools or workspace runtime behavior;
- provider or live API calls;
- raw external package import;
- runtime, public, production, release, MCP, provider, or external-facing
  readiness claims;
- adding a machine checker in this tranche.

## Source Verification

| Claimed item | Source file | Verified section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EARC-T3 target defines how external-agent output is classified after review. | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | `## T3 Target Shape` | external output to CVF disposition matrix | EARC roadmap | ACCEPT |
| External review output is advisory until CVF absorbs it through governed artifacts. | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_PACKET_TEMPLATE.md` | `## Absorption Instruction` | external output is advisory | external-agent review packet template | ACCEPT |
| External agents must distinguish public/simple vocabulary, governed source, private provenance, external comparison, and inference. | `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md` | `## External-Agent Instruction` | source classification instruction | workflow-chain public review context | ACCEPT |
| Reusable findings must be promoted into a CVF-governed artifact, not left in provider memory. | `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md` | `## Protocol`; `## Provider-memory learning boundary` | governed finding promotion | finding-to-governance standard | ACCEPT |
| Durable foundation files belong in indexed stable reference folders. | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | `## Rule`; `## Date Policy` | stable foundation folder rule | foundation storage standard | ACCEPT |

## Decision

Proceed with EARC-T3 as a reference/workflow tranche. The workflow is a CVF
control-plane local view for classifying returned external output, not a runtime
implementation or public publication.

## Evidence / Verification

| Evidence | Expected result |
|---|---|
| `python governance/compat/generate_corpus_scan_registry.py --generate` | Registry aggregate updates from source entries |
| `python governance/compat/generate_corpus_scan_registry.py --check` | Registry aggregate matches sources |
| `git diff --check` | Diff hygiene passes |
| `python governance/compat/run_worker_return_fast_gate.py` | Reviewer-fast checks pass |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 3f0cebf1 --head HEAD --enforce` | Material commit shape is bounded |
| Pre-commit hook | Required local governance checks pass |

## Claim Boundary

This GC-018 authorizes reference/workflow work only. It does not authorize
public-sync, MCP implementation, provider/live calls, workspace runtime
mutation, raw external package import, machine-check implementation, or
readiness claims.

## Work Order

The authorized work order is:

`docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3_EXTERNAL_FINDING_ABSORPTION_WORKFLOW_FOR_CODEX_2026-06-18.md`
