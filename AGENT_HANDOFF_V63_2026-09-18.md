# CVF Agent Handoff V63 - ACEL Group 1 Verified, T3B Readiness Next

<!-- CVF-GC020-MATERIAL-SHA:START -->
Current material HEAD recorded for this handoff: `a907469aa`. Group 1 is
`SOURCE_CREATED_LOCAL_VERIFIED`; T3B readiness is route-selected and control
is at one consolidated operator principal/policy checkpoint.
<!-- CVF-GC020-MATERIAL-SHA:END -->

Memory class: active-handoff

Status: ACTIVE

## Purpose

Carry the independently verified ACEL G1 T3A-C2 Group 1 source closure and
route the next Local-only T3B readiness decision.

## Scope / Target / Owner Boundary

Role: Local orchestrator/reviewer. Phase: T3B readiness audit and route
selection. Decision owner: Local for technical readiness and route selection;
operator for the concrete activation-approver principal, first specification
version content, and fresh authorization for any actual T3B creation.

External research is closed for this lane. A shared-workspace worker, if later
dispatched, is `INTERNAL_AGENT`; the operator relays its work order only and
does not become the reviewer.

## Startup Acknowledgment

Startup acknowledged: current mode=`acel_g1_t3b_operator_principal_and_policy_checkpoint`;
active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=operator
approves or modifies the recommended dedicated approver principal and exact v1
policy bytes; parked checkpoint=work-order dispatch and actual T3B creation,
plus T3C/T3D/T3E, promotion/admission/live/runtime/public/deployment.

## Current Mode

`acel_g1_t3b_operator_principal_and_policy_checkpoint`.

The active program remains restricted to
`agent-capability-engineering-lab__handoff-v2`. Latest closed learning-history
wave remains `LHW24`.

## Active Boundary

Only Local T3B readiness analysis and route selection are open. Actual source
creation remains closed.

Remote tracking branch: `origin/main`

Exact remote SHA must be derived live from git when needed.

External agent memory files: non-canonical convenience only.

## Latest Work / Changes

- Group 1 source is `SOURCE_CREATED_LOCAL_VERIFIED` at material commit
  `58281c2c6`.
- Registry snapshot and genesis lifecycle receipt passed the canonical source
  checker and a separate canonical-hash recomputation.
- keyId: `partya-44853ea9a690452c`.
- rowHashHex: `4e94882407c73ab779ead5c2b05d6f67041ad5e9f138ef034e7c152dbe2229f9`.
- entryHashHex: `dbda6b1cc20b77186f5f1c1896f60dc87cff8aab7ab35ed225ed417d06e19fae`.
- publicKeySha256Hex:
  `5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01`.
- Local verification record:
  `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md`.
- Candidate evaluation remains `UNVERIFIED`; key promotion is not authorized.
- T2B rejection remains controlling. T2C through T2H remain contract/design
  evidence and do not establish Groups 2-4 or consumer wiring.
- Thirteen pre-existing untracked G1 evidence paths remain byte-preserved,
  uncommitted, and outside this lane.
- T3B route-selection audit committed at `a907469aa`; it found the outer
  Group 2 hash/chain contract ready but the decoded policy schema previously
  unspecified, and proposed exact compact v1 JSON plus a dedicated principal.

## T3B Readiness Inputs

The accepted T2F contract defines T3B as Group 2 specification-document plus
activation-decision-file implementation. Its operator checkpoint requires:

1. a concrete activation-approver principal distinct from Parties A/B/C; and
2. the exact first specification version content.

The role appointment exists only as a bounded governance identity. It is not a
concrete OS/service principal, credential, specification, activation decision,
or source-establishment proof. Local completed the route audit and proposed
exact values, but cannot approve operator-owned identity and policy choices.

## Next Allowed Move

PROGRAM_ID=AGENT-CAPABILITY-ENGINEERING-LAB-2026-09; NEXT_SOURCE_ID=agent-capability-engineering-lab__handoff-v2; NEXT_ACTION_CLASS=CONTINUE_ACTIVE_PROGRAM; CURRENT_TRANCHE_ACTION=ACEL_G1_T3B_READINESS_ROUTE_SELECTED_AT_a907469aa; NEXT_STEP=OPERATOR_DECIDE_DEDICATED_ACTIVATION_APPROVER_PRINCIPAL_AND_EXACT_V1_POLICY_BYTES; EXPANSION_ALLOWED=false. Recommended principal is cvf-g1-activation-approver and recommended freshnessThresholdSeconds is 86400 within the exact compact policy payload recorded by the T3B readiness audit. No work order or actual T3B source creation opens until the operator approves or modifies both choices. T3C, T3D, T3E, key promotion, candidate admission, provider/live, runtime, public-sync and deployment remain parked. Thirteen parked paths remain unchanged. Latest closed LHW wave remains LHW24.

## Parked Checkpoints

- actual T3B source creation or activation;
- T3C observation source, T3D issuer source, and T3E consumer wiring;
- key promotion or candidate admission;
- provider/live work, runtime activation, public sync, deployment or production;
- mutation, staging or commitment of the thirteen parked untracked paths.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: project material commit `a907469aa` into
the active front door and move only to the consolidated T3B operator checkpoint.
Protected paths: `AGENT_HANDOFF_V63_2026-09-18.md`;
`CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
`CVF_SESSION/state/entries/nextAllowedMove.json`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
`governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.
The final two paths are pre-existing untracked parked evidence, listed only for
guard changed-set accounting; they remain read-only and are not authorized for
mutation, staging, or commitment.

Operator authorization: standing Local reviewer/closer and session-transition
authority after the Local T3B readiness decision. Rollback boundary: revert
only this continuity projection; preserve the Group 1 source and T3B route
audit commits and all parked files. No T3B source, credential, activation,
promotion, admission, live/runtime/public or deployment effect is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local session-sync steward |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL G1 T3A-C2 verified-source continuity, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, state generator, governance gates and Git |
| Target paths | active handoff, front door, core/source state and generated state/bootstrap |
| Allowed scope source | standing Local reviewer/closer authority after operator Party A execution |
| Before status evidence | material HEAD `58281c2c6`; Group 1 independently verified; thirteen parked paths untracked |
| After status evidence | T3B readiness audit/route selection is next; implementation remains closed |
| Diff evidence | exact continuity manifest before session-only commit |
| Approval boundary | continuity projection and Local audit routing only |
| Claim boundary | no Group 2 source, activation, promotion, admission, live/runtime/public effect |
| Agent type | Local session-sync steward |
| Invocation ID | `acel-g1-t3a-c2-verified-source-v63-continuity-20260920` |
| Expected manifest | handoff, front door, core, next-move, generated state and bootstrap |
| Actual changed set | verified before commit |
| Manifest delta | pending final diff reconciliation |
| Deletion or rename disposition | none |

## Claim Boundary

This handoff records continuity and the next bounded Local decision only. It
does not establish Group 2, activate a specification, bind a verifier consumer,
promote the Party A key, admit a candidate, or authorize provider/live,
runtime, public-sync, deployment or production behavior.
