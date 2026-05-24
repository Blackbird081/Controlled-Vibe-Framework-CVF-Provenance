# CVF CDH Delta Meta-Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL

docType: roadmap

Date: 2026-05-20

---

## Status

READY_FOR_REBUTTAL. This is a static meta-roadmap filing only. It does not
authorize implementation, GC-018 filing, provider runtime work, memory runtime
work, Maika changes, or public claims.

## Authorization / Decision

Authorized as HN3 filing-only work by
`docs/work_orders/CVF_WO_HN3_CDH_DELTA_META_ROADMAP_2026-05-20.md`, following
Claude's `NON_BLOCKING_WITH_PER_SLICE_GATING` rebuttal on the post-pain-point
hardening roadmap. The decision is to replace the original BLOCKED CDH roadmap
with independent C/D/H/M delta slices.

## Purpose

Provide one corrected planning artifact for the CDH/M runtime-maturity delta
family. The artifact preserves the useful downstream direction while keeping
each slice independently rebutted, GC-018-gated, and work-ordered.

## Scope / Target / Owner Boundary

In scope:

- M delta: Maika text-summary deployment verification through the governed CVF
  path only.
- H delta: audit-memory policy refinement over the existing receipt flow.
- C delta: existing CLI execute hardening and live-proof/persistence framing.
- D delta: vision contract, vision runtime, and reasoning contract as separate
  sub-surfaces.
- Queue entries for independent per-slice rebuttals.

Out of scope:

- implementation of any slice;
- GC-018 for any slice;
- unified CDH closure;
- code, test, provider, memory, Maika, or public-sync changes.

Owner boundary: Orchestrator files per-slice candidate packets later; Reviewer
rebuts each slice independently; Worker implementation begins only after that
slice has its own GC-018 and work order.

## Predecessor Evidence

- `docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`
- `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `docs/reviews/archive/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

## Replacement Notice

This meta-roadmap replaces the BLOCKED
`docs/roadmaps/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`. The four
BLOCKING_FINDINGS from
`docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
remain load-bearing per slice. Do not file GC-018 against the original roadmap;
use the slice gates below.

## Per-Slice Sections

### Per-Slice Section M

`sliceId`: `CDH-M`

`corrected scope`: M delta is limited to deployment verification and evidence
hardening for the already implemented Maika text-only daily summary Edge
Function. It may prove the function calls CVF `/api/execute` with minimized
text payload through the governed path, but it must not introduce image/photo
handling, direct provider fallback, or child-data proof outside the bounded
text-summary surface.

`loadBearingConstraint`: Must NOT use Maika child / health / photo data as
low-governance proof (Finding 4). Text-summary only through governed CVF path
until vision runtime is separately accepted.

`evidenceAnchor`: `docs/reviews/archive/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`

`downstreamGate`: Next step requires a rebuttal cycle, then a slice-specific
GC-018, then a work order. Live proof must use deployed Supabase Edge Function
invocation with an authenticated admin or teacher session, and must not print
or copy raw keys.

`nonGoals`:

- no bundled CDH closure;
- no Maika photo-description proof;
- no direct provider fallback;
- no public-sync claim;
- no child identity or contact payload proof.

`acceptanceCriteriaSeed`:

- deployed function invocation returns governed CVF response;
- request payload evidence shows minimized text fields only;
- no direct provider SDK/import/call is present;
- fallback remains local rule-based text only;
- completion review records deployment verification and residual privacy risk.

### Per-Slice Section H

`sliceId`: `CDH-H`

`corrected scope`: H delta is limited to policy/readout refinement over the
existing audit-memory receipt path. It may improve how receipt write metadata,
privacy filters, degraded capture, and audit readout are represented, while
preserving the existing no-reinjection capture invariant.

`loadBearingConstraint`: Must NOT treat `reinjectionAllowed` as a
memory-capture write gate (Finding 2). Capture vs reinjection boundary is
preserved.

`evidenceAnchor`: `docs/reviews/archive/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

`downstreamGate`: Next step requires a rebuttal cycle, then a slice-specific
GC-018, then a work order. Live proof must exercise the existing `/api/execute`
audit-memory receipt path and verify receipt fields without enabling prompt
reinjection.

`nonGoals`:

- no bundled CDH closure;
- no persistent/archive memory enablement;
- no provider-side memory behavior;
- no new memory tier;
- no frozen memory-policy rewrite.

`acceptanceCriteriaSeed`:

- audit-memory receipt preserves `canReinject: false`;
- `writesRequireReceipt` and `privacyFilters` remain visible in receipt output;
- degraded capture is represented honestly in an audit event;
- tests verify no `reinjectionAllowed` write gate;
- live proof uses the existing governed execute path.

### Per-Slice Section C

`sliceId`: `CDH-C`

`corrected scope`: C delta starts from the existing `cvf execute` command and
may add live CLI proof, installability evidence, JSONL receipt persistence
verification, or operator-facing diagnostics. It is not an add-first-command
tranche.

