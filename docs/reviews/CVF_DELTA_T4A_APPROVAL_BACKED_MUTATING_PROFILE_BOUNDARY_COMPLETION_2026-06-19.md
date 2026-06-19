# CVF Delta-T4A Approval-Backed Mutating Profile Boundary Completion

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_CLOSURE

Date: 2026-06-19

docType: review

Worker / reviewer / closer: Codex, phase-separated single-agent route

Execution base: `22f35116`

Material commit: `PENDING_MATERIAL_COMMIT`

Closure base: `PENDING_POST_MATERIAL_SYNC`

## Purpose

Record implementation and adversarial self-review of the bounded Delta-T4A
approval-backed mutating profile before material commit and closure conversion.

## Scope / Target / Owner Boundary

Accepted target: one new `approval-marker-write` static profile, one T4A
approval policy/evidence module, launcher wiring that keeps T1/T2/T3 admission
before T4A approval and runner invocation, and a fixed workspace-local marker
write at `.cvf/delta/approval-marker-write.json`.

Still forbidden: arbitrary executable/args/env, caller-selected target paths,
shell execution, npm project scripts, EDIT/COMMIT execution, direct IDE/shell/
git/filesystem interception, provider/live calls, secrets/quota, workspace-state
mutation, queues/daemons, public-sync, and readiness claims.

## Reviewer Findings And Repairs

| ID | Finding | Severity | Repair | Result |
| --- | --- | --- | --- | --- |
| R1 | The existing guard engine escalates AI-agent R2 actions, so the first runtime draft could not reach T4A approval. | HIGH | Kept tranche-level risk sensitivity R2 in the work order, but classified the fixed marker profile runtime as R1 so T1 can ALLOW and the new T4A approval evidence remains the mutation gate. | RESOLVED |
| R2 | TypeScript narrowed the fixed marker target literal too aggressively in target safety checks. | LOW | Reordered the path validation and widened the intermediate relative path. | RESOLVED |

No unresolved finding remains inside the bounded Delta-T4A claim.

## Findings / Position

Reviewer position: accept the bounded material for closure conversion. The
runner is unreachable until T1 ALLOW, T2 atomic consumption, T3 durable intent,
and T4A approval evidence succeed. The only mutation is a create-exclusive
marker write at the fixed workspace-local path.

## Risk / Corrective Action

Residual risk: `cvf-governed-exec` remains opt-in and does not intercept direct
IDE, shell, git, or filesystem actions. The T4A approval record is local JSON
evidence under the configured Delta audit directory; it is not a hosted
approval service, queue, or universal policy engine. Future arbitrary commands,
EDIT/COMMIT profiles, external interception, or CVF Web action execution require
separate authorization.

## Source And Runtime Freshness Verification

| Surface | Fresh verification | Result |
| --- | --- | --- |
| Delta-T1 preflight | existing pure handler reused | durable ALLOW receipt required |
| Delta-T2 consumption | existing pure handler/store reused | exact one-time consumption required |
| Delta-T3 execution store | existing create-exclusive intent/final receipt reused | T3 intent precedes approval and runner |
| T4A approval policy | new source and focused tests reviewed | profile, target, action hash, expiry, and optional binding validation |
| Marker write | new source and smoke readback reviewed | fixed create-exclusive workspace-local JSON marker |
| CLI | source reviewed | no arbitrary executable, args, env, shell, EDIT, or COMMIT flag added |

## Acceptance Criteria Review

| ID | Evidence | Result |
| --- | --- | --- |
| AC1 | profile registry exposes exactly one new mutating profile, `approval-marker-write` | PASS |
| AC2 | focused tests prove runner is not called before approval and prior T1/T2/T3 gates remain intact | PASS |
| AC3 | marker write validates and writes only `.cvf/delta/approval-marker-write.json` | PASS |
| AC4 | missing, expired, wrong-target, or wrong-action approval rejects before runner | PASS |
| AC5 | parser still accepts only profile/workspace/cwd/json and rejects arbitrary exec/args | PASS |
| AC6 | approval evidence stores bounded ids, hashes, timestamps, and target fields | PASS |
| AC7 | runner failure finalizes `FAILED` and returns launcher failure | PASS |
| AC8 | known credential patterns remain redacted from returned stdout/stderr | PASS_BOUNDED |
| AC9 | focused tests, full MCP tests, build, and temp-workspace binary smoke pass | PASS |
| AC10 | no provider/live/public/queue/workspace-state/external-interception claim added | PASS |

## Verification Evidence

