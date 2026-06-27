# CVF GC-018 - Delta-T3 Governed Command Launcher

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Execution route: SINGLE_AGENT_MULTI_ROLE

Base head: `f50e2903`

## Purpose

Authorize one bounded Delta-T3 Local Workspace Runtime tranche after Delta-T2
closed at accepted material commit `d3bf3594` and closure commit `22ad256e`.

Delta-T3 adds a local `cvf-governed-exec` binary that owns a small static set
of non-destructive command profiles. The launcher must issue a Delta-T1
preflight receipt, consume it through Delta-T2, persist an execution intent,
and only then invoke the exact profile through a direct process runner.

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
| --- | --- |
| Decision | Dispatch one bounded local governed command-launcher implementation |
| Proposed tranche | Delta-T3 Governed Command Launcher |
| Base head | `f50e2903` |
| Worker / reviewer / closer | Codex across phase-separated roles |
| Route | `SINGLE_AGENT_MULTI_ROLE` |
| Upstream evidence | Delta-T1 and Delta-T2 closures; MCP-GW-001; workspace two-layer standard |
| Later tranche | mutating EDIT/COMMIT profiles and wider IDE/shell interception remain separately authorized work |

## Scope / Target / Owner Boundary

Allowed scope:

- add one package binary named `cvf-governed-exec` in the MCP package;
- add a static CVF-owned profile registry for `git-status` and
  `git-diff-check`; dispatched npm script candidates are rejected because
  project-defined scripts are not statically non-destructive;
- derive one canonical RUN action from the selected profile and resolved
  workspace-relative working directory;
- call the existing Delta-T1 pure preflight handler and persist its audit;
- call the existing Delta-T2 pure consumer and atomically claim its receipt;
- persist a secret-safe create-exclusive execution intent before process start;
- invoke only the exact registered executable and arguments with `shell:false`;
- finalize the execution receipt with exit status and bounded diagnostic data;
- redact known credential patterns from bounded stdout/stderr returned by the
  wrapper, without persisting raw command output;
- add deterministic injected-runner tests, CLI parser tests, package build,
  binary smoke proof, completion review, and evidence JSON.

Forbidden scope:

- no arbitrary executable or caller-supplied argument passthrough;
- no `cmd`, PowerShell, bash, sh, node eval, Python eval, shell control string,
  env override, elevated process, detached process, watcher, queue, or daemon;
- no cwd outside the resolved workspace root, including symlink escape;
- no EDIT or COMMIT execution profile;
- no provider/live API call, credentials, quota, public-sync, or CVF Web work;
- no claim that direct shell, IDE, git, filesystem, or non-wrapper actions are
  intercepted or governed;
- no universal governed-coding, production-readiness, or release-readiness
  claim.

Risk ceiling: R2 local deterministic runtime implementation. The shipped
profiles themselves are R0/R1 and non-destructive. Any mutating command,
arbitrary command, external interception, or provider execution requires a
later fresh GC-018 and source-verified work order.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T1 exports a pure preflight handler taking engine and persistence ports. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | `preflightGovernanceAction` declaration | `preflightGovernanceAction` | Delta-T1 pure handler | ACCEPT |
| Delta-T1 supports RUN and yields a receipt only after durable audit persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | `PREFLIGHT_ACTION_CLASSES`; persistence block | `RUN`; `auditPersisted`; `receiptId` | `preflightGovernanceAction` | ACCEPT |
| Delta-T2 exports a pure receipt consumer and returns execution admission only after atomic claim. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-receipt-consumer.ts` | `consumeGovernanceActionReceipt` | `executionAdmissionEligible` | Delta-T2 pure handler | ACCEPT |
| Delta-T2 marker store reads the persisted audit and uses create-exclusive marker files. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 55-91 | `JsonReceiptConsumptionStore`; `claimReceipt` | `ReceiptConsumptionStore` | ACCEPT |
| JSON persistence owns durable audit save/read under a configured data directory. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts` | lines 31-84 | `JsonFileAdapter`; `saveAuditEntry`; `getAuditEntries` | `PersistenceAdapter` | ACCEPT |
| The MCP package guard factory registers the six current guards. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/index.ts` | lines 24-38 | `createGuardEngine` | guard runtime factory | ACCEPT |
| The current MCP package has a CLI wrapper but no governed process launcher. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts` | module header; `runCli` | `runCli` | MCP package CLI wrapper | ACCEPT |
| The MCP package publishes binaries through `package.json`. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | `bin` | `cvf-mcp-server` | npm package manifest | ACCEPT |
| Delta-T2 explicitly leaves launcher enforcement to later authorization. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T2_GOVERNANCE_ACTION_RECEIPT_CONSUMPTION_COMPLETION_2026-06-19.md` | `## Risk / Corrective Action`; `## Claim Boundary` | `CLOSED_PASS_BOUNDED` | Delta-T2 completion | ACCEPT |
| Local Workspace Runtime calls for MCP/CLI ingress bound to guards and receipts. | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `## Local Workspace Runtime` | `CVF_LOCAL_WORKSPACE_RUNTIME` | workspace two-layer standard | ACCEPT |

