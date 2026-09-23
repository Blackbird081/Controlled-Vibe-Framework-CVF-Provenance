# CVF Agent Handoff V63 - ACEL T3C Party B Principal Checkpoint

<!-- CVF-GC020-MATERIAL-SHA:START -->
Current HEAD recorded for this handoff: `51cb067542aacf2c3085436c8330fcb0a036a159`. Checkpoint-selection material parent anchor for the dedicated continuity synchronization commit.
<!-- CVF-GC020-MATERIAL-SHA:END -->
Memory class: active-handoff
Status: ACTIVE
## Purpose

Carry the independently verified Group 1 closure and route the bounded real
Group 2 ceremony in strict order: Party A spec write, Local verification, then
and only then Approver decision writes.

## Scope / Target / Owner Boundary

Role: Local orchestrator/reviewer. Phase: post-audit prepare-only operator selection.
Decision owner: Local.

External research is closed for this lane. The selected shared-workspace
worker is `INTERNAL_AGENT`; the operator relays its work order only and
does not become the reviewer.

## Startup Acknowledgment

Startup acknowledged: current mode=`acel_g1_group4_actual_token_checkpoint_retained_closed_prepare_only_selection_next`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=operator selection of one bounded Local prepare-only packet or retention of the closed checkpoint; parked checkpoint=HRLTP-T2 implementation, actual Party B/C execution, passwords, Group 4 source creation, T3E, provider/live/runtime/public/deployment.

## Current Mode
`acel_g1_group4_actual_token_checkpoint_retained_closed_prepare_only_selection_next`.
The active program remains restricted to `agent-capability-engineering-lab__handoff-v2`.
Latest closed learning-history wave remains `LHW24`.

## Active Boundary

T3B is closed with one Local-verified active v1 specification. Party B is a
verified exact local principal and T3C-C1 hermetic tooling is accepted at
`db78c87df`.
T3C-C2 is closed `SOURCE_CREATED_LOCAL_VERIFIED`, and Party C is Local verified. T3D-C1 tooling is accepted at `9ed844c2a` with no source created. T3D-C0-R1 is closed at `2fffa1ef7`; its shared-parent route remains conditional on actual Windows proof. Local architecture selection `8caacc64c`, static proof packet `c395fd1aa` and source gap audit `e79910b5c` led to C1-R2. The correction is accepted at `988491791` for hermetic tooling only. Foundation T1 is closed at `c82f81d49`. The readiness audit at `a765880e4` confirmed the runner gap. The T3D-C3 bounded runner dispatch is committed at `4b68fa465`; its exact four-path material result is committed at `a1203c1ee` and independently accepted bounded at `88137e9a2`. The Local checkpoint-selection audit at `51cb06754` retains the operator checkpoint closed because no reviewed run-specific payload, root, prestate ledger or command packet exists. The thirteen rejected T2/T2A/T2B paths remain archived. HRLTP-T2 is dispatched at `19466bfdc` but paused.

Remote tracking branch: `origin/main`; derive exact remote SHA live when needed.
External agent memory files: non-canonical convenience only.

## Latest Work / Changes

- Group 1 source is `SOURCE_CREATED_LOCAL_VERIFIED` at material commit
  `58281c2c6`; registry snapshot and genesis lifecycle receipt passed the
  canonical source checker and a separate canonical-hash recomputation.
- keyId: `partya-44853ea9a690452c`.
- rowHashHex: `4e94882407c73ab779ead5c2b05d6f67041ad5e9f138ef034e7c152dbe2229f9`.
- entryHashHex: `dbda6b1cc20b77186f5f1c1896f60dc87cff8aab7ab35ed225ed417d06e19fae`.
- publicKeySha256Hex: `5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01`.
- Local verification record: `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md`.
- Candidate evaluation remains `UNVERIFIED`; key promotion is not authorized. T2B rejection remains controlling. T2C through T2H remain contract/design
  evidence and do not establish Groups 2-4 or consumer wiring.
- The thirteen rejected G1 T2 evidence paths are archived with exact hashes at
  `333d687c6` and are not active-path authority.
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
- T3D-C0 closed `CLOSED_PASS_BOUNDED` at `e14722e17`; independent review passed all four repaired T2F contract joins and pre-commit passed 90/90. A post-commit range run rejected the mixed material/current-authority projection because exact-hash projection and range separation conflict; no range PASS is claimed, and this remains a governance-learning input.
- T3D-C1 Group 4 tooling is accepted `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`
  at `9ed844c2a`. Independent GPT-6 Astra review closed the final publication-
  ownership and successor-signal findings; Python 82/82, checker 9/9, Party C
  53/53, Party B 51/51, worker-return fast gate and reviewer-fast 69/69 passed.
  The material hook passed 90/90. Thirteen parked paths remain byte-identical,
  and both real Group 4 source paths remain absent.
- Local audited T3D-C2 readiness and found three unresolved operational joins:
  the shared parent/reservation security model, fresh operational input versus
  hermetic vector identity, and a Party B issuer-registry observation route.
  The contract-only C0-R1 repair packet committed at `622bc4b0f` after its
  isolated exact-manifest Git hook passed 90/90. It owns exactly the existing
  T2F contract plus one worker return, uses `WORKER_MUST_NOT_COMMIT`, and does
  not authorize scripts, checkers, accounts, ACL mutation, credentials, source
  creation or T3E.
- T3D-C0-R1 closed `CLOSED_PASS_BOUNDED` at `2fffa1ef7`; Local closed five
  findings and a distinct read-only reviewer returned `PASS_INDEPENDENT_PROBE`.
  Fast/reviewer-fast 69/69/full-hook 90/90 passed; lossless extraction met
  GC-023 without an exception. `STOP_REASSESS_ARCHITECTURE`; no C1-R2 successor.
