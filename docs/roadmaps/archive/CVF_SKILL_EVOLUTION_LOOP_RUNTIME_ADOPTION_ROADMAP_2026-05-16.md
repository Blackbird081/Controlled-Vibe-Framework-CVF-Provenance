Memory class: ROADMAP

# CVF Skill Evolution Loop Runtime Adoption Roadmap - 2026-05-16

Status: completed.

## Purpose

Move Skill Evolution Loop from `docs-classified` to `runtime-owned`.

## Scope

Implement one deterministic Skill Governance Engine contract for governed skill
evolution proposal, verification, reinjection decision, and receipt.

## Source

Source bundle:

- `.private_reference/legacy/CVF 16.5/Memento-Skills`

## Baseline

CVF had skill governance infrastructure but not this bounded loop as one tested
contract.

## Authorization / Decision

Authorized by operator instruction to complete the CVF 16.5 absorption roadmap
autonomously.

Decision: use the existing Skill Governance Engine package.

## Non-Goals

This roadmap does not deliver:

- autonomous production skill rewrite;
- external skill execution;
- live provider calls;
- new skill registry UI.

## Work Plan

| Step | Action | Status |
|---|---|---|
| 1 | Create GC-018 authorization and ADR | complete |
| 2 | Create source matrix and proof plan | complete |
| 3 | Implement governed skill evolution contract | complete |
| 4 | Add focused tests | complete |
| 5 | Update summary and handoff | complete |
| 6 | Run verification | complete |

## Acceptance Criteria

The tranche is accepted when:

- contract exists in Skill Governance Engine;
- tests cover proposal-only boundary, verification, reinjection path, human
  review, risk lowering, receipts, and determinism;
- package check passes;
- governed file-size and Markdown guards pass;
- full pre-push chain passes before push.

## Evidence

Owner files:

- `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/evolution_engine/governed.skill.evolution.contract.ts`
- `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/tests/governed.skill.evolution.contract.test.ts`

## Verification

Verification recorded in the closure packet:

- Skill Governance Engine `npm run check` PASS;
- focused Skill Evolution Loop Vitest PASS, 1 file / 13 tests;
- full Skill Governance Engine Vitest PASS, 9 files / 102 tests;
- governed file-size guard PASS;
- markdown structural completeness PASS;
- docs governance compatibility PASS.

## Claim Boundary

This roadmap closes proposal-loop governance only. It does not authorize
self-modifying skills.
