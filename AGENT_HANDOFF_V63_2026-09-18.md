# CVF Agent Handoff V63 - ACEL T3B Group 2 Party A Spec Execution Checkpoint

<!-- CVF-GC020-MATERIAL-SHA:START -->
Current material HEAD recorded for this handoff: `47c8dd462`. Group 1 is
`SOURCE_CREATED_LOCAL_VERIFIED`; T3B R2 tooling is `CLOSED_PASS_BOUNDED`; the
next open action is the credential-bound Party A Group 2 spec write.
<!-- CVF-GC020-MATERIAL-SHA:END -->

Memory class: active-handoff

Status: ACTIVE

## Purpose

Carry the independently verified Group 1 closure and route the bounded real
Group 2 ceremony in strict order: Party A spec write, Local verification, then
and only then Approver decision writes.

## Scope / Target / Owner Boundary

Role: Local orchestrator/reviewer. Phase: T3B Party A spec execution checkpoint.
Decision owner: operator for the credential-bound Party A action; Local for
independent source verification and authorization of the later Approver step.

External research is closed for this lane. A shared-workspace worker, if later
dispatched, is `INTERNAL_AGENT`; the operator relays its work order only and
does not become the reviewer.

## Startup Acknowledgment

Startup acknowledged: current mode=`acel_g1_t3b_group2_party_a_spec_execution_checkpoint`;
active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=operator
runs the committed Group 2 spec writer as the verified Party A principal and
returns `SPEC_CREATED_PENDING_LOCAL_VERIFICATION`; parked checkpoint=Approver
execution until Local verification, plus T3C/T3D/T3E and
promotion/admission/live/runtime/public/deployment.

## Current Mode

`acel_g1_t3b_group2_party_a_spec_execution_checkpoint`.

The active program remains restricted to
`agent-capability-engineering-lab__handoff-v2`. Latest closed learning-history
wave remains `LHW24`.

## Active Boundary

Only one real Party A Group 2 spec write is open. Approver execution remains
closed until Local independently verifies that created spec.

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
- Operator created the account with SID
  `S-1-5-21-1644666849-912006174-747199667-1008`; it is enabled, expiring and
  non-admin, but Windows still reports `PasswordRequired=false`.
- The launcher now enforces enabled/password-required/non-admin posture and
  fails closed at material commit `57a948c0f`.
- Operator set the password-required flag; Local verified the exact SID,
  enabled/expiring/non-admin posture and launcher exit 0.
- Paired T3B baseline/work order committed at `97cae8068` after 89/89 checks.
- Independent review found four consolidated defects: principal-readable
  handoff ACLs, per-version event-hash binding, fail-closed supersession
  citation, and packet/evidence-contract coherence.
- The independent review, R1 baseline and R1 work order committed at
  `0f9c5d040` after focused gates and 89/89 pre-commit checks.
- The R1 worker return passed its declared self-tests, but Local independent
  probes proved that its supersession prerequisite required an invalid
  two-active-version state and that the durable event did not bind the
  replacement version/hash. R1 is `REWORK_REQUIRED`; this is a root-contract
  dispatch defect, not a worker-only implementation defect.
- The R1 completion review plus R2 atomic-rotation baseline/work order committed
  at `8ba852366` after focused gates and 89/89 pre-commit checks. R2 owns exactly
  five paths, does not execute either principal, and must not create a real source.
- Local accepted the corrected R2 implementation as `CLOSED_PASS_BOUNDED` at
  `014f64391`: decision-writer self-test 74/74, Python suite 58/58, three
  independent atomic-rotation probes 3/3, worker-return fast gate COMPLIANT,
  and both real Group 2 output paths absent. The worker-return count overclaim
  65/65 was reviewer-corrected to the observed 58/58 before commitment.
- Reviewer corrected the closure-provenance omission at `030bc1e74` by
  tracking the previously frozen spec writer at its already-reviewed SHA-256
  `226b081d20f7e1aaf0c0b672c0dd004ebd53bd0b2350ca87ac38e829c7cb62e6`;
  its hermetic self-test passed 48/48 and created no real Group 2 output.
- Party A launcher was corrected at `47c8dd462` to invoke the verified Group 2
  spec writer automatically after `runas`; operator input is now limited to
  the account password and exact ceremony confirmation phrase.

## T3B Readiness Inputs