`loadBearingConstraint`: Must NOT claim `cvf execute` is missing (Finding 1).
Existing CLI execute surface remains the baseline.

`evidenceAnchor`: `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`

`downstreamGate`: Next step requires a rebuttal cycle, then a slice-specific
GC-018, then a work order. Live proof must call the current governed `/api/execute`
route or explicitly remain local-only with no live claim.

`nonGoals`:

- no bundled CDH closure;
- no new CLI verb family;
- no provider/runtime behavior change;
- no claim that execute was absent;
- no public release claim without public-sync review.

`acceptanceCriteriaSeed`:

- current `cvf execute` baseline remains intact;
- dry-run remains secret-redacted;
- JSONL receipt persistence is verified with schema-relevant fields;
- live or local-only proof boundary is explicit;
- CLI tests and type checks pass.

### Per-Slice Section D

`sliceId`: `CDH-D`

`corrected scope`: D delta is split into three sub-surfaces: Vision contract
(typed shape only; no provider call), Vision runtime (provider call plus
audit-event capture), and Reasoning contract (typed shape only). Reasoning
runtime is OUT OF SCOPE for this meta-roadmap and would need its own roadmap
later.

`loadBearingConstraint`: Must NOT bundle contract-only with provider runtime
claims (Finding 3). Three sub-surfaces (vision contract / vision runtime /
reasoning contract) gate independently.

`evidenceAnchor`: `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`

`downstreamGate`: Next step requires a rebuttal cycle, then one slice-specific
GC-018 per selected D sub-surface, then a work order. Vision runtime requires a
real provider call and audit-event capture; contract-only sub-surfaces require
type/test proof and no runtime claim.

`nonGoals`:

- no bundled CDH closure;
- no reasoning runtime;
- no Maika photo proof unless vision runtime is separately accepted;
- no hidden provider routing change;
- no contract-only packet claiming live runtime.

`acceptanceCriteriaSeed`:

- selected D sub-surface is named before GC-018;
- contract-only work has type/test evidence and no provider call;
- vision runtime work has live provider evidence and audit capture;
- reasoning runtime remains excluded;
- completion review states exact provider/runtime claim boundary.

## Cross-Slice Non-Goals

- Do not file one unified CDH-delta GC-018.
- Do not dispatch one bundled C/D/H/M work order.
- Do not treat prior completion packets as authorization for new runtime work.
- Do not make public claims from this private planning artifact.
- Do not reopen any Review-CVF A-H pain point.

## Downstream Dispatch Order

Recommended order:

1. M delta first, because it is the active Maika product verification need and
   can remain text-only.
2. H delta second, because it hardens receipt truth without widening provider
   behavior.
3. C delta third, because live CLI proof depends on a stable governed route
   posture.
4. D delta last, because vision runtime is the heaviest and contract/runtime
   separation is the easiest place to overclaim.

This order is advisory. Each slice still needs independent rebuttal, GC-018,
and a work order.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Original CDH roadmap is reused directly | Mark it REPLACED_BY_META and keep BLOCKING_FINDINGS load-bearing |
| Slices get bundled again | Queue four independent rebuttal items and forbid unified GC-018 |
| D contract/runtime claims blur | Require D sub-surface selection before GC-018 |
| M privacy proof overreaches | Keep M text-summary only until D vision runtime separately passes |
| H capture/reinjection boundary blurs | Restate the `reinjectionAllowed` constraint in the H slice |

## Non-Goals

- Implementation.
- GC-018 filing.
- Runtime/provider/memory/Maika edits.
- Public-sync publication.
- Claiming runtime maturity closure.
- Updating pain-point closure status.

## Work Plan

1. File this meta-roadmap.
2. Mark the original CDH roadmap as `REPLACED_BY_META`.
3. Add four independent queue items for M/H/C/D rebuttals.
4. Close HN3 as a filing-only tranche.
5. Wait for the operator/Orchestrator to select which slice to rebut first.

## Acceptance Criteria

- This file has all required roadmap sections.
- M/H/C/D slices each include `sliceId`, corrected scope,
  `loadBearingConstraint`, `evidenceAnchor`, `downstreamGate`, `nonGoals`, and
  `acceptanceCriteriaSeed`.
- The D slice explicitly names vision contract, vision runtime, and reasoning
  contract, and excludes reasoning runtime.
- Original CDH roadmap has a status note only.
- Active review queue has four new per-slice items.
- No implementation or GC-018 occurs in this tranche.

## Verification

Static verification only:

- Markdown structure check through local governance hook chain.
- JSON parse check for `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`.
- Git diff check that no code/runtime/provider/memory/Maika file changed.

## Related Artifacts

- `docs/work_orders/CVF_WO_HN3_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

## Claim Boundary

This meta-roadmap is a private planning router. It proves no runtime behavior,
authorizes no implementation, files no GC-018, and changes no public-facing CVF
claim.
