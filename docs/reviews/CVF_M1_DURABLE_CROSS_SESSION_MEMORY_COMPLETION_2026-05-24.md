# CVF M1 - Durable Cross-Session Memory Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: review

Date: 2026-05-24

Tranche: M1

Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Close the M1 durable-memory tranche after verifying policy-gated durable
read/write receipts for existing `skill` and `long-term` tiers.

---

## Scope / Target / Owner Boundary

Target: LPF durable memory store and runtime memory hierarchy.

Owner: CVF Learning Plane memory governance surface.

Boundary: only `skill` and `long-term` durable persistence are in scope; no
provider prompt raw memory, autonomous writes, or hosted/cloud persistence are
claimed.

---

## Target / Source

Sources: M1 GC-018 baseline, M2 completion review, legacy `agentmemory` source
folder, and C2 summary-only memory reinjection gate.

---

## Scope / Methodology

Method: verify M2 closed before implementation, scan legacy memory specs,
implement durable stores, test write/read/privacy/cross-session behavior, and
run one live route proof using summary-only C2 reuse.

---

## Result

M1 is `CLOSED_PASS`.

Delivered bounded durable memory for the existing `skill` and `long-term`
tiers with policy-gated write/read receipts. `canReinject=false` remains
binding; contextual reuse is summary-only through the existing C2 gate.

---

## M2 Precondition

M2 was verified `CLOSED_PASS` before M1 implementation:

- `docs/reviews/CVF_M2_D06_MEMORY_TIER_FREEZE_RELEASE_COMPLETION_2026-05-24.md`
- Owner map records `freeze_released: true` for
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`.

---

## Legacy Spec Scan

The active legacy registry was read:

- `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

The M1 design was checked against the legacy `agentmemory` folder:

- `CVF_CONTROLLED_MEMORY_GATEWAY.md`
- `CVF_MEMORY_ACCESS_POLICY.md`
- `CVF_MEMORY_CAPTURE_ADAPTER.md`
- `CVF_MEMORY_CONTEXT_PACKAGER.md`
- `CVF_MEMORY_EVENT_HOOKS.md`
- `CVF_MEMORY_GUARD_CONTRACT.md`
- `CVF_MEMORY_LIFECYCLE_POLICY.md`
- `CVF_MEMORY_PRIVACY_FILTER_POLICY.md`
- `CVF_MEMORY_REINJECTION_PROTOCOL.md`
- `CVF_MEMORY_RETRIEVAL_POLICY.md`
- `Thong_tin.md`

Design decisions retained from the legacy scan:

- all memory access requires scope;
- write/read operations emit receipts;
- raw secrets and raw memory payloads are excluded before persistence;
- retrieval and reinjection remain separately approved;
- reinjection is summary-only and governed by the C2 gate.

---

## Implementation

Files added or changed:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/durable-memory-store.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/runtime-memory-hierarchy.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- `scripts/run_cvf_m1_durable_memory_live_probe.mjs`

The store supports:

- in-process and file-backed durable memory backends;
- durable write/read receipts;
- `skill` and `long-term` tiers only;
- write-time privacy/lifecycle/provenance filters;
- cross-session file-backed read proof;
- summary-only live route reuse through C2 memory reinjection.

---

## Evidence

Evidence JSON:

- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_EVIDENCE_2026-05-24.json`

Verification:

| Check | Result |
| --- | --- |
| Targeted LPF tests | PASS - `durable-memory-store.test.ts` + `runtime-memory-hierarchy.test.ts`, 16/16 |
| LPF TypeScript | PASS - `npm run check` |
| Live proof | PASS - `node scripts/run_cvf_m1_durable_memory_live_probe.mjs` |
| Live receipt | `rcpt-env-mpjb6x9o-552qp0` |
| Live trace | `env-mpjb6x9o-552qp0` |
| Live provider/model | Alibaba `qwen-turbo` |
| Raw secret printed | false |
| Raw memory released | false |

Live proof facts:

- write memory id: `m1-skill-safe`;
- read memory id: `m1-skill-safe`;
- summary-only reinjected memory id: `m1-skill-safe`;
- raw payload item `m1-raw-rejected` excluded as
  `raw_memory_payload_rejected`.

---

## Findings / Position

Position: M1 closes the bounded durable-memory gap for existing `skill` and
`long-term` tiers. It does not reopen broader memory hierarchy or reinjection
boundaries.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Raw memory reaches provider prompt | Store and C2 gate reject raw payload fields; live proof excluded `m1-raw-rejected`. |
| `canReinject=false` is weakened | Runtime hierarchy and durable store tests assert `canReinject=false`. |
| Unauthorized tiers persist | Store rejects non-`skill`/`long-term` tiers. |

---

## Decision / Recommendation / Disposition

Disposition: `CLOSED_PASS`.

---

## Claim Boundary

Allowed claim:

- bounded durable memory for `skill` and `long-term` tiers with policy-gated
  cross-session read/write receipts and summary-only C2 contextual reuse.

Not claimed:

- autonomous memory write;
- `canReinject=true`;
- raw memory prompt reinjection;
- organizational, working, task, audit, or receipt tier persistence;
- hosted/cloud persistence;
- broad memory authority;
- enterprise production readiness;
- global freeze release.
