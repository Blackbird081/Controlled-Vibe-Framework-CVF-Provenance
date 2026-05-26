# CVF LHW1 Legacy Workflow Connector Absorption Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-05-27

## Purpose

Return from Surface 1 export cleanup to legacy knowledge absorption, but only
for high-value workflow pieces that already exist and mainly need a clean CVF
connector standard.

LHW1 is not broad legacy archaeology. It is a connector tranche: identify
disconnected workflow parts, normalize the accepted value into CVF-owned
workflow surfaces, and produce the minimum standard needed for later runtime or
UI implementation.

## Operator Direction

Operator priority:

- continue absorbing valuable legacy knowledge;
- complete workflow chains where useful pieces already exist;
- avoid going deep into low-value areas;
- prioritize flows with requirements, role packets, receipts, context capture,
  skill packs, or UI pieces already present but not connected.

## Knowledge Absorption Blind-Spot Control Block

Control standard:

`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources to resolve before implementation:

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_LH1_LEGACY_HARVEST_CLOSEOUT_LEDGER_COMPLETION_2026-05-25.md`
- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- prior W-series work orders for WC-3 Candidates 1-4 where already closed or partially wired
- `docs/roadmaps/CVF_MA1_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_ROADMAP_2026-05-26.md`

Accepted-source rule:

- Read detailed source files for the selected connector family before
  implementation.
- Do not scope from summaries alone.
- Record accept/defer/reject disposition for every source family touched.

Blind-spot adversarial roles:

- Workflow Architect: checks whether the connector creates an actual workflow
  chain rather than another prose standard.
- Non-Coder Value Reviewer: checks whether the connected flow helps a
  non-coder get work done.
- Governance Auditor: checks ownership, receipts, boundaries, and no hidden
  runtime claim.
- Integration Maintainer: checks whether the connector can be wired later
  without broad rewrites.

Stop rule:

- If the selected source family requires broad runtime execution, raw memory
  reinjection, external skill ingestion, database mutation, or provider
  behavior changes, stop and split into a fresh GC-018.

Blind-spot verdict: CLEAR.

Basis: all five scope sources exist and are readable; candidate screen maps
directly to LH1 ledger dispositions; no new source family is opened without
a ledger trigger; adversarial roles completed above; Candidate 7 external
ingestion remains HOLD; no runtime, memory, or provider surface is touched
in T1/T2/T3.

## Candidate Screen

| Priority | Connector family | Existing pieces | LHW1 value | Initial disposition |
| --- | --- | --- | --- | --- |
| 1 | Product skill pack workflow connector | C7A top-10 packs, C8 selection readout, Review CVF Problem B, existing template/export work | Turns static skill packs into selectable workflow chains for non-coders | ACCEPT for T1 |
| 2 | Workflow state-machine connector | WC-3 Candidate 1, CVF Edit, Human System Harness, MA1 | Connects phases, role handoff, review gates, and recovery into one chain standard | ACCEPT for T2 if T1 clean |
| 3 | Context capture connector | caveman, Workflow GoClaw, VI2 context profile readouts | Connects intake context/profile to workflow handoff without overbuilding memory | ACCEPT with narrow readout boundary |
| 4 | Memory event capture connector | agentmemory, VI3 capture record, M1/M2 memory boundaries | Connects event capture to receipts and summary-only packaging with `canReinject=false` | DEFER unless workflow connector needs it |
| 5 | Tool/MCP/database action connector | WC-3 Candidate 3, MCP Gamma, CLI-Anything, OpenAgentd, pancake-pos-mcp | Important but higher risk; should follow workflow connector clarity | DEFER |
| 6 | External skill ingestion connector | Candidate 7, ES1/C7B/C7C | Valuable later, but needs demand and action governance | HOLD |

## Recommended Sequence

### LHW1-T1 - Product Skill Pack Workflow Connector

Deliverables:

- a canonical connector spec that turns a certified product skill pack into a
  non-coder workflow chain;
- required fields for skill pack metadata, workflow spec, execution policy,
  review checklist, receipt schema, and failure recovery;
- mapping from current web templates/spec export surfaces into the connector;
- one or two example connector records from existing certified packs.

The connector spec and all example records are document artifacts.
No cvf-web source files, routes, or components are changed in T1.
No runtime execution in T1.

### LHW1-T2 - Workflow Chain State Connector

Deliverables:

- a state connector that binds Intake -> Design -> Build -> Review -> Freeze to
  role assignments, evidence receipts, and recovery states;
- MA1-compatible role transfer packet fields;
- dissent/review handoff requirements;
- boundary for what must be runtime-enforced later versus document-only now.

Dispatch only if T1 proves the connector shape is useful.

### LHW1-T3 - Context Profile Connector

Deliverables:

- a connector between non-coder context capture, route/profile readouts, and the
  workflow packet;
- clear compaction and relevance rules inspired by caveman/GoClaw sources;
- no raw memory reinjection and no provider route behavior change.

Dispatch only if T1/T2 expose a concrete context gap.

## Verification

Roadmap-level verification:

- source files cited and dispositions recorded;
- connector standard is in English and machine-readable enough for future
  validators;
- one or two example records can be read by an agent without extra oral context;
- no runtime/provider/memory claim is made without live proof.

Implementation-level verification, when authorized:

- static unit tests for connector schema or validator if code is added;
- document lint/consistency checks for examples;
- live provider proof only if the tranche claims governance behavior through
  `/api/execute` or provider execution.

## Claim Boundary

LHW1 as proposed is a roadmap and connector-normalization tranche. It does not
claim runtime workflow enforcement, external skill ingestion, MCP/tool action
execution, memory reinjection, hosted readiness, production readiness, or
public release readiness.
