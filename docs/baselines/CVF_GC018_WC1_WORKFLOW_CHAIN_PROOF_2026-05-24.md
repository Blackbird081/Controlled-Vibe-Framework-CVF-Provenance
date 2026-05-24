# GC-018: WC-1 Workflow Chain Proof

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Purpose

Authorize a bounded WC-1 implementation to prove the existing CVF workflow
chain end to end with live evidence: governed execution writes summary-only
durable memory, then a second governed execution reads that prior context.

## Scope / Target / Owner Boundary

Scope: proof artifact only; no new production runtime surface.

Target:

- `scripts/run_cvf_wc1_workflow_chain_probe.mjs`
- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-1 completion evidence under `docs/reviews/`

Owner: Codex implementer with product, QA, governance, and release review roles.

Out of scope: route/provider behavior changes, new receipt-envelope fields,
new memory tiers, autonomous memory write, `canReinject=true`, raw memory prompt
injection, hosted/cloud persistence, production readiness, or freeze release.

## Depth Audit

Depth score: 9/10.

Rationale:

- Operator explicitly authorized opening implementation after the WC roadmap.
- WC-2 is closed; WC-1 is the next sequenced tranche before WC-3.
- Existing M1/R2/S1 surfaces prove read and write separately, but not the
  two-turn chain in one live workflow.
- The only new source artifact should be a probe script, not runtime behavior.

## Source / Predecessor Evidence

- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-2 closure:
  `docs/reviews/CVF_WC2_MOCK_FALLBACK_ELIMINATION_COMPLETION_2026-05-24.md`
- R2 durable memory read closure:
  `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
- S1 durable memory write closure:
  `docs/reviews/CVF_S1_DURABLE_MEMORY_WRITE_ROUTE_COMPLETION_2026-05-24.md`

## Authorized Change

- Add a live probe script that starts the local CVF web app with a temporary
  file-backed durable-memory store.
- Execute turn 1 with `durableMemoryWrite.enabled=true`.
- Execute turn 2 with `durableMemory.enabled=true` against the same scope.
- Verify the second turn reads the first turn's memory by receipt evidence.

## Decision / Baseline / Proposed Tranche

Decision: continue.

Baseline: durable memory write and durable memory read are individually proven.

Proposed tranche: WC-1 proves the read/write workflow chain across two live
governed calls using existing runtime surfaces.

## Evidence Plan

- `node scripts/run_cvf_wc1_workflow_chain_probe.mjs`
- `npm run check` in `cvf-web`
- Mandatory release gate bundle
- Completion review with receipt ids, trace ids, memory ids, and boundary

## Acceptance Criteria

- [ ] Turn 1 returns live receipt and `durableMemoryWriteReceipt`.
- [ ] Turn 2 returns live receipt and `durableMemoryRead`.
- [ ] Turn 2 read receipt includes turn 1 memory id.
- [ ] Both durable receipts preserve `rawMemoryReleased=false`.
- [ ] Both durable receipts preserve `canReinject=false`.
- [ ] Raw secrets are not printed.

## Claim Boundary

WC-1 may claim only one bounded two-turn workflow-chain proof using existing
local route surfaces and a temporary local durable-memory store. It does not
claim hosted/cloud memory persistence, autonomous memory behavior, raw-memory
prompt injection, universal workflow reliability, provider stability, production
readiness, or new governance authority.
