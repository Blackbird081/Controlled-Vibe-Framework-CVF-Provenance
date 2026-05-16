Memory class: SUMMARY_RECORD

# CVF ADR Knowledge Vault Intake Runtime Ownership - 2026-05-16

Status: ACCEPTED.

## Purpose

Record the ownership decision for adopting markdown knowledge-vault intake into
CVF as executable Control Plane behavior.

## Scope

This ADR covers the first bounded Knowledge Vault Intake tranche inside:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

## Context

`tolaria` provides a local-first markdown vault doctrine: frontmatter
normalization, source-of-truth boundaries, provenance receipts, graph views,
context snapshots, drift signals, governed reinjection, and MCP knowledge tool
guards.

CVF should absorb this as governed Control Plane intake and context packaging,
not as a parallel vault runtime.

## Decision

Implement a CVF-owned `KnowledgeVaultIntakeContract`.

The contract owns:

- markdown frontmatter normalization;
- source input versus governed source-of-truth boundary;
- provenance receipt creation;
- knowledge graph view construction;
- governed context snapshot packaging;
- drift signal creation with `autoApplyAllowed: false`;
- governed reinjection proposal classification;
- MCP-style knowledge tool call gate.

## Alternatives

Alternative 1: copy the vault as a standalone knowledge system.

Rejected because CVF must remain the governance root.

Alternative 2: expose raw markdown files directly to agents.

Rejected because `tolaria` explicitly requires Context Builder packaging and
receipt-backed governance before agent use.

Alternative 3: keep this as docs-only.

Rejected because the operator requires selected high-fit absorption lanes to
become alive inside CVF.

## Consequences

Positive:

- external markdown assets now have an owner-native intake path;
- context snapshots can prove included and excluded assets;
- drift and reinjection remain proposal-only;
- MCP-like knowledge tools are gated before read/write.

Costs:

- YAML parsing remains intentionally bounded to simple frontmatter;
- no live file mutation or external MCP tool call is claimed.

## Verification

Verification must include:

- Control Plane package typecheck;
- focused vitest coverage for Knowledge Vault Intake;
- governed file-size check after GC-023 split;
- full pre-push chain before provenance push.

## Claim Boundary

This ADR claims deterministic local Control Plane behavior for knowledge-vault
intake and packaging only. It does not claim a live vault app, live MCP tool
execution, autonomous learning, or direct file mutation.
