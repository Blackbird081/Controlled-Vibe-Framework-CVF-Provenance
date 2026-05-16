<!-- Memory class: SUMMARY_RECORD -->

# CVF GC-018 MCP Business Adapter Authorization - 2026-05-16

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION.

## Purpose

Authorize a bounded runtime tranche that absorbs the generic MCP business-tool
adapter pattern from `pancake-pos-mcp` into CVF without adopting Pancake POS as
a core runtime dependency.

## Scope

Target owner surface:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`

Source:

- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/`

The tranche may implement deterministic local contracts for business MCP tool
registration, risk classification, approval gating, transport policy,
execution receipt, and governed adapter result.

## Source

Predecessor evidence:

- `docs/baselines/CVF_16_5_LIVING_INTEGRATION_CLASSIFICATION_SUMMARY_2026-05-16.md`
- `.private_reference/legacy/CVF 16.5/pancake-pos-mcp/Thong_tin.md`

## Decision

Approved direction: CVF-owned generic MCP Business Adapter contract.

Pancake POS remains a deferred domain profile. CVF adopts the adapter pattern,
not the Pancake runtime or domain-specific tool catalog.

## Non-Goals

- no Pancake POS runtime dependency;
- no external MCP server call;
- no API key, shop id, bearer token, or endpoint config;
- no domain-specific Pancake tool hard-code;
- no live business mutation claim;
- no replacement for CVF Guard Contract.

## Evidence

Required evidence before closure:

- source adoption matrix;
- ADR;
- roadmap;
- deterministic tests for registry, classifier, approval, transport, receipt,
  and adapter behavior;
- package typecheck;
- closure note with claim boundary.

## Approval Gate

The operator authorized autonomous continuation of the knowledge absorption
roadmap on 2026-05-16. This file records that authorization for the MCP Business
Adapter tranche.
