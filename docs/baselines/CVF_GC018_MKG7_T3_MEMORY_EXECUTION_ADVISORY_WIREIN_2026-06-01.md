# CVF GC-018 - MKG7-T3 Memory Execution Advisory Wire-In

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize MKG7-T3: wire a compact, bounded Memory advisory readout object into
the `/api/execute` governed execution response as an advisory-only evidence
field. The advisory must not interfere with the existing memory paths already
present in the route (`evaluateDurableMemoryRoute`, `evaluateAifMemoryReinjection`,
lines 637–646 @ `route.ts`), must not influence provider execution, and must
not grow `/api/execute/route.ts` beyond the 1000-line hard threshold.

T3 is guarded by file-size, source, and helper-extraction requirements.

## Scope / Target / Owner Boundary

Target owner surfaces:

- helper module (NEW): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.ts`
- test (NEW): `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-advisory.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — additive advisory field only; must stay ≤ 858 lines after change (current: 858)
- `docs/reviews/CVF_MKG7_T3_MEMORY_EXECUTION_ADVISORY_WIREIN_COMPLETION_2026-06-01.md` (NEW)

Source-of-truth files (read-only):

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` — readout shape contract
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` — projection helper
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` — T2 output (must exist)
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` — T1 contract

Boundary: advisory-only field in response envelope; must not modify existing
durable-memory or AIF-memory-reinjection paths; no provider calls; no raw
Memory release; no public-sync.

## Decision

Authorize T3 as a bounded helper-first integration: extract advisory builder
into a new helper module, add an advisory-only field to the ALLOW response
envelope, and add focused tests. If adding the field would push route.ts above
858 lines, the worker must extract additional helper logic first (minimum shrink
target: 50 lines) before adding. Leave pending and uncommitted.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Execute route (additive only) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (858 lines) | ACCEPT_FOR_ADDITIVE_ADVISORY_FIELD — must not exceed 858 lines after change; if growth needed, extract helper first |
| Existing durable memory path | lines 637–638 @ `route.ts` | ACCEPT_AS_READ_ONLY — must not be modified |
| Existing AIF memory reinjection path | lines 639–646 @ `route.ts` | ACCEPT_AS_READ_ONLY — must not be modified |
| Readout projection helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | ACCEPT_AS_CONTRACT_SOURCE |

## Source / Predecessor Evidence

- T2 eligibility policy must exist before T3 is executed.
- Execute route currently at 858 lines (hard limit 1000). No helper extraction required unless T3 addition would exceed 858 lines.
- Existing memory paths in execute route (`evaluateDurableMemoryRoute` line 637, `evaluateAifMemoryReinjection` line 639) are active; T3 advisory field must be additive and must not touch these paths.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

Bounded cvf-web owner set plus LPF T2 output. No Legacy folder absorption.
Filesystem corpus listing is `N/A with reason`.

### Gate 2 - Prior Absorption Resolution

MKG1–MKG6 closed, T1 contract complete, T2 eligibility policy complete.

### Gate 3 - File-Level Value Extraction

The advisory readout object is a compact, summary-only projection of the MKG6
`buildMemoryRuntimeReadout` result, annotated with the T2 eligibility decision.
It must not include raw candidate content.

### Gate 4 - Owner-Surface Normalization

New advisory builder lives in a dedicated helper module under
`src/app/api/execute/` — same owner domain as the route. The route imports only
the builder; advisory object is additive in the ALLOW response envelope.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Advisory field in ALLOW response | ACCEPT_NOW | bounded additive only |
| Modifying durable/AIF memory paths | REJECT_DIRECT | forbidden by T3 boundary |
| Enforcement (advisory → policy gate) | DEFER — requires separate GC-018 | T3 is advisory-only |

### Gate 6 - Adversarial Role Review

Risk: worker modifies existing durable-memory or reinjection paths while adding
advisory. Required: diff must show only additive changes to route.ts; existing
memory paths untouched.

### Gate 7 - Thin Proof And Closure Delta

New helper module, focused tests asserting advisory-only behavior and that
existing memory paths are untouched, cvf-web `npm run check` PASS, file-size
guard PASS, execute-route step-sequence guard PASS.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- new helper module with advisory builder;
- focused tests: advisory field present in ALLOW response, `rawMemoryReleased=false`, `canReinject=false`, existing memory path receipts unaffected;
- cvf-web `npm run check` PASS;
- `python governance/compat/check_execute_route_step_sequence.py --enforce` PASS;
- `python governance/compat/check_governed_file_size.py --enforce` PASS;
- pending completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T3 authorizes an advisory-only Memory readout field in the execute response.
Does not authorize modifying existing memory paths, enforcement behavior,
provider calls, raw Memory release, prompt injection, persistence mutation,
public-sync, or push.
