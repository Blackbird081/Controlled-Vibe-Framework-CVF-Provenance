# CVF Governance Worker-Return Review Package

Memory class: POINTER_RECORD

Status: APPROVED

docType: assf_package_front_door

## Purpose

This front door identifies the approved CVF-owned reviewer skill. The body is
`SKILL.md`; provenance and lifecycle declarations are in `skill.source.json`.

## Scope / Applies-To

Local review of internal CVF worker returns. The package is APPROVED after Local UAT and reviewer certification.
The existing receipt-backed loader may read it on explicit selection; this
does not yet claim ACTIVE production execution. Reviewer authority comes from the current work order
and CVF standards, not from this package.

## Owner Surface

`docs/reference/agent_system_skills/registry/entries/cvf-governance-worker-return-review.json`
owns the metadata state. The package proposal review is
`docs/reviews/CVF_NCR_REVIEW_SKILL_PROPOSAL_2026-09-27.md`.

## Claim Boundary

This file is a package front door only. UAT and certification are recorded separately in the NCR-SRA1 UAT
review. This front door is not invocation, host installation, provider proof, public export, or production
readiness evidence.