- T3D-C3 dispatch `4b68fa465`, material `a1203c1ee` and closure `88137e9a2`
  preserve exact four-path tooling and `CLOSED_PASS_BOUNDED`. Claude's distinct
  probe passed stable hashes, 22/22 TestPolicy rows, fail-closed finalization,
  tamper rejection, real child-process evidence and exact cleanup. Tooling is
  accepted; Party B/C ACL behavior remains unproven.
- Checkpoint selection `51cb06754` reconciled all seven gates and retains
  `CHECKPOINT_RETAINED_CLOSED_EXECUTION_PACKET_NOT_MATERIALIZED`: no fresh
  payload, root, prestate ledger or command packet exists. Seven prior input
  directories remain untouched; wildcard cleanup is prohibited.

## T3B Readiness Inputs

The approved principal is dedicated standard local account `cvf-g1-approver`,
distinct from Parties A/B/C; its exact JCS policy is recorded in the T3B
principal-policy decision. This identity evidence is not source/activation proof.

## Next Allowed Move

PROGRAM_ID=AGENT-CAPABILITY-ENGINEERING-LAB-2026-09; NEXT_SOURCE_ID=agent-capability-engineering-lab__handoff-v2; NEXT_ACTION_CLASS=CONTINUE_ACTIVE_PROGRAM; CURRENT_TRANCHE_ACTION=G1_T3D_C3_ACTUAL_TOKEN_CHECKPOINT_RETAINED_CLOSED_AT_51CB06754; CURRENT_TRANCHE_DISPOSITION=CHECKPOINT_RETAINED_CLOSED_EXECUTION_PACKET_NOT_MATERIALIZED; NEXT_STEP=OPERATOR_SELECT_BOUNDED_LOCAL_PREPARE_ONLY_PACKET_OR_RETAIN_CLOSED; EXPANSION_ALLOWED=false. The Local audit found accepted tooling and principals but no reviewed run-specific payload, disposable root, clean-prestate ledger or exact command packet. If the operator chooses to proceed, first identify one fresh nonempty operational registry payload and authorize only Local coordinator -PrepareProof against one exact absent %TEMP% root; do not launch Party B/C, request or record passwords, or treat preparation as actual-token proof. Review the generated manifest, 22 envelopes, command packet, containment and cleanup binding before a separate execution-opening decision. Preserve the seven observed prior input directories without wildcard cleanup or inference. HRLTP-T2 stays paused; Group 4 source, T3E, provider/live/runtime/public-sync/deployment remain parked. Latest closed LHW wave remains LHW24.

## Parked Checkpoints

- autorun lane-binding R1 is closed at `ee81deeeb`; HRLTP-T2 remains paused for Local no-subagent route reassessment;
- T3C-C2 is closed and Local verified at `820aae3ec`;
- T3D-C1 hermetic tooling is accepted at `9ed844c2a`; T3D-C0-R1 is closed at
  `2fffa1ef7`, while C1-R2 tooling correction is accepted at `988491791`;
  T3D-C3 runner is accepted bounded at `88137e9a2`; checkpoint selection at
  `51cb06754` retains Party B/C execution closed pending a separately selected
  Local prepare-only packet; source creation and T3E remain parked;
- key promotion or candidate admission;
- provider/live work, runtime activation, public sync, deployment or production;
- promotion or restoration of the thirteen rejected archived paths without fresh Local review.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: project checkpoint-selection material SHA `51cb06754` into exact active continuity sources and generated views; route only to operator selection of a Local prepare-only packet or continued closure; preserve HRLTP-T2 as paused and keep actual principal execution/source/T3E parked pending separate authorization.
Protected paths:

- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/acelG1T3dC3ActualTokenCheckpointSelection20260923.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: explicit operator direction to continue and standing
Local reviewer/closer session-transition authority. Rollback boundary: revert
only this continuity projection; preserve material commit `a1203c1ee`, closure
commit `88137e9a2`, checkpoint-selection commit `51cb06754`, the readiness audit
and prior accepted sources.
This change creates no Group 4 source and authorizes no alternate-
principal execution, credential, second observation, promotion, admission,
live/runtime/public or deployment effect.
## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local session-sync steward |
| Provider or surface | private CVF workspace |
| Session or invocation | Group 4 actual-token checkpoint-selection continuity, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, state generator, governance gates and Git |
| Target paths | active handoff, front door, core/source state and generated state/bootstrap |
| Allowed scope source | explicit operator approval plus standing Local reviewer/closer and session-transition authority |
| Before status evidence | checkpoint-selection material HEAD `51cb06754`; audit hook passed 90/90 |
| After status evidence | operator checkpoint is explicitly retained closed; only prepare-only operator selection is next |
| Diff evidence | exact continuity manifest before session-only commit |
| Approval boundary | continuity projection and prepare-only operator-selection routing only |
| Claim boundary | continuity only; bounded tooling acceptance is recorded, but no actual-token proof, ACEL/source action, promotion, admission, live/runtime/public effect is claimed |
| Agent type | Local session-sync steward |
| Invocation ID | `cvf-acel-g1-t3d-c3-checkpoint-selection-v63-continuity-20260923` |
| Expected manifest | handoff, front door, core, next-move, generated state and bootstrap |
| Actual changed set | verified before commit |
| Manifest delta | exact source manifest plus two generated projections |
| Deletion or rename disposition | none |

## Claim Boundary

This handoff records continuity for the bounded Group 4 readiness decision and
routes only Local authoring/implementation with current-token hermetic tests. It
does not claim actual-token proof, create a Group 4 source, perform a T3E lookup, bind a
verifier consumer, promote a key, admit a candidate, or authorize provider/live,
runtime, public-sync, deployment or production behavior.
