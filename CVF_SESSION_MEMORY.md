# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-25

Current mode marker: `c7a_product_skill_pack_top10_closed`

Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the single session-memory entry point for new agents, resumed
agents, future `cvf-cli`, and future `cvf-mcp-server` startup.

It is intentionally compact. The previous long front-door snapshot was archived
verbatim at
`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_C7A_REFRESH_ARCHIVE_2026-05-25.md`.

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff:
   `AGENT_HANDOFF_V13_2026-05-25.md`
5. Read mandatory startup guards listed in the state registry.

Pain-point closure direction:

`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

Previous handoff archive:

`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V12_2026-05-23.md`

## Current State

Current mode: `c7a_product_skill_pack_top10_closed`.

C7A closed PASS bounded at:

`docs/reviews/CVF_C7A_PRODUCT_SKILL_PACK_TOP10_COMPLETION_2026-05-25.md`

The certified product skill pack inventory now has ten unique static packs:

- `strategy_analysis`
- `product_brief`
- `sop_generator`
- `proposal_writer`
- `meeting_summarizer`
- `contract_review`
- `landing_page_builder`
- `competitor_review`
- `data_analysis`
- `app_requirements_spec`

Registry:

`governance/registries/cvf-certified-skill-pack-registry.json`

Validation evidence: `scripts/validate_skill_pack_certification.py` PASS for
all ten packs; registry check `entries=10 unique=10 c7a=3`.

## Candidate 7 Decision

Candidate 7 is not a green light for broad external ingestion.

What is closed:

- C7A completed the practical product-skill-pack inventory from seven to ten
  strong workflows using the existing T1/T2/W7 intake chain.

What remains held:

- external skill/model ingestion;
- direct tool execution;
- MCP or database action execution;
- provider/runtime behavior changes;
- public-sync or hosted/product-readiness claims.

Candidate 7 may reopen only with fresh GC-018, the mandatory Knowledge
Absorption Blind-Spot Control Block, and a concrete source/use-case binding.

## Recommended Next Tranche

Recommended next value tranche: product skill pack selection/readout quality.

Rationale: after C7A, CVF has enough pack inventory to choose from. The higher
value move is now helping LLM/agents select the right certified pack, explain
why, report risk/review requirements, and say when no pack should be used.

Bounded target for that future tranche:

- deterministic pack selection/readout helper over the ten certified packs;
- no new packs by default;
- no runtime execution;
- no provider calls;
- no receipt-envelope change;
- no memory, MCP, database, tool, public-sync, hosted readiness, production
  readiness, or freeze-release change.

Required before implementation: fresh GC-018 and work order.

## Mandatory Standards

Live run diagnostics:

`docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

Knowledge absorption blind-spot prevention:

`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Every GC-018 memory/graph/intelligence tranche must include the Knowledge
Absorption Blind-Spot Control Block.

## Boundary

This front door is routing state only. It does not replace evidence packets,
roadmaps, handoffs, governance guards, or the machine-readable state registry.

Do not continue broad F-1 tuning. Do not claim output-quality parity. Do not
push public-facing changes from this provenance workspace.