The approved principal is `cvf-g1-approver`, a dedicated standard
local account distinct from Parties A/B/C. The exact compact JCS payload and
`freshnessThresholdSeconds=86400` are recorded in
`docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md`.
This identity evidence makes tooling dispatchable only. It is not Group 2
source-establishment or activation proof.

## Next Allowed Move

PROGRAM_ID=AGENT-CAPABILITY-ENGINEERING-LAB-2026-09; NEXT_SOURCE_ID=agent-capability-engineering-lab__handoff-v2; NEXT_ACTION_CLASS=CONTINUE_ACTIVE_PROGRAM; CURRENT_TRANCHE_ACTION=ACEL_G1_T3B_PARTY_A_AUTORUN_READY_AT_47c8dd462; NEXT_STEP=OPERATOR_RUN_PARTY_A_GROUP2_SPEC_AUTORUN_UNDER_VERIFIED_PRINCIPAL; EXPANSION_ALLOWED=false. Double-click `scripts/run_as_cvf_g1_party_a.cmd`, enter the Party A password, then type the exact confirmation phrase `EXECUTE GROUP 2 SPEC WRITE`; the launcher invokes the committed writer and exact principal binding automatically. Stop after `SPEC_CREATED_PENDING_LOCAL_VERIFICATION` and return the output to Local for independent source verification. Do not run the Approver decision writer before Local verification. T3C/T3D/T3E, key promotion, candidate admission, provider/live, runtime, public-sync and deployment remain parked. Thirteen parked paths remain unchanged. Latest closed LHW wave remains LHW24.

## Parked Checkpoints

- Approver Group 2 decision writes until Local verifies the Party A spec;
- T3C observation source, T3D issuer source, and T3E consumer wiring;
- key promotion or candidate admission;
- provider/live work, runtime activation, public sync, deployment or production;
- mutation, staging or commitment of the thirteen parked untracked paths.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: project material commit `47c8dd462` into
the active front door and move only to the Party A Group 2 spec-execution checkpoint.
Protected paths: `AGENT_HANDOFF_V63_2026-09-18.md`;
`CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
`CVF_SESSION/state/entries/nextAllowedMove.json`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
`governance/compat/check_acel_g1_verification_authority_spec.py`;
`governance/compat/test_check_acel_g1_verification_authority_spec.py`;
`governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.
The ACEL checker paths are tracked closure evidence and remain unchanged. The
task-class checker paths are pre-existing parked evidence listed only for guard
changed-set accounting; they are not authorized for mutation, staging, or
commitment by this session-sync change.

Operator authorization: explicit approval of both T3B choices plus standing
Local reviewer/closer and session-transition authority. Rollback boundary:
revert only this continuity projection; preserve the Group 1 source, T3B audit,
decision/launcher, principal-correction and R2 closure commits and all parked
files. This continuity change creates no Group 2 source and authorizes no
Approver action before Local verification, credential handling, promotion,
admission, live/runtime/public or deployment effect.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local session-sync steward |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL G1 T3B Party A spec-execution continuity, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, state generator, governance gates and Git |
| Target paths | active handoff, front door, core/source state and generated state/bootstrap |
| Allowed scope source | explicit operator approval plus standing Local reviewer/closer authority |
| Before status evidence | material HEAD `47c8dd462`; R2 closed, spec writer tracked and Party A autorun launcher ready; thirteen parked paths untracked |
| After status evidence | one Party A spec write is next; Approver remains closed pending Local verification |
| Diff evidence | exact continuity manifest before session-only commit |
| Approval boundary | continuity projection and Local audit routing only |
| Claim boundary | continuity only; no Group 2 source, activation, promotion, admission, live/runtime/public effect |
| Agent type | Local session-sync steward |
| Invocation ID | `acel-g1-t3b-party-a-spec-execution-v63-continuity-20260920` |
| Expected manifest | handoff, front door, core, next-move, generated state and bootstrap |
| Actual changed set | verified before commit |
| Manifest delta | pending final diff reconciliation |
| Deletion or rename disposition | none |

## Claim Boundary

This handoff records continuity and the bounded Party A execution checkpoint only.
It does not establish Group 2, activate a specification, bind a verifier consumer,
promote the Party A key, admit a candidate, or authorize provider/live,
runtime, public-sync, deployment or production behavior.
