Memory class: GOVERNANCE_BASELINE

# CVF ADR Skill Evolution Loop Runtime Ownership - 2026-05-16

Status: accepted.

## Purpose

Record owner placement for Skill Evolution Loop runtime behavior.

## Scope

Owner package:

- `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/`

## Source

Source bundle:

- `.private_reference/legacy/CVF 16.5/Memento-Skills`

## Baseline

The Skill Governance Engine already owns skill lifecycle concerns. The new loop
should extend that package, not create a parallel root.

## Context

Memento-Skills emphasizes Read -> Execute -> Reflect -> Write. CVF absorbs this
as Read -> Execute -> Reflect -> Proposal -> Verify -> Approve -> Receipt ->
Governed Reinjection. The write step is never autonomous.

## Alternatives

Alternative A: create `EXTENSIONS/CVF_GOVERNED_SKILL_EVOLUTION_LOOP/`.

Disposition: deferred because an existing skill governance owner already exists.

Alternative B: keep it documentation-only.

Disposition: rejected because selected knowledge must become living.

Alternative C: add a bounded contract to the Skill Governance Engine.

Disposition: accepted.

## Decision

Add:

- `evolution_engine/governed.skill.evolution.contract.ts`

## Consequences

CVF gains a tested proposal-only evolution loop while preserving the no
self-write production boundary.

## Evidence

Evidence is recorded in the closure packet.

## Verification

Package checks and focused tests must pass before commit.

## Claim Boundary

This ADR does not authorize autonomous mutation of production skills.
