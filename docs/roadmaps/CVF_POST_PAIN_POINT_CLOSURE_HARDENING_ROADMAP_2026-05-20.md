# CVF Post Pain-Point Closure Hardening Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_CLAUDE_REBUTTAL

docType: roadmap

Date: 2026-05-20

---

## Purpose

Close the Review-CVF pain-point steering loop and define the next CVF
hardening choices without reopening A-H residual closure.

The 17.05 Review-CVF pain points are closed for the current contract. The next
work should be framed as CVF hardening, product expansion, or runtime maturity
delta work, not as residual pain-point closure.

This roadmap proposes three independent hardening directions for Claude
rebuttal.

---

## Scope / Target / Owner Boundary

Target:

- Post-pain-point CVF hardening direction after Review-CVF residual closure.

In scope:

- Marking A-H pain-point closure as complete for the current contract.
- Reframing next work as CVF hardening, not residual closure.
- Clarifying HN1, HN2, and HN3 for Claude rebuttal.
- Updating session front-door pointers so future agents load the hardening
  roadmap before selecting new work.

Out of scope:

- Implementing HN1, HN2, or HN3.
- Filing GC-018.
- Creating work orders.
- Editing public-sync.
- Reopening any Review-CVF A-H pain point.

Owner boundary:

- Codex authors this hardening roadmap and session-pointer update.
- Claude may rebut this roadmap as Orchestrator/Reviewer.
- Operator chooses which accepted hardening candidate proceeds to GC-018 or a
  work order.

---

## Authorization / Decision

Operator decision on 2026-05-20:

- N3 is withdrawn because Codex's review-gate trigger was correct.
- The pain-point steering file should be closed and reframed under CVF
  hardening.
- All three candidate directions are acceptable for clarification before
  Claude rebuttal.

Decision recorded here:

- Review-CVF A-H residual closure is closed.
- This roadmap becomes the active post-pain-point hardening direction.
- No candidate is authorized for implementation by this roadmap.

---

## Scope

This roadmap is a planning and steering artifact only.

HN1 is scoped to template-skill linkage coverage posture. HN2 is scoped to
governance-kernel owner mapping. HN3 is scoped to re-authoring the blocked CDH
runtime maturity roadmap as a current-state delta.

The candidates are independent. A future work order may select one candidate
without bundling the other two.

---

## Closure Baseline

Authoritative closure source:

- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

Current pain-point posture:

| Surface | Current status |
| --- | --- |
| A-H Review-CVF pain points | CLOSED for current residual closure contract |
| Remaining A-H candidate work | None |
| Post-residual N1 public catalog update | CLOSED, public commit `d11c772a` |
| Post-residual N2 workflow-chain V2 rebuttal | CLOSED_BY_PRIOR_TRANCHE |
| Post-residual N3 skill dead-reference repair | WITHDRAWN, zero dead references |

Do not use the stale `5/8 CLOSED, 3/8 PARTIAL` shorthand as a steering
baseline. It has been superseded.

---

## Candidate HN1 - Template-Skill Linkage Coverage Delta

Intent: audit and repair the remaining template-to-skill linkage coverage gap,
but only where the gap is real and current.

Evidence from current HEAD:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
  contains 27 public skills and all 27 indexed markdown paths resolve.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
  maps 58 template IDs to skills.
