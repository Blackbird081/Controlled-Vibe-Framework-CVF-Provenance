# CVF Dual Agent Surface Accounting Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

Date: 2026-06-23

docType: reference

## Purpose

Require every new or materially changed CVF foundation, workflow, capability,
skill, memory surface, governance control, and agent-facing artifact to account
for both internal agents and external agents through CLI/MCP boundaries.

## Scope / Applies To

Applies to new or materially changed CVF roadmaps, baselines, work orders,
reference contracts, architecture packets, implementations, completion
reviews, public claims, and skill packages that serve or could serve agents.

It does not force CLI/MCP implementation where no external use is justified;
it forces an explicit, evidence-backed disposition.

## Core Rule

Authors must evaluate both consumer classes:

1. `INTERNAL_AGENT` - agents operating inside CVF-governed workspace,
   orchestration, runtime, or control-plane surfaces.
2. `EXTERNAL_AGENT_CLI_MCP` - external agents consuming CVF through governed
   CLI, MCP, adapter-contract, proposal, receipt, or readout boundaries.

Accounting does not automatically authorize implementation. Each consumer row
must use exactly one disposition:

- `IMPLEMENTED`
- `CONTRACT_ONLY`
- `DEFERRED_WITH_REASON`
- `N/A_WITH_REASON`

Silence is not a valid disposition.

## Mandatory Dual Agent Surface Matrix

Applicable roadmaps, baselines, work orders, reference contracts, completion
reviews, and architecture packets must include:

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Disposition |
|---|---|---|---|---|
| `INTERNAL_AGENT` | exact internal owner, path, or proposed doc-only contract | permissions, commit/action authority, and claim boundary | source/test/review evidence or reason | allowed disposition |
| `EXTERNAL_AGENT_CLI_MCP` | exact CLI/MCP/adapter owner, proposed contract, or deferred owner | ingress, authentication, approval, receipt, raw-data, mutation, and public boundary | source/live/contract evidence or reason | allowed disposition |

The matrix must distinguish interface existence from runtime behavior and must
not promote a proposed CLI/MCP field into a current source fact.

## Lifecycle Placement

- Roadmap: decide applicability and likely owner for both consumers.
- GC-018/work order: source-verify existing owners and declare exact allowed
  implementation scope for each consumer.
- Implementation: change only the rows explicitly authorized.
- Review/closure: verify implemented rows and preserve bounded dispositions for
  deferred rows.
- Public export: treat public CLI/MCP claims separately from private provenance
  closure.

## Fail Conditions

Return to the orchestrator or block closure when an applicable artifact:

- designs only for internal agents and omits external CLI/MCP disposition;
- claims external-agent support from an internal helper or document alone;
- treats `CONTRACT_ONLY` as runtime availability;
- implements CLI/MCP behavior from a roadmap-only or adapter-contract-only
  decision;
- omits authentication, approval, receipt, raw-data, mutation, or claim
  boundary where the external surface can act;
- uses provider-local memory as authority for either consumer class.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Work orders must source-verify named CLI/MCP tools and fields | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | source-verification requirements | `CLI/MCP tool name` | work-order template | VALUE_SET | ACCEPT |
| Workspace architecture distinguishes CVF Web and local agent runtime/CLI/MCP surfaces | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | two-layer model; Layer Responsibility Matrix | `CVF_WEB_WORKSPACE`; `CVF_LOCAL_WORKSPACE_RUNTIME` | workspace architecture | VALUE_SET | ACCEPT |
| External MCP/workspace proposals require CVF authority before implementation | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | absorption decisions; claim boundary | `ADAPT`; `DEFER` | external package absorption map | VALUE_SET | ACCEPT |
| Memory summary contract distinguishes adapter contract from runtime behavior | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | claim boundary and adapter contract | `adapterContractOnly` | external-agent memory contract | LITERAL_INVARIANT | ACCEPT |
| Current continuity model excludes external-agent memory from canonical authority | `docs/reference/CVF_CONTEXT_CONTINUITY_MODEL.md` | source hierarchy | `external agent memory files` | context continuity model | LITERAL_INVARIANT | ACCEPT |

## Finding-To-Governance Learning Disposition

- Defect class: `RULE_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `STANDARD_ADDED`
- Next control action: add a deterministic checker candidate after sufficient
  forward use proves stable applicability rules.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this standard changes
  design accounting only.

## Epistemic Process Block

### Expected Result / Prediction

Mandatory dual-surface accounting should expose internal-only architecture
assumptions before implementation without forcing premature CLI/MCP scope.

### Evidence Comparison

Existing workspace and memory contracts already distinguish internal owners
from external CLI/MCP or adapter-contract surfaces, but no general rule makes
that comparison mandatory across all new CVF foundations.

### Contradiction Or Gap Disposition

External accounting can be `DEFERRED_WITH_REASON` or `N/A_WITH_REASON`; this
resolves the apparent conflict between architecture completeness and bounded
implementation authorization.

### Claim Update

The accepted claim is mandatory accounting for both consumers, not universal
external-agent implementation or runtime support.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance architecture rule. A later public-safe
summary requires an authorized public-sync batch from the sibling clone.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | architecture accounting for internal and external agent consumers |
| claimDisposition | N/A with reason: no Delta execution behavior is implemented |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: documentation standard only |
| invocationBoundary | roadmap, dispatch, implementation, and closure authoring checks |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | mandatory accounting, not mandatory simultaneous implementation |
| forbiddenExpansion | no automatic CLI/MCP runtime, provider/live, public-sync, or external-agent readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex standard author |
| Provider or surface | local workspace |
| Session or invocation | dual-agent surface rule authoring, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governance gates, git commit |
| Target paths | this standard and System Skills roadmap |
| Allowed scope source | operator instruction to record a mandatory internal/external-agent rule and roadmap |
| Before status evidence | clean HEAD `7c0480bc` after Claude ADIF-T0 checkpoint |
| After status evidence | two documentation-only architecture artifacts |
| Diff evidence | real-range name-status and governance gate output |
| Approval boundary | architecture documentation only |
| Claim boundary | no ADIF edit, runtime, CLI/MCP implementation, provider/live, or public-sync |
| Agent type | standard/roadmap author |
| Invocation ID | `cvf-dual-agent-surface-system-skills-roadmap-2026-06-23` |
| Expected manifest | this standard; System Skills roadmap |
| Actual changed set | this standard; System Skills roadmap |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This standard requires explicit dual-consumer accounting. It does not require
both consumers to be implemented in the same tranche and does not authorize an
external CLI/MCP surface without its own source-verified work order.
