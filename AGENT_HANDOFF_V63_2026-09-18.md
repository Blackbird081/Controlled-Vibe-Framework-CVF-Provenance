# CVF Agent Handoff V63 - ACEL T3C Party B Principal Checkpoint

<!-- CVF-GC020-MATERIAL-SHA:START -->
Current material HEAD recorded for this handoff: `9493825e`. Group 1 is
`SOURCE_CREATED_LOCAL_VERIFIED`; Group 2 v1 is
`ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`; Party B is verified and
T3C-C1 AR1 is reviewer-fixed, verified and materially closed; CVF-HRLTP-T1
is independently reviewed and accepted, and its bounded multi-agent routing
observation is recorded without a cost-superiority claim.
The MCP/MUO orchestration discussion is parked for a later tranche at
`docs/reference/external_agent_invocation_control/CVF_AGENT_ORCHESTRATION_PLATFORM_MCP_DISCUSSION.md`;
the external-agent invocation moratorium remains unchanged.
<!-- CVF-GC020-MATERIAL-SHA:END -->

Memory class: active-handoff
Status: ACTIVE

## Purpose

Carry the independently verified Group 1 closure and route the bounded real
Group 2 ceremony in strict order: Party A spec write, Local verification, then
and only then Approver decision writes.

## Scope / Target / Owner Boundary

Role: Local orchestrator/reviewer. Phase: post-CVF-HRLTP-T1 tranche selection.
Decision owner: Local.

External research is closed for this lane. A shared-workspace worker, if later
dispatched, is `INTERNAL_AGENT`; the operator relays its work order only and
does not become the reviewer.

## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_hrltp_t1_closed_next_tranche_selection_checkpoint`;
active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=Local audits
current ACEL state and selects the next source-verified governed tranche; parked
checkpoint=Party B real execution/source creation, T3D/T3E and
promotion/admission/live/runtime/public/deployment.

## Current Mode

`cvf_hrltp_t1_closed_next_tranche_selection_checkpoint`.

The active program remains restricted to `agent-capability-engineering-lab__handoff-v2`.
Latest closed learning-history wave remains `LHW24`.

## Active Boundary

T3B is closed with one Local-verified active v1 specification. Party B is a
verified exact local principal and T3C-C1 hermetic tooling is accepted at
`db78c87df`.
Real observation/source creation and all downstream actions remain closed.

Remote tracking branch: `origin/main`; derive exact remote SHA live when needed.
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
- T3B authority selection, dedicated `cvf-g1-approver` provisioning and
  secret-free launchers were governed through `a907469aa`, `ef29dbc1f`,
  `16a6273dc`, `57a948c0f` and `97cae8068`.
- Independent review exposed four atomic-rotation/root-contract defects; R1
  was rejected and R2 was accepted `CLOSED_PASS_BOUNDED` at `014f64391` with
  decision writer 74/74, Python 58/58 and three independent probes 3/3.
- Closure provenance was corrected at `030bc1e74`; Party A launcher/writer
  privilege handling was corrected at `47c8dd462` and `5121004d4`, with exact
  owner/DACL enforcement and verified atomic rollback.
- Party A successfully created `SPEC_v1.json`; Local independently verified
  the exact fixed-policy bytes, direct hash, closed-record hash, Party A owner
  and three-ACE protected DACL. The spec plus verification receipt committed
  at `89498f172` after reviewer-fast 68/68 and pre-commit 89/89.
- The Approver launcher was bounded to one `APPROVED` append for spec version
  1 and committed at `3a163417e`; it cannot append `ACTIVATED` in this step.
- The operator appended exactly one `APPROVED` event. Local independently
  verified its v1 binding, genesis chain hash, Approver account posture,
  ownership and protected two-ACE DACL. The event plus approval receipt
  committed at `83eccf3e6`; v1 remains inactive with an empty active set.
- The Approver launcher was changed from `APPROVED` to exactly one
  `ACTIVATED` append for spec version 1 and committed at `961b7e17a` after
  89/89 pre-commit checks.
- The operator appended one `ACTIVATED` event. Local independently replayed
  the two-event chain, recomputed both hashes, verified the unique active set
  `{1}` and rechecked owner/DACL. The event plus activation receipt committed
  at `f85cdf68c`; T3B is
  `ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`.
- Local selected the T3C principal-first route at `b73990089`: exact standard
  account `cvf-g1-party-b` must be provisioned and verified before hermetic
  tooling dispatch. Group 3 remains `SOURCE_NOT_CREATED`.
- Operator provisioned `LAM-RUBY\cvf-g1-party-b`, SID ending `-1009`; Local
  verified enabled/password-required/expiring/non-admin/distinct posture.
- Initial T3C-C1 dispatch `c322b7dc5` was rejected for append duplication,
  rollback/race/blank-line defects and manifest overrun. Consolidated R1
  committed at `7ce1f02fd` after 89/89 pre-commit; it keeps four worker paths
  and forbids credentials, Party B execution, real log, staging and commit.
- AR1 baseline/work order committed at `dd76f9e00` after fresh operator authorization: it requires a real peer process, exception-safe mutex lifetime, exact semantic DACL restoration, complete ACE adversaries and final-return SHA-256 binding. R2 remains terminal and AR1 is a new chain.
- Local reviewer-fixer replaced the crashed raw-thread/mutex-only proof with
  the same writer running in a real second `pwsh` process and deterministic
  READY/ATTEMPTING/PARENT_RELEASE/ENTERED/COMPLETE barriers. Exact semantic
  owner/protection/ACE restoration and post-acquire cleanup are proven.
  Evidence: writer 56/56, Python 42/42, checker self-test PASS,
  worker-return fast gate COMPLIANT, reviewer-fast 68/68, pre-commit 89/89,
  and canonical return pre/post SHA-256
  `db8a821d52178835df28a8b9032cd7ec471580d3a6664351ae7300b620b29b0f`.
  Material commit: `db78c87df`; real Group 3 log remains absent.