- Static template source under
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/` currently
  exposes 60 template IDs by direct `id` scan.
- The two unmapped template IDs are:
  - `individual_skills_folder`
  - `vibe_workflow_folder`
- Existing mapped template references have 0 broken skill refs against the
  current public skill index.

Corrected problem statement:

This is not a dead-reference repair and not a 118-template emergency. It is a
small linkage policy question: should the two development-folder templates
remain intentionally unmapped, be mapped to a current skill, or be classified
as non-skill surfaces with an explicit exemption?

Proposed scope:

- File an inventory of the two unmapped template IDs.
- Decide one class per ID: `map`, `exempt`, or `retire`.
- If `map`, require the target skill to exist in `skills-index.json`.
- If `exempt`, add an explicit reason so the guard does not regenerate false
  work orders.
- Keep public claims unchanged unless a public catalog sync is separately
  authorized.

Non-goals:

- Do not reopen N3 dead-reference repair.
- Do not widen the public skill corpus.
- Do not claim all templates must have a 1:1 skill.
- Do not edit runtime routing without a new work order.

Suggested gate:

Claude should rebut whether this can proceed as GC-044-compatible catalog
hygiene or whether it needs a fresh GC-018. Implementation must wait for that
rebuttal and a specific work order.

---

## Candidate HN2 - Governance Kernel Freeze Owner Map

Intent: convert the current governance-kernel freeze posture into a precise
owner-map and alias-table roadmap, without adding new governance semantics.

Evidence:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` still carries
  `freezePosture: governance_kernel_freeze_recommended`.

Corrected problem statement:

The residual A1 freeze-doc candidate was rejected because it duplicated active
guard-chain coverage. That does not eliminate the broader kernel-freeze
posture. The remaining hardening need is an owner map, not another doctrine
stack.

Proposed scope:

- Inventory kernel surfaces: authority, roles, policy decisions, risk model,
  guard model, execution lifecycle, delegation/handoff, receipts, memory,
  capability, provider execution, and vocabulary aliases.
- For each surface, assign one of: `canonical_owner`, `adapter_required`,
  `legacy_alias`, `deferred`, or `rejected`.
- Name the canonical owner file or explicitly mark `owner_gap`.
- Produce an alias table for terms that currently drift across docs and code.
- Produce a freeze-release rule: new kernel semantics require owner-map
  reference.

Non-goals:

- Do not add a new role taxonomy.
- Do not add a new PolicyEngine, RiskEngine, GuardEngine, receipt format, or
  memory tier.
- Do not promote private review packets into public claims.
- Do not claim runtime coherence merely because an owner map exists.

Suggested gate:

Claude should rebut whether HN2 is the correct strategic next roadmap or
whether it should be split into a pure inventory packet first. Any checker or
guard mutation requires a later GC-018 and work order.

---

## Candidate HN3 - Runtime Maturity CDH Delta Re-Authoring

Intent: rewrite the blocked CDH roadmap as a current-state delta roadmap,
using completion evidence already filed after the original CDH draft.

Evidence:

- `docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`
- `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `docs/reviews/CVF_LANE_C_EXECUTION_GATEWAY_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_LANE_H_MEMORY_RUNTIME_WIRING_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_M1_MAIKA_TEXT_SUMMARY_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

Corrected problem statement:

The original CDH roadmap is blocking because it was stale against HEAD and
mixed contract work, runtime claims, and Maika child-data proof. A valid next
roadmap must be a delta roadmap, not an implementation replay.

Proposed sub-slices:

| Slice | Corrected scope |
| --- | --- |
| C delta | Existing CLI execution gateway hardening only: live proof, install/bin wiring, dry-run, or JSONL persistence if justified. |
| D delta | Split vision contract, vision runtime, and reasoning contract. Do not bundle contract-only and provider runtime claims. |
| H delta | Policy refinement over existing audit-memory receipt flow. Preserve capture vs reinjection boundaries. |
| M delta | Maika text-summary integration only through governed CVF path; no direct provider fallback, no photo-description until vision runtime is separately accepted. |

Non-goals:

- Do not claim `cvf execute` is missing.
- Do not treat `reinjectionAllowed` as a memory-capture write gate.
- Do not use Maika child/health/photo data as low-governance proof.
- Do not close broad runtime maturity from one narrow delta.

Suggested gate:

Claude should rebut whether HN3 should be one delta roadmap with independent
GC-018 packets per sub-slice, or split immediately into separate C/D/H/M
roadmaps. Implementation must not begin from the original CDH roadmap.

---

## Recommended Order

Recommended sequence for rebuttal:

1. HN1 first: small, data-backed, likely to eliminate another misleading
   stale-memory item quickly.
