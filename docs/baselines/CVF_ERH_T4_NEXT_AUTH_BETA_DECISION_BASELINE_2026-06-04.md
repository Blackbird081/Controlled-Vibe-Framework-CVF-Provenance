# CVF ERH-T4 Next-Auth Beta Decision Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-04

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T4_NEXT_AUTH_BETA_DECISION_2026-06-04.md`

## Purpose

Record the ERH-T4 decision for the current `next-auth` beta dependency in the
web package manifest.

## Scope / Target / Owner Boundary

Target:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`

Boundary: decision record only. No dependency migration or runtime auth change
is authorized in this tranche.

## Source / Current Fact

| Source | Evidence | Disposition |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 30 declares `"next-auth": "^5.0.0-beta.30"` | ACCEPT |
| `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | current posture is not production-readiness proof | ACCEPT |

## Decision / Baseline / Proposed Tranche

Decision: accept the `next-auth` beta dependency for the current private
prototype/governed-web scope with an explicit public caveat.

Rationale:

- ERH is not claiming hosted production readiness in this batch.
- Changing auth dependency versions can alter auth/session semantics and needs
  separate implementation/testing authority.
- The public GitHub surface should not hide the beta dependency if it is
  relevant to external-agent assessment.

Required public caveat for ERH-T1B:

`The current web package uses next-auth v5 beta; treat hosted production auth
stability as deferred until a separate dependency migration or acceptance review
is completed.`

## Options Considered

| Option | Decision | Reason |
| --- | --- | --- |
| Accept beta for current bounded scope | ACCEPTED | matches T3 non-production posture |
| Migrate to stable in this batch | REJECTED_FOR_SCOPE | requires runtime/package work and tests |
| Public caveat only | ACCEPTED_AS_PUBLIC_BOUNDARY | informs external reviewers accurately |

## Follow-Up Trigger

Open a separate dependency/auth work order if any future public claim says CVF
web auth is hosted-production ready, enterprise-ready, or stable-dependency
certified.

## Evidence / Verification

| Check | Result |
| --- | --- |
| `rg -n '"next-auth"' EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | source line declares `next-auth` beta dependency |
| T3 dependency release | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` exists |
| Runtime/package modification | N/A with reason: decision baseline only |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Beta auth dependency can be hidden by broad public readiness language | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | public caveat plus separate migration trigger |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision baseline. No public-sync commit or public
artifact path evidence is included.

Next action: ERH-T1B may export only the caveat and follow-up trigger.

## Claim Boundary

This baseline accepts the beta dependency only for current bounded scope. It
does not prove auth security, hosted readiness, production stability, or
dependency migration completion.