| Command or check | Result |
| --- | --- |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 22f35116 --head HEAD` | PASS |
| `npx vitest run src/cli/mutating-profile-approval.test.ts src/cli/governed-command-launcher.test.ts --reporter verbose` | PASS, 2 files / 19 tests |
| `npm run test:run` | PASS, 30 files / 617 tests |
| `npm run build` | PASS |
| temp-workspace `node dist/cli/governed-exec.js --profile approval-marker-write --workspace <temp> --json` | PASS, accepted true, `approvalBackedMutationProved=true` |
| smoke marker readback | PASS, fixed target `.cvf/delta/approval-marker-write.json` |
| smoke cleanup | PASS, temporary workspace and audit directory removed |

Provider/live proof: N/A with reason: Delta-T4A proves a local wrapper-owned
mutation boundary and makes no provider or external-service governance claim.

## Closure Diff Gate

| Comparison | Result |
| --- | --- |
| GC-018 to work order | fixed approval-backed marker mutation and claim boundaries preserved |
| Work order to implementation | runtime edits stay in named MCP source/test scope plus this completion/evidence |
| Required manifest to actual material set | MATCH pending material commit |
| Forbidden scope | no dependency, lockfile, Model Gateway, Web, workspace state, queue, hook, public, provider, or credential path changed |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Defect class | `RUNTIME_SIGNAL_GAP` for the new approval-boundary runtime signal |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Current action | first bounded approval-backed mutation added behind wrapper-owned admission |
| Machine-check action | `MACHINE_CHECK_CANDIDATE`: future mutating profiles should declare fixed target, approval evidence source, and no caller path input |
| Runtime/provider/cost lane | `N/A_WITH_REASON`: no provider call, token cost, or live API latency signal |
| Next action | keep arbitrary/EDIT/COMMIT/external interception parked |
| Worker blame | N/A with reason: self-review found and repaired issues before material commit |

## Epistemic Process Block

### Expected Result / Prediction

The wrapper was expected to add exactly one fixed marker-write mutation after
durable T1/T2/T3 and local T4A approval evidence.

### Evidence Comparison

The admission prediction held after the fixed marker profile was classified as
runtime R1 under the current guard engine. Focused tests and binary smoke show
the marker write is target-bound and approval-bound.

### Contradiction Or Gap Disposition

The main contradiction was guard semantics for AI-agent R2. The tranche remains
R2-sensitive as a governed work item, but the actual fixed marker runtime action
is R1 and still requires explicit T4A approval evidence.

### Claim Update

The accepted claim is limited to an opt-in wrapper-owned
`approval-marker-write` profile. No universal or external interception claim is
added.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | Delta-T4A work order | closure conversion pending | PENDING_CLOSURE |
| Completion or reviewer artifact | this file | Codex review and two resolved findings | PASS |
| Roadmap state | N/A with reason: active-session/operator-derived tranche | no roadmap mutation | N/A with reason |
| Registry JSON | BLOCKED with reason: no corpus registry edit authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no new external source consumed | repo-local sources only | N/A with reason |
| System loop interlock | N/A with reason: no queue/scheduler/loop added | no interlock mutation | N/A with reason |
| Session continuity | accepted-material state | pending material commit | PENDING_CLOSURE |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| full admission precedes process | T1 audit, T2 marker, T3 intent, T4A approval before runner | ordering and failure-injection tests | PASS |
| arbitrary execution unavailable | strict profile registry/parser | unknown profile and extra args reject | PASS |
| marker target fixed | no caller target path | source, tests, and smoke readback | PASS |
| approval failure blocks runner | runner not called | missing-policy and missing-approval tests | PASS |
| failure evidence is durable | failed approval/runner finalizes receipt | focused failure tests | PASS |
| execution claim stays bounded | wrapper marker true; interception false | response and marker assertions | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex implementer/reviewer |
| Provider or surface | local provenance workspace |
| Session or invocation | `delta-t4a-material-codex-2026-06-19` |
| Working directory | repository root and MCP package |
| Command or tool surface | PowerShell, apply_patch, Vitest, TypeScript, Node binary, Python governance gates |
| Target paths | exact seven-path material manifest below |
| Allowed scope source | Delta-T4A GC-018 and work order |
| Before status evidence | execution base `22f35116`; clean worktree before edits |
| After status evidence | material pending commit with tests/build/smoke passed |
| Diff evidence | `git diff --name-status`; focused/full tests; build; binary smoke |
| Approval boundary | one fixed approval-backed marker-write profile only |
| Claim boundary | no arbitrary command, EDIT/COMMIT, provider/live, public-sync, queue, daemon, interception, or universal governed coding |
| Agent type | single-agent multi-role Codex material phase |
| Invocation ID | `delta-t4a-approval-backed-mutating-profile-boundary-material-codex-2026-06-19` |
| Expected manifest | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.test.ts`; `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md`; `docs/reviews/evidence/delta-t4a-approval-backed-mutating-profile-boundary-2026-06-19.json` |
| Actual changed set | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.test.ts`; `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md`; `docs/reviews/evidence/delta-t4a-approval-backed-mutating-profile-boundary-2026-06-19.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime component. Public-sync is not authorized.

## Claim Boundary

Completion evidence proves only opt-in wrapper-owned execution of one fixed
approval-backed marker-write profile after durable T1/T2/T3/T4A admission. It
does not make the wrapper mandatory outside its path, execute arbitrary commands,
implement EDIT/COMMIT, intercept external tools, prove provider behavior, or
establish universal governed coding.
