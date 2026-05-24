# CVF WC-1 Workflow Chain Proof Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-05-24

---

## Purpose

Close WC-1 after proving a bounded two-turn workflow chain using existing CVF
runtime surfaces: a governed live execution writes summary-only durable memory,
then a second governed live execution reads that same memory by receipt
evidence.

## Scope / Target / Owner Boundary

Scope: proof artifact and governance status only.

Target:

- `scripts/run_cvf_wc1_workflow_chain_probe.mjs`
- `docs/reviews/CVF_WC1_WORKFLOW_CHAIN_PROOF_EVIDENCE_2026-05-24.json`
- `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

Out of scope: route/provider behavior changes, new receipt-envelope fields,
new memory tiers, autonomous memory write, `canReinject=true`, raw-memory prompt
injection, hosted/cloud persistence, production readiness, or freeze release.

## Target / Source

Target: WC-1 read/write workflow-chain proof.

Source: WC-1 GC-018, WC-1 work order, R2 durable-memory read closure, S1
durable-memory write closure, and live WC-1 probe output.

## Evidence Trace

- GC-018:
  `docs/baselines/CVF_GC018_WC1_WORKFLOW_CHAIN_PROOF_2026-05-24.md`
- Work order:
  `docs/work_orders/CVF_WO_WC1_WORKFLOW_CHAIN_PROOF_2026-05-24.md`
- Roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- Evidence JSON:
  `docs/reviews/CVF_WC1_WORKFLOW_CHAIN_PROOF_EVIDENCE_2026-05-24.json`

## Findings

WC-1 is closed pass bounded.

Implemented:

- Added `scripts/run_cvf_wc1_workflow_chain_probe.mjs`.
- The probe starts CVF Web with a temporary file-backed durable-memory store.
- Turn 1 sends a signed live `/api/execute` call with
  `durableMemoryWrite.enabled=true`.
- Turn 2 sends a signed live `/api/execute` call with
  `durableMemory.enabled=true` against the same scope.
- The proof checks turn 2 receipt evidence rather than relying on model output.

## Verification / Evidence

Live probe:

`node scripts/run_cvf_wc1_workflow_chain_probe.mjs`

Result: PASS.

Turn 1:

- HTTP 200.
- `success=true`.
- provider/model: Alibaba `qwen-turbo`.
- receipt: `rcpt-env-mpjrwfuh-opgp5q`.
- trace: `env-mpjrwfuh-opgp5q`.
- `evidenceMode=live`.
- durable write decision: `allowed`.
- memory id: `s1-4da7cc23-8a60-4005-9084-a85787ed3660`.
- `rawMemoryReleased=false`.
- `canReinject=false`.

Turn 2:

- HTTP 200.
- `success=true`.
- provider/model: Alibaba `qwen-turbo`.
- receipt: `rcpt-env-mpjrwowf-omx3d7`.
- trace: `env-mpjrwowf-omx3d7`.
- `evidenceMode=live`.
- durable read decision: `allowed`.
- durable read memory ids include turn 1 memory id:
  `s1-4da7cc23-8a60-4005-9084-a85787ed3660`.
- `summaryOnly=true`.
- `rawMemoryReleased=false`.
- `canReinject=false`.

Security:

- `rawSecretPrinted=false`.
- request headers not printed.
- temporary durable-memory store removed after probe.

Additional verification:

- `node --check scripts/run_cvf_wc1_workflow_chain_probe.mjs`: PASS.
- `npm run check` in `cvf-web`: PASS.
- Markdown structural completeness: PASS.
- `python scripts/run_cvf_release_gate_bundle.py --json`: PASS `7/7`.

## Acceptance Criteria

- [x] Live receipt from turn 1 includes `durableMemoryWriteReceipt`.
- [x] Live receipt from turn 2 confirms prior session context retrieval through
      durable-memory read evidence.
- [x] Turn 2 read receipt includes turn 1 memory id.
- [x] `rawMemoryReleased=false` in both durable receipts.
- [x] `canReinject=false` preserved.
- [x] `evidenceMode=live` on both calls.
- [x] `rawSecretPrinted=false`.

## Risk / Corrective Action

Risk: readers may overinterpret WC-1 as a general autonomous memory or hosted
persistence claim.

Corrective action: WC-1 explicitly proves only a local two-turn chain using
existing route read/write surfaces and receipt evidence.

## Disposition

`CLOSED_PASS_BOUNDED`.

## Claim Boundary

WC-1 claims one bounded two-turn live workflow-chain proof using existing local
CVF route surfaces and a temporary local durable-memory store. It does not claim
hosted/cloud memory persistence, autonomous memory behavior, raw-memory prompt
injection, universal workflow reliability, provider stability, production
readiness, or new governance authority.
