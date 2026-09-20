# CVF Agent Handoff V63 - ACEL T3B Approver Provisioning Checkpoint

<!-- CVF-GC020-MATERIAL-SHA:START -->
Current material HEAD recorded for this handoff: `16a6273dc`. Group 1 is
`SOURCE_CREATED_LOCAL_VERIFIED`; the T3B principal and exact v1 policy are
operator-approved, and control is at the approver-account provisioning checkpoint.
<!-- CVF-GC020-MATERIAL-SHA:END -->

Memory class: active-handoff

Status: ACTIVE

## Purpose

Carry the independently verified ACEL G1 T3A-C2 Group 1 source closure and
route the one-time T3B approver-account provisioning and Local verification.

## Scope / Target / Owner Boundary

Role: Local orchestrator/reviewer. Phase: T3B approver-account provisioning.
Decision owner: operator for one-time secret entry/account creation; Local for
identity and least-privilege verification and later work-order/review routing.

External research is closed for this lane. A shared-workspace worker, if later
dispatched, is `INTERNAL_AGENT`; the operator relays its work order only and
does not become the reviewer.

## Startup Acknowledgment

Startup acknowledged: current mode=`acel_g1_t3b_activation_approver_account_provisioning_checkpoint`;
active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=operator
creates the approved standard local approver account, then Local verifies it;
parked checkpoint=T3B dispatch/source creation plus T3C/T3D/T3E,
promotion/admission/live/runtime/public/deployment.

## Current Mode

`acel_g1_t3b_activation_approver_account_provisioning_checkpoint`.

The active program remains restricted to
`agent-capability-engineering-lab__handoff-v2`. Latest closed learning-history
wave remains `LHW24`.

## Active Boundary

Only approver-account provisioning and Local verification are open. T3B work
order dispatch and actual source creation remain closed.

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
- Operator approved both proposed choices; the governed decision and two
  secret-free `runas` launchers committed at `ef29dbc1f` after 89/89 checks.
- Local corrected the 26-character, non-representable Windows username to the
  exact 15-character `cvf-g1-approver` at `16a6273dc`, before provisioning.

## T3B Readiness Inputs

The approved principal is `cvf-g1-approver`, a dedicated standard
local account distinct from Parties A/B/C. The exact compact JCS payload and
`freshnessThresholdSeconds=86400` are recorded in
`docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md`.
The account does not yet exist, so the decision is not source-establishment
proof and does not make T3B dispatchable.

## Next Allowed Move

PROGRAM_ID=AGENT-CAPABILITY-ENGINEERING-LAB-2026-09; NEXT_SOURCE_ID=agent-capability-engineering-lab__handoff-v2; NEXT_ACTION_CLASS=CONTINUE_ACTIVE_PROGRAM; CURRENT_TRANCHE_ACTION=ACEL_G1_T3B_WINDOWS_PRINCIPAL_CORRECTED_AT_16a6273dc; NEXT_STEP=OPERATOR_CREATE_CVF_G1_APPROVER_ACCOUNT_WITH_PASSWORD_THEN_LOCAL_VERIFY; EXPANSION_ALLOWED=false. Exact standard local principal is cvf-g1-approver; the prior 26-character proposal was corrected before provisioning because it exceeded the Windows local SAM-name limit. Exact compact v1 policy with freshnessThresholdSeconds 86400 remains approved. No T3B work order or source creation opens until Local verifies the account's exact name, SID, enabled/password-required posture and non-administrator membership. T3C, T3D, T3E, key promotion, candidate admission, provider/live, runtime, public-sync and deployment remain parked. Thirteen parked paths remain unchanged. Latest closed LHW wave remains LHW24.

## Parked Checkpoints

- actual T3B source creation or activation;
- T3C observation source, T3D issuer source, and T3E consumer wiring;
- key promotion or candidate admission;
- provider/live work, runtime activation, public sync, deployment or production;
- mutation, staging or commitment of the thirteen parked untracked paths.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: project material commit `16a6273dc` into
the active front door and move only to the approver-account provisioning checkpoint.
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

Operator authorization: explicit approval of both T3B choices plus standing
Local reviewer/closer and session-transition authority. Rollback boundary:
revert only this continuity projection; preserve the Group 1 source, T3B audit,
decision/launcher and principal-correction commits and all parked files. No T3B source, credential, activation,
promotion, admission, live/runtime/public or deployment effect is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local session-sync steward |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL G1 T3B approver-provisioning continuity, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, state generator, governance gates and Git |
| Target paths | active handoff, front door, core/source state and generated state/bootstrap |
| Allowed scope source | explicit operator approval plus standing Local reviewer/closer authority |
| Before status evidence | material HEAD `16a6273dc`; compatible principal/policy approved; launchers committed; thirteen parked paths untracked |
| After status evidence | approver account creation and Local verification are next; implementation remains closed |
| Diff evidence | exact continuity manifest before session-only commit |
| Approval boundary | continuity projection and Local audit routing only |
| Claim boundary | no Group 2 source, activation, promotion, admission, live/runtime/public effect |
| Agent type | Local session-sync steward |
| Invocation ID | `acel-g1-t3b-approver-provisioning-v63-continuity-20260920` |
| Expected manifest | handoff, front door, core, next-move, generated state and bootstrap |
| Actual changed set | verified before commit |
| Manifest delta | pending final diff reconciliation |
| Deletion or rename disposition | none |

## Claim Boundary

This handoff records continuity and the bounded provisioning checkpoint only.
It does not establish Group 2, activate a specification, bind a verifier consumer,
promote the Party A key, admit a candidate, or authorize provider/live,
runtime, public-sync, deployment or production behavior.
