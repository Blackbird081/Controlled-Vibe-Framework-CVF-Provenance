# CVF R2 Execute Route Durable Memory Wiring Completion

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: review

Date: 2026-05-24

Tranche: R2

Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`

---

## Purpose

Close the R2 gap between M1 durable memory storage and the governed web
execution path.

---

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
and route-local durable-memory wiring.

Owner: CVF web governed execution route.

Boundary: R2 is an explicit request-policy read path only. It does not create
autonomous memory writes, graph authority, raw-memory prompt release,
`canReinject=true`, or hosted/cloud durable persistence.

---

## Target / Source

Sources: M1 durable memory completion, R1 durable store resilience, R2 GC-018,
and the existing `/api/execute` governance envelope.

---

## Scope / Methodology

Method: add typed `durableMemory` request input, route-local file-backed store
read evaluation, summary-only prompt block construction, receipt embedding in
`governanceEvidenceReceipt`, degraded denial receipts for missing/corrupt store
cases, focused route tests, one live provider proof, and the mandatory release
gate.

---

## Findings / Position

R2 is `CLOSED_PASS`. The governed web route can read bounded durable memory
when the request explicitly opts in and actor policy authorizes the read. The
receipt records the durable-memory decision and memory ids. The prompt context
contains summaries only, and `canReinject=false` remains binding.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Route reads memory without explicit policy | `durableMemory.enabled` and `policy.actorAuthorized=true` are both required. |
| Corrupt durable store breaks `/api/execute` | Route test covers corrupt JSON degradation to a denied/no-record receipt. |
| Provider sees raw memory | Prompt block is built from authorized summaries only; receipt records `rawMemoryReleased=false`. |
| Memory read is mistaken for authority | Prompt policy states context only, not approval authority, and `canReinject=false`. |

---

## Decision / Recommendation / Disposition

Disposition: `CLOSED_PASS`.

R3 handles the non-coder Step 0 setup gap separately. No additional durable
memory expansion should proceed without a fresh work order and claim boundary.

---

## Evidence Trace

- Authority:
  `docs/baselines/CVF_GC018_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_2026-05-24.md`
- Work order:
  `docs/work_orders/CVF_WO_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_2026-05-24.md`
- Evidence JSON:
  `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_EVIDENCE_2026-05-24.json`

---

## Evidence

Changed implementation:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`

Verification:

- Route durable-memory tests: PASS -
  `npm run test:run -- src/app/api/execute/route.durable-memory.test.ts`,
  3/3.
- `cvf-web` TypeScript/check gate: PASS - `npm run check`.
- Live R2 route proof: PASS -
  `node scripts/run_cvf_r2_durable_memory_route_live_probe.mjs`, receipt
  `rcpt-env-mpjdj5rc-p1g9go`, trace `env-mpjdj5rc-p1g9go`, provider
  `alibaba`, model `qwen-turbo`, memory id `r2-skill-safe`,
  `rawMemoryReleased=false`.
- Mandatory release gate: PASS -
  `python scripts/run_cvf_release_gate_bundle.py --json`, 7/7.

---

## Claim Boundary

Allowed claim: `/api/execute` can perform an explicit, policy-gated,
summary-only durable skill/long-term memory read and emit receipt evidence for
that read.

Not claimed: autonomous reinjection, raw-memory prompt injection,
`canReinject=true`, graph approval authority, hosted/cloud memory persistence,
enterprise SaaS/GA readiness, or broad production readiness.
