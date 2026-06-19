# CVF Delta-T3 Governed Command Launcher Completion

Memory class: FULL_RECORD

Status: ACCEPTED_MATERIAL_PENDING_CLOSURE

Date: 2026-06-19

docType: review

Worker / reviewer / closer: Codex, phase-separated single-agent route

Execution base: `aae39481`

## Purpose

Record implementation and adversarial self-review of the bounded Delta-T3
`cvf-governed-exec` launcher before accepted-material commit and closure
conversion.

## Scope / Target / Owner Boundary

Accepted target: one package binary, a two-profile Git read-only registry, an
injected direct-process runner, T1/T2/T3 admission sequencing, a durable
execution intent/final receipt, strict workspace real-path containment, bounded
known-pattern-redacted output, and deterministic tests.

Still forbidden: arbitrary executable/args/env, shell/interpreter execution,
npm project scripts, mutating command profiles, EDIT/COMMIT execution, direct
IDE/shell/git/filesystem interception, provider/live calls, secrets/quota,
workspace-state mutation, queues/daemons, public-sync, and readiness claims.

## Reviewer Findings And Repairs

| ID | Finding | Severity | Repair | Result |
| --- | --- | --- | --- | --- |
| R1 | Execution receipt finalization truncated the file but wrote from the post-read offset, leaving NUL padding. | MEDIUM | Replaced offset-dependent `writeFile` with positional write at offset zero; added finalize/readback/re-finalize regression proof. | RESOLVED |
| R2 | Dispatched npm test/build/check profiles were syntactically static but semantically execute project-defined scripts, so they cannot support a non-destructive claim. | HIGH | Removed all npm profiles from shipped runtime; retained only hardened `git-status` and `git-diff-check`; closure must mark npm rows rejected from T3. | RESOLVED_BY_SCOPE_NARROWING |

No unresolved finding remains inside the bounded two-profile T3 claim.

## Findings / Position

Reviewer position: accept the bounded Delta-T3 material. The wrapper-owned
runner is unreachable until T1 durable ALLOW, T2 atomic consumption, and T3
create-exclusive intent persistence succeed. The execution receipt is
finalized after the child process returns and never stores stdout or stderr.

## Risk / Corrective Action

Residual risk: direct commands outside `cvf-governed-exec` remain bypassable;
Git behavior still depends on the installed Git binary and repository state;
known-pattern redaction is not a proof that arbitrary output contains no secret.
The launcher therefore exposes only two bounded Git inspection profiles and
makes no universal interception or raw-output secrecy claim.

Any mutating profile, npm project script, EDIT/COMMIT owner, arbitrary command,
or IDE/shell proxy requires fresh operator authorization, GC-018, source
verification, and a stronger approval/output policy.

## Source And Runtime Freshness Verification

| Surface | Fresh verification | Result |
| --- | --- | --- |
| Delta-T1 preflight | existing pure handler reused | durable ALLOW receipt required |
| Delta-T2 consumption | existing pure handler/store reused | exact one-time consumption required |
| T3 receipt store | new source and temp readback reviewed | create-exclusive intent; positional synced finalization |
| Profile registry | new source reviewed | only hardened `git-status` and `git-diff-check` |
| Direct runner | new source reviewed | exact executable/args, `shell:false`, no caller env, bounded capture |
| Workspace boundary | real-path source/tests reviewed | lexical and symlink escape rejected |
| Package binary | built output inspected | shebang preserved; strict parser |

## Acceptance Criteria Review

| ID | Evidence | Result |
| --- | --- | --- |
| AC1 | additive `cvf-governed-exec` bin; T1/T2 source untouched | PASS |
| AC2 | negative tests prove runner is not called after T1, T2, or T3 failure | PASS |
| AC3 | unknown profile/extra CLI args rejected; only two Git read-only profiles retained | PASS_BOUNDED |
| AC4 | direct runner uses exact args, `shell:false`, detached false, bounded capture | PASS |
| AC5 | lexical and symlink real-path escape tests pass | PASS |
| AC6 | execution receipt omits action, cwd, executable, stdout, and stderr | PASS |
| AC7 | non-zero runner result finalizes `FAILED` and returns launcher failure | PASS |
| AC8 | known API-key/password patterns are redacted from returned output | PASS_BOUNDED |
| AC9 | focused 15 tests, full 610 tests, build, shebang, and real binary smoke pass | PASS |
| AC10 | no mutating/provider/public/queue/workspace/interception work added | PASS |

## Verification Evidence

| Command or check | Result |
| --- | --- |
| `npx vitest run src/cli/governed-command-launcher.test.ts src/persistence/json-governed-execution.store.test.ts --reporter verbose` | PASS, 2 files / 15 tests |
| `npm run test:run` | PASS, 29 files / 610 tests |
| `npm run build` | PASS |
| built `dist/cli/governed-exec.js` first line | PASS, `#!/usr/bin/env node` |
| real local `git-status` profile smoke | PASS, exit 0; T1/T2/T3 receipt chain completed |
| smoke receipt readback | PASS, execution receipt `COMPLETED`, output absent from receipt |
| smoke cleanup | PASS, temporary workspace receipt directory removed |
| `git diff --check` | PASS |
| pre-dispatch autorun and dispatch steward | PASS before dispatch commit `aafcdfda` |
| pre-implementation autorun and implementation steward | PASS from dispatch-sync commit `aae39481` |

