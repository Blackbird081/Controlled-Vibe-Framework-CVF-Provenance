# CVF MA1 Internal Multi-Agent Work Transfer Packet Roadmap

Memory class: ROADMAP_RECORD

docType: roadmap

Date: 2026-05-26

Status: AUTHORIZED_FOR_IMPLEMENTATION

## Purpose

Create a canonical English-only packet for internal CVF work transfer across
orchestrator, role agents, subagents, reviewers, auditors, and integrators.

The operator asked for a standard spec that any agent can read consistently
when CVF decomposes work into multiple roles or providers. This tranche closes
that gap before continuing Surface 1 web-export fixes.

## Authorization / Decision

Decision: implement MA1 as a governed documentation and protocol tranche.

The packet is a control artifact, not a runtime scheduler. It standardizes how
one CVF agent hands bounded work to another role or provider lane, how that
role reports back, and how integration/audit captures the result.

## Scope / Target / Owner Boundary

Owner surface:

- CVF internal multi-agent / multi-role work-transfer protocol.

In scope:

- English-only canonical transfer packet standard;
- role-lane assignment schema;
- source fidelity and authority gates;
- evidence and receipt requirements;
- risk, stop, and dissent handling;
- acceptance checklist;
- sample use as the control packet for the following Surface 1 i18n/export fix.

Out of scope:

- live subagent runtime implementation;
- automated scheduler;
- provider routing changes;
- MCP protocol changes;
- receipt envelope changes;
- public product claims;
- hosted deployment.

## Non-Goals

MA1 does not try to build autonomous agents, create a runtime job queue,
replace work orders, certify provider independence, or expose a public
non-coder export surface. It only defines the internal transfer packet that
agents use before or during governed work.

## Surface Fidelity Gate

| Field | Value |
| --- | --- |
| Source code path | Not a generated code artifact; canonical reference doc under `docs/reference/` |
| Output artifact | English markdown work-transfer packet copied into work orders or role dispatch packets |
| Audience | CVF-aware agents, role agents, reviewers, auditors, integrators |
| Language layer | Layer 4 Engine Room, English invariant |
| Generation trigger | Orchestrator dispatches role work or a multi-role tranche begins |
| Operator verdict path | Operator requested MA1 before Surface 1 fix |

## Work Plan

1. Create GC-018 baseline and work order for MA1.
2. Publish the canonical English-only transfer packet standard.
3. Record a completion packet and claim boundary.
4. Commit MA1 independently before code work.
5. Use the MA1 packet as the control packet for the Surface 1 i18n/readiness
   and risk-gate correction tranche.

## Work Packages

### MA1-A: Canonical Packet Contract

Deliver a reference document with:

- packet metadata;
- authority and surface fidelity gates;
- source/evidence ledger;
- role roster;
- task allocation table;
- allowed and forbidden actions;
- expected output schema;
- dissent and convergence rules;
- acceptance checklist.

### MA1-B: Governance Closure

Deliver:

- GC-018 baseline;
- work order;
- completion review;
- active session/handoff state update.

## Evidence Plan

Required:

- file existence checks for all MA1 artifacts;
- markdown structural review by role simulation;
- active session state compatibility check.

Live provider/API proof is not required because MA1 is a deterministic internal
documentation/control protocol and does not claim provider governance behavior.

## Acceptance Criteria

- A single canonical English-only packet standard exists.
- The standard can be copied into a work order as a concrete role assignment.
- It explicitly prevents wrong-surface review, authority inversion, and
  unbounded role drift.
- It is used in the next Surface 1 implementation tranche.

## Stop Conditions

Stop if MA1 attempts to claim runtime role isolation, autonomous subagent
scheduling, public readiness, or provider behavior.

## Claim Boundary

MA1 may claim only a canonical English internal work-transfer packet standard.
It does not prove live multi-agent execution, provider independence, MCP
control, hosted readiness, production readiness, or public release readiness.