## New Delta-T3 Fields

These are new authorized fields, not existing runtime facts.

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| binary id | `cvf-governed-exec` | distinct governed launcher surface |
| launcher contract | `cvf.delta.governedCommandLauncher.v1` | stable bounded result contract |
| execution receipt contract | `cvf.delta.governedExecutionReceipt.v1` | durable execution evidence |
| command profile | static id, executable, args, risk level | deny arbitrary command construction |
| execution intent | create-exclusive record before process invocation | prove admission preceded launch |
| execution final state | `COMPLETED`, `FAILED`, or retained `ADMITTED` after interruption | bounded durable diagnostic |
| action execution marker | true only after runner reports process start | distinguish admission from execution |
| external interception marker | always false | preserve wrapper-only boundary |

## Delta-T3 Execution Control Block

| Field | Disposition |
| --- | --- |
| Action class | `RUN` only |
| Command authority | static CVF-owned profile registry only |
| Admission sequence | T1 durable ALLOW receipt -> T2 atomic consumption -> T3 durable intent -> direct runner |
| Process API | injected runner; production adapter uses direct executable with `shell:false` |
| Working directory | existing real path within existing real workspace root |
| Environment | inherited environment only; no caller override |
| Output | bounded capture; known credential patterns redacted; raw output not persisted |
| Receipt persistence | one create-exclusive execution record per T2 consumption id, finalized atomically |
| Failure posture | no runner call before all three durable admission stages pass |
| Execution claim | bounded to the wrapper-owned child process only |
| Interception claim | always `externalInterceptionProved=false` |
| Provider boundary | no provider or Model Gateway execution |
| Public boundary | private provenance only |

## Rescan Intelligence Hardening

- Original source artifact: `MCP-GW-001`, Delta-T1/T2 completion, and the
  workspace two-layer standard.
