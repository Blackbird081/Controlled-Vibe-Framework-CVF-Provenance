# CVF CDH-D Delta Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED_NON_BLOCKING_WITH_SUBSURFACE_SPLIT

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

File the reviewer-only rebuttal for CDH-D in the CDH delta meta-roadmap.

This rebuttal separates provider-method residual work into three distinct
surfaces: vision contract, vision runtime, and reasoning contract. It rejects
any bundled runtime claim.

---

## Scope / Target / Owner Boundary

In scope:

- `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- `docs/work_orders/CVF_WO_CDH_D_DELTA_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/reasoning-contract.ts`
- matching contract tests

Out of scope:

- provider vision runtime;
- image fetching;
- Maika photo description;
- reasoning runtime;
- bundled provider-method runtime parity;
- public provider capability claims.

---

## Target / Source Under Review

Queue item:

- `cdh-d-delta`

Expected response path:

- `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`

Prior closure evidence:

- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`

---

## Scope / Methodology

Method:

1. Reviewed the D2 vision-contract completion packet.
2. Reviewed the W1 provider-contract completion packet.
3. Re-read `vision-contract.ts`, `vision-contract.test.ts`,
   `reasoning-contract.ts`, and `reasoning-contract.test.ts`.
4. Split the residual D surface into already-closed contract work and any
   future runtime work that would require a fresh GC-018.

No live provider or image invocation was run for this rebuttal. This is a
reviewer packet, not a runtime closure packet.

---

## Findings / Position

Position: **NON_BLOCKING_WITH_SUBSURFACE_SPLIT**.

Findings:

1. Vision contract is already closed by D2. The Model Gateway defines
   `VisionRequest`, `VisionContract`, `VisionCapableProvider`, required
   fields, a type guard, tests, exports, and an optional adapter stub. The D2
   closure explicitly excludes provider implementation, HTTP/image fetch,
   vision runtime routing, and Maika photo description.
2. Reasoning contract is already present from W1. The Model Gateway defines
   `ReasoningRequest`, `ReasoningContract`, `ReasoningCapableProvider`,
   required fields, a type guard, tests, and exports. The W1 closure
   explicitly excludes provider implementation, runtime routing, adapter
   method parity, and live AI capability proof.
3. Vision runtime remains a separate, unproved runtime surface. It cannot be
   bundled with the already-closed contract work and cannot be claimed from
   Maika text-summary proof.
4. Reasoning runtime remains out of scope. A reasoning contract does not imply
   reasoning runtime, provider method parity, or live reasoning support.
5. CDH-D can proceed only if the next work order selects exactly one
   sub-surface and states its claim boundary before implementation.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Contract evidence is overstated as runtime provider support | Keep D2/W1 as contract-only closures |
| Vision runtime is bundled with reasoning contract or Maika text proof | Require separate GC-018 and work order for vision runtime only |
| Reasoning contract is converted into reasoning runtime | Reject reasoning runtime unless a future roadmap explicitly authorizes it |
| Public capability claims escape private provenance | No public-sync/provider claim without separate public-safe proof and authorized sync |

---

## Decision / Recommendation / Disposition

Disposition: **NON_BLOCKING_WITH_SUBSURFACE_SPLIT**.

CDH-D may proceed only after a fresh slice-specific GC-018 chooses one of the
following sub-surfaces:

| Sub-surface | Current disposition | Future gate |
| --- | --- | --- |
| Vision contract | Already closed by D2 | No new implementation unless a specific contract defect is identified |
| Reasoning contract | Already closed by W1 | No runtime claim; contract-only evidence is already filed |
| Vision runtime | Not proved | Requires separate GC-018, live provider proof, image handling controls, audit evidence, and a narrow claim boundary |

No bundled runtime claim is authorized. Reasoning runtime is not authorized by
this rebuttal.

---

## Claim Boundary

This rebuttal may be cited as:

> CDH-D is non-blocking only after splitting provider-method work into vision
> contract, vision runtime, and reasoning contract. Vision and reasoning
> contracts have contract-only closure evidence; vision runtime remains a
> separate future gate.

This rebuttal must not be cited as:

> CVF has live vision runtime support, Maika photo support, reasoning runtime,
> or bundled provider-method runtime parity.