Provider/live proof: N/A with reason: Delta-T3 proves a local child-process
boundary and makes no provider or external-service governance claim.

## Closure Diff Gate

| Comparison | Result |
| --- | --- |
| GC-018 to work order | durable admission, static registry, direct runner, receipt, and claim boundaries preserved |
| Work order to implementation | npm profiles narrowed out after R2; all runtime edits stay in six named package paths |
| Required manifest to actual material set | MATCH including this completion and evidence JSON |
| Forbidden scope | no T1/T2 mutation, dependency, lockfile, Model Gateway, Web, workspace state, queue, hook, public, or provider path |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Defect class | `RUNTIME_SIGNAL_GAP` plus `CLAIM_BOUNDARY_OVERREACH` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Current action | wrapper-owned process admission and durable result evidence added |
| Machine-check action | `MACHINE_CHECK_CANDIDATE`: future execution profiles must declare whether command semantics are static or delegated to project configuration |
| Runtime/provider/cost lane | `N/A_WITH_REASON`: no provider call, token cost, or live API latency signal |
| Next action | keep mutating/npm/arbitrary/EDIT/COMMIT and external interception parked |
| Reviewer repair learning | file-handle writes after reads require explicit offsets; static CLI tokens do not imply static command semantics |
| Worker blame | N/A with reason: phase-separated adversarial self-review found and repaired both defects before acceptance |

## Epistemic Process Block

### Expected Result / Prediction

The wrapper was expected to execute only after three durable admission stages,
persist a bounded result receipt, and expose no arbitrary process surface.

### Evidence Comparison

The admission and execution prediction held. Temp readback found one file-offset
bug, and semantic review contradicted the non-destructive classification of npm
profiles. Both were repaired before acceptance.

### Contradiction Or Gap Disposition

The persistence contradiction is resolved by positional write. The npm-profile
contradiction is resolved by removing those profiles, not by weakening the
claim. Direct-shell bypass remains explicitly outside T3.

### Claim Update

The accepted claim is narrowed to wrapper-owned execution of two hardened Git
inspection profiles after durable T1/T2/T3 admission. No broader execution or
interception claim is added.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | Delta-T3 work order | accepted material; closure conversion follows commit evidence | N/A with reason |
| Completion or reviewer artifact | this file | Codex review and two resolved findings | PASS |
| Roadmap state | N/A with reason: active-session/operator-derived tranche | no roadmap mutation | N/A with reason |
| Registry JSON | BLOCKED with reason: no corpus registry edit authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no new external source consumed | repo-local sources only | N/A with reason |
| System loop interlock | N/A with reason: no queue/scheduler/loop added | no interlock mutation | N/A with reason |
| Session continuity | N/A with reason: material batch only | separate post-material session sync | N/A with reason |

## Execution Admission Assertion Matrix

| Assertion | Required observation | Observed result | Status |
| --- | --- | --- | --- |
| full admission precedes process | T1 audit, T2 marker, T3 intent before runner | ordering and failure-injection tests | PASS |
| arbitrary execution unavailable | strict profile registry/parser | unknown profile and extra args reject | PASS |
| cwd stays in workspace | real-path containment | lexical and symlink tests | PASS |
| failure evidence is durable | failed runner finalizes receipt | focused failure test | PASS |
| execution receipt is secret-safe | no output/action/path fields | raw JSON readback | PASS |
| execution claim stays bounded | wrapper process true; interception false | response and receipt assertions | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex implementer/reviewer |
| Provider or surface | local provenance workspace |
| Session or invocation | `delta-t3-governed-command-launcher-material-2026-06-19` |
| Working directory | repository root and MCP package |
| Command or tool surface | PowerShell, apply_patch, Vitest, TypeScript, Node binary, Python governance gates |
| Target paths | exact eight-path material manifest below |
| Allowed scope source | Delta-T3 GC-018 and work order |
| Before status evidence | clean implementation base `aae39481` |
| After status evidence | focused/full tests, build, receipt readback, and real bounded smoke pass; two findings resolved |
| Diff evidence | `git diff --name-status`; `git diff --check`; focused/full tests; binary smoke; reviewer-fast |
| Approval boundary | static-profile non-destructive RUN launcher only |
| Claim boundary | no arbitrary/mutating command, EDIT/COMMIT, external interception, provider/live, public-sync, or universal governed coding |
| Agent type | single-agent multi-role Codex material phase |
| Invocation ID | `delta-t3-governed-command-launcher-material-codex-2026-06-19` |
| Expected manifest | `EXTENSIONS\CVF_ECO_v2.5_MCP_SERVER/package.json`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.test.ts`; `docs/reviews/CVF_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_COMPLETION_2026-06-19.md`; `docs/reviews/evidence/delta-t3-governed-command-launcher-2026-06-19.json` |
| Actual changed set | `EXTENSIONS\CVF_ECO_v2.5_MCP_SERVER/package.json`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts`; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.test.ts`; `docs/reviews/CVF_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_COMPLETION_2026-06-19.md`; `docs/reviews/evidence/delta-t3-governed-command-launcher-2026-06-19.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime component. Public-sync is not authorized.

## Claim Boundary

Accepted material proves only wrapper-owned execution of two exact Git
inspection profiles after durable T1/T2/T3 admission. It does not make the
wrapper mandatory outside its path, execute arbitrary or mutating commands,
intercept external tools, prove provider behavior, or establish universal
governed coding.