- Predecessor intake artifact:
  `docs/reviews/CVF_DELTA_T2_GOVERNANCE_ACTION_RECEIPT_CONSUMPTION_COMPLETION_2026-06-19.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because a bounded wrapper-owned
  execution path moves from parked to operator-authorized.
- Routing matrix status: `DO_NOW` for static non-destructive profiles;
  `SEPARATE_RUNTIME_TRANCHE` for mutating profiles or external interception;
  `OUT_OF_SCOPE` for provider/live, public-sync, queue, and readiness.
- Semantic sampling status: `PARTIAL_TARGETED`, covering no-receipt execution,
  blocked preflight, replay, intent persistence failure, cwd escape, runner
  failure, output redaction, and exact profile invocation.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Machine guard: `governance/compat/check_rescan_intelligence_hardening.py`

### Original-Intake Delta Ledger

| Item | Delta category | Original disposition | Updated disposition | Rationale |
| --- | --- | --- | --- | --- |
| T1 durable preflight | `UNCHANGED_FROM_INTAKE` | implemented and closed | reused as sole preflight authority | prevents duplicate policy evaluation semantics |
| T2 one-time consumption | `UNCHANGED_FROM_INTAKE` | implemented and closed | reused as sole admission-consumption authority | prevents replay before execution |
| Wrapper-owned execution | `CHANGED_DISPOSITION` | parked after T2 | authorized for static non-destructive profiles | operator selected continuation |
| Durable execution intent/final receipt | `NEW_FINDING` | absent in T2 | required before and after child process | preserves crash/failure evidence |
| Arbitrary or mutating execution | `REMOVED_OR_REJECTED` | possible broad launcher goal | rejected from T3 | exceeds bounded R2 profile scope |

### Follow-Up Routing Matrix

| Lane | Applies to | Rationale |
| --- | --- | --- |
| DO_NOW | static non-destructive RUN profiles and execution receipts | bounded T3 foundation |
| RESOLVED_BY_DESIGN | reuse T1/T2 owners and MCP package binary surface | prevents parallel authority |
| SEPARATE_RUNTIME_TRANCHE | EDIT/COMMIT, mutating profiles, arbitrary commands | materially higher execution risk |
| STRATEGIC_OPERATOR_DECISION | IDE/shell/git/filesystem interception breadth | changes operator workflow and control reach |
| OUT_OF_SCOPE | provider/live, public-sync, queue, daemon, readiness | unnecessary for T3 proof |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | required verdict |
| --- | --- | --- | --- | --- | --- |
| DELTA-T3-01 | T1/T2 admission chain | valid consumption permits later execution | `UNCHANGED_FROM_INTAKE` | Can runner start before durable T1/T2/T3 success? | No runner call before all stages pass |
| DELTA-T3-02 | static profile registry | wrapper controls command shape | `CHANGED_DISPOSITION` | Can caller inject executable, args, env, or shell text? | No; unknown or extra input rejected |
| DELTA-T3-03 | workspace boundary | cwd belongs to workspace | `NEW_FINDING` | Can symlink or lexical path escape workspace? | No; real-path containment required |
| DELTA-T3-04 | execution receipt | execution is durably evidenced | `NEW_FINDING` | Can runner failure be reported as success or lose intent? | No; admitted intent remains and final state fails |
| DELTA-T3-05 | claim boundary | T3 improves governed coding | `REMOVED_OR_REJECTED` | Does wrapper prove direct IDE/shell interception? | No; external interception remains false |

## Acceptance Criteria

| ID | Criterion | Dispatch state |
| --- | --- | --- |
| AC1 | `cvf-governed-exec` is published from the MCP package without changing T1/T2 contracts. | PASS |
| AC2 | The runner is unreachable unless T1 ALLOW, T2 consumption, and T3 intent persistence all succeed. | PASS |
| AC3 | Only exact static profiles execute; arbitrary executable, args, env, shell, EDIT, and COMMIT are unavailable. | PASS_BOUNDED: two Git profiles shipped; npm candidates rejected |
| AC4 | Real workspace/cwd checks reject lexical and symlink escape. | PASS |
| AC5 | Execution receipt persists admission/final status without raw action, target, stdout, stderr, or credential values. | PASS |
| AC6 | Runner failure returns a bounded failed receipt and does not become success. | PASS |
| AC7 | Returned output is bounded and known credential patterns are redacted. | PASS_BOUNDED |
| AC8 | Focused tests, full MCP tests, package build, binary smoke, and governance gates pass. | PASS |
| AC9 | No provider/live, public-sync, queue, daemon, mutating profile, or broad interception work occurs. | PASS |

## Evidence / Verification

Required evidence:

- focused Vitest for admission ordering, static profiles, cwd containment,
  durable intent/final receipt, runner failure, and output redaction;
- full MCP package test suite and TypeScript build;
- local binary smoke using a static non-destructive profile in a temporary
  workspace with a secret-safe receipt directory;
- `git diff --check`, exact changed-set evidence, reviewer-fast, autorun phase
  gates, and commit-steward preflights;
- no provider/live receipt because provider behavior is outside this tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime tranche. No public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Baseline status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Material implementation | MCP package source/tests and completion evidence | commit `ff584e42` | PASS |
| Accepted-material continuity | active session state | commit `febf67fc` | PASS |
| Profile boundary | completion review and evidence JSON | two shipped Git profiles; three npm candidates rejected | PASS_BOUNDED |
| Provider/live proof | N/A with reason: no provider claim | no live provider command | N/A with reason |
| Public-sync | N/A with reason: not authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |

## Claim Boundary

Delta-T3 may prove only that the `cvf-governed-exec` wrapper admitted and ran
one exact registered non-destructive command profile after T1/T2/T3 durable
controls. It does not prove direct shell or IDE actions were intercepted, make
the wrapper mandatory outside its own process path, or establish universal
governed coding.