- CVF-HRLTP-T1 foundation dispatch is committed at `6b078bf8b`. Its paired
  baseline/work order converts the four accepted AR1 defect classes into one
  reusable standard/checker/test/hook tranche. The INTERNAL_AGENT owns exactly
  ten uncommitted paths, must preserve the thirteen parked paths, and returns
  the independent probe as pending for Local execution. Dispatch author fast
  gate passed; pre-dispatch passed 81/83, with only the two known cross-lane
  parked-worktree findings from task routing and three historical probe-less
  returns. The dispatch commit used a documented hook bypass rather than
  misclassifying those parked paths as worker authority.
- CVF-HRLTP-T1 multi-agent routing evidence is recorded at `dd0e9eed` in
  `docs/reviews/evidence/cvf-hrltp-t1-multi-agent-routing-observation-2026-09-22.json`.
  It preserves the four lane allocations, operator-reported raw time string,
  verification results and reviewer-local repair counts. Per-model time,
  token, quota and currency cost remain explicitly unavailable. The sample is
  admissible only as a bounded naturalistic observation; it does not prove
  topology or model cost/quality superiority and is not a P4 auto-enrollment.

## T3B Readiness Inputs

The approved principal is `cvf-g1-approver`, a dedicated standard
local account distinct from Parties A/B/C. The exact compact JCS payload and
`freshnessThresholdSeconds=86400` are recorded in
`docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md`.
This identity evidence makes tooling dispatchable only. It is not Group 2
source-establishment or activation proof.

## Next Allowed Move

PROGRAM_ID=AGENT-CAPABILITY-ENGINEERING-LAB-2026-09; NEXT_SOURCE_ID=agent-capability-engineering-lab__handoff-v2; NEXT_ACTION_CLASS=CONTINUE_ACTIVE_PROGRAM; CURRENT_TRANCHE_ACTION=CVF_HRLTP_T1_REVIEWER_ACCEPTED_AT_e25f6a1; NEXT_STEP=LOCAL_AUDITS_CURRENT_ACEL_PROGRAM_STATE_AND_SELECTS_THE_NEXT_SOURCE_VERIFIED_TRANCHE; EXPANSION_ALLOWED=false. CVF-HRLTP-T1 static governance foundation is accepted after an independent Local probe and bounded reviewer repair. Preserve thirteen parked untracked paths byte-identically. Do not run Party B, create a real Group 3 source, open T3D/T3E, promote a key, evaluate a candidate, call a provider, public-sync or deploy without a fresh governed authority packet. Latest closed LHW wave remains LHW24.

## Parked Checkpoints

- CVF-HRLTP-T1 implementation is released only to the committed no-commit INTERNAL_AGENT worker lane;
- T3C real Party B execution/source creation remains separately parked;
- T3D issuer source and T3E consumer wiring;
- key promotion or candidate admission;
- provider/live work, runtime activation, public sync, deployment or production;
- mutation, staging or commitment of the thirteen parked untracked paths.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: project accepted CVF-HRLTP-T1 completion
`e25f6a1b` into the active front door and open the next-tranche selection checkpoint.
Protected paths: `AGENT_HANDOFF_V63_2026-09-18.md`;
`CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
`CVF_SESSION/state/entries/cvfHrltpT1Closure20260922.json`;
`CVF_SESSION/state/entries/nextAllowedMove.json`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
`governance/compat/check_acel_g1_registry_observation_log.py`;
`governance/compat/test_check_acel_g1_registry_observation_log.py`;
`governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.
The ACEL observation checker paths are uncommitted R1 worker inputs and remain
unstaged by this continuity commit. The
task-class checker paths are pre-existing parked evidence listed only for guard
changed-set accounting; they are not authorized for mutation, staging, or
commitment by this session-sync change.

Operator authorization: standing Local reviewer/closer, worker-dispatch and
session-transition authority. Rollback boundary: revert only this continuity
projection; preserve accepted sources, R1 dispatch, all worker inputs and all
parked files. This change creates no Group 3 source and authorizes no Party B,
credential, promotion, admission, live/runtime/public or deployment effect.

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
| Before status evidence | material HEAD `dd76f9e00`; AR1 baseline/order committed; thirteen parked paths plus four AR1 worker inputs untracked |
| After status evidence | exact committed AR1 order is ready for operator relay to the INTERNAL_AGENT; real source execution remains closed |
| Diff evidence | exact continuity manifest before session-only commit |
| Approval boundary | continuity projection and Local audit routing only |
| Claim boundary | continuity only; no Group 2 source, activation, promotion, admission, live/runtime/public effect |
| Agent type | Local session-sync steward |
| Invocation ID | `acel-g1-t3c-c1-worker-dispatch-v63-continuity-20260921` |
| Expected manifest | handoff, front door, core, next-move, generated state and bootstrap |
| Actual changed set | verified before commit |
| Manifest delta | pending final diff reconciliation |
| Deletion or rename disposition | none |

## Claim Boundary

This handoff records continuity and the bounded T3C-C1 worker checkpoint only.
It does not create an observation, establish Group 3, bind a verifier consumer,
promote a key, admit a candidate, or authorize provider/live, runtime,
public-sync, deployment or production behavior.