2. HN2 second: strategic owner-map work that can reduce future scope drift.
3. HN3 third: highest runtime and data-safety risk; should only proceed after
   the stale CDH framing is rewritten.

Alternative:

If the operator wants strategic reconvergence before catalog hygiene, HN2 may
move before HN1. HN3 should not move first unless Claude narrows it to one
sub-slice and removes Maika child-data overclaim.

---

## Claude Rebuttal Questions

Claude should answer:

1. Is HN1 genuinely needed after the corrected 60/58/2 linkage inventory, or
   should the two development-folder templates be explicitly exempted without a
   full roadmap?
2. Should HN2 be a single governance-kernel owner-map roadmap, or should it be
   split into inventory, owner map, and guard integration tranches?
3. Should HN3 remain a unified CDH delta roadmap, or should C, D, H, and Maika
   be separated before any GC-018 is filed?
4. Which candidate, if any, needs public-sync involvement?
5. Which candidate requires live governance proof, and at what gate?

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Pain-point residual work is reopened under a new name | Keep A-H closure baseline fixed and require fresh hardening labels. |
| Stale `118 unlinked templates` claim regenerates bad work | Use the corrected current inventory: 60 templates, 58 mapped, 2 unmapped, 0 broken skill refs. |
| HN2 becomes governance theatre | Require owner files, alias classifications, and explicit non-enforcement boundaries. |
| HN3 overclaims runtime maturity | Split contract, runtime, and proof slices; require GC-018 before implementation. |
| Maika proof bypasses governance | Governed CVF path only; no direct provider fallback for proof claims. |

---

## Non-Goals

- Reopening Review-CVF A-H pain-point closure.
- Editing implementation files from this roadmap.
- Filing GC-018.
- Creating a downstream work order.
- Updating public claims.
- Treating this roadmap as release readiness.

---

## Work Plan

Roadmap-only work plan:

1. File this hardening roadmap.
2. Mark the pain-point closure direction packet as superseded/closed for active
   steering while preserving it as evidence.
3. Update session front-door pointers to reference this hardening roadmap.
4. Let Claude rebut HN1/HN2/HN3 and recommend sequencing.
5. After rebuttal, dispatch only the accepted candidate through its own
   GC-018/work-order gate if implementation is required.

Future implementation work plan:

- HN1 should start with a two-ID linkage inventory and classification.
- HN2 should start with a kernel-surface owner inventory.
- HN3 should start by rewriting or splitting the blocked CDH roadmap.

---

## Acceptance Criteria

This roadmap is ready for Claude rebuttal when:

- A-H pain-point closure is explicitly marked closed.
- HN1/HN2/HN3 each have evidence anchors, corrected problem statements,
  non-goals, and gates.
- The stale 118-template claim is corrected.
- The roadmap does not authorize implementation.

---

## Verification / Evidence

Static verification performed before filing:

- Active skill index path audit: 27 indexed skill markdown paths, 27 live.
- Template linkage scan: 60 static template IDs, 58 mapped, 2 unmapped.
- Skill linkage integrity: 0 mapped template IDs point to missing public skill
  refs.
- Active session state JSON parses successfully.
- Active review queue JSON parses successfully.

Commands used:

```powershell
Get-Content -Raw CVF_SESSION/ACTIVE_SESSION_STATE.json | ConvertFrom-Json
Get-Content -Raw CVF_SESSION/ACTIVE_REVIEW_QUEUE.json | ConvertFrom-Json
```

No live provider proof is required because this roadmap makes no runtime
governance claim.

---

## Related Artifacts

- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
- `docs/reviews/CVF_N3_SKILL_CORPUS_REPAIR_WORK_ORDER_WITHDRAWAL_2026-05-20.md`
- `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md`
- `docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`
- `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`

---

## Claim Boundary

This roadmap claims only a post-pain-point hardening direction ready for Claude
rebuttal. It does not authorize implementation, does not file GC-018, does not
change public claims, and does not reopen any Review-CVF A-H pain point.
