# CVF Governance Latency WS2-T1 Command And Proof Boundary Audit

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: audit

Date: 2026-08-05

Batch ID: CVF-GOVERNANCE-LATENCY-WS2-T1

Self-declared worker-return artifact: no (companion audit; paired worker return
carries the self-declaration and Status marker)

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GOVERNANCE_LATENCY_WS2_T1_2026-08-05.md`

## Purpose

Determine the smallest useful, source-backed command contract for a candidate
WS2 local role and whether an existing cheap technical boundary can enforce
its environment, effects, network, and transitive children. This audit
returns exactly one bounded T1 decision. It does not implement, execute, or
authorize DESIGN, SPEC, or BUILD work.

## Target / Source

Target: the current governed command launcher and its CLI entrypoint.

Source files inspected:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`

## Scope / Methodology

Read-only local source inspection of the governed launcher, its CLI wiring,
its approval-policy dependency, common persistence adapters/stores, and its
test file. Bounded `rg`/`Grep`
searches across `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src` for every symbol
exported by the launcher module (`GOVERNED_COMMAND_LAUNCHER_CONTRACT`,
`getGovernedCommandProfile`, `launchGovernedCommand`,
`DirectGovernedCommandRunner`, `GovernedCommandProfileId`) to separate
production callers from test-only callers. No process, network, package
manager, or provider call was executed. No bypass probe was run. Git status
was captured before and remains clean of unexpected mutation.

## Current Profile And Caller Inventory

The launcher defines exactly three fixed command profiles in
`GOVERNED_COMMAND_PROFILE_IDS` (`governed-command-launcher.ts` lines 33-37):
`git-status`, `git-diff-check`, and `approval-marker-write`
(`APPROVAL_MARKER_PROFILE_ID`). `getGovernedCommandProfile`
(lines 48-73) resolves each ID to a fixed `executable`, immutable `args`
array, and `riskLevel`:

| Profile ID | Executable | Args | Risk level | Mutating target |
|---|---|---|---|---|
| `git-status` | `git` | `-c core.fsmonitor=false -c core.untrackedCache=false status --short` | `R0` | none |
| `git-diff-check` | `git` | `--no-pager diff --no-ext-diff --no-textconv --check` | `R0` | none |
| `approval-marker-write` | `node` | `--version` | `R1` | `.cvf/delta/approval-marker-write.json` |

Bounded caller search results (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src`):

| Symbol | Production caller | Test-only caller |
|---|---|---|
| `launchGovernedCommand` | `governed-exec.ts` line 72 (sole production call site) | `governed-command-launcher.test.ts` (13 `it(...)` cases) |
| `DirectGovernedCommandRunner` | `governed-exec.ts` line 84 (instantiated for CLI runs) | referenced only via the `GovernedCommandRunner` interface mock in tests |
| `getGovernedCommandProfile` | `governed-exec.ts` (indirectly, inside `launchGovernedCommand`); `receipt-to-execution-evidence-auditor.ts` line 98 (`getGovernedCommandProfile(input.expectedProfileId)`, profile lookup for evidence auditing, not command execution) | `governed-command-launcher.test.ts` lines 140-163 |
| `parseGovernedExecArgs` | `governed-exec.ts` line 64 (CLI entrypoint) | `governed-command-launcher.test.ts` lines 369-391 |

`package.json` (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` lines 7-10)
registers `cvf-governed-exec` as a `bin` entry pointing at
`dist/cli/governed-exec.js`, confirming `governed-exec.ts` is the packaged CLI
surface, not an internal-only module.

No other file under `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src` imports
`launchGovernedCommand`, `DirectGovernedCommandRunner`, or
`parseGovernedExecArgs`. `receipt-to-execution-evidence-auditor.ts` imports
only the pure profile-lookup function `getGovernedCommandProfile` and the
`GovernedCommandProfileId` type for evidence classification; it does not
invoke `launchGovernedCommand` and therefore does not execute a command.

Repository-wide build/test commands (`npm test`, `npm run build`, `tsc`,
`vitest`) are not treated as governed-role command demand in this inventory.
They are developer-workflow commands with no cited consumer inside the
governed launcher's own call graph, per the work order's instruction that
repository-wide commands are not role demand merely because they exist.

## Candidate Role And Command-Demand Matrix

| Candidate command | Source-backed availability evidence | Role-demand evidence | Demand disposition |
|---|---|---|---|
| `git-status` (`git -c core.fsmonitor=false -c core.untrackedCache=false status --short`) | profile registry, packaged `governed-exec.ts` entrypoint, and tests | no non-test caller or governed WS2 role contract selects this profile; AGENTS.md requires a status check but does not require this launcher route | `commandDemand: PROFILE_EXISTS_ROLE_DEMAND_NOT_PROVEN` |
| `git-diff-check` (`git --no-pager diff --no-ext-diff --no-textconv --check`) | profile registry, packaged `governed-exec.ts` entrypoint, and tests | no non-test caller or governed WS2 role contract selects this profile; the worker fast gate invokes Git directly, not through `cvf-governed-exec` | `commandDemand: PROFILE_EXISTS_ROLE_DEMAND_NOT_PROVEN` |
| `approval-marker-write` (`node --version`) | profile registry, T4A approval flow, packaged entrypoint, and tests | prior mutation-proof scaffolding establishes availability, not demand by a zero-network reviewer or implementation-worker role | `commandDemand: PROFILE_EXISTS_ROLE_DEMAND_NOT_PROVEN` |
| Any executable or argv outside the three fixed profiles | none found in source | no governed WS2 role contract or non-test caller found | `commandDemand: NOT_SOURCE_IDENTIFIABLE` |

The three profiles and packaged CLI prove a callable fixed-admission surface,
not actual WS2 role demand. No current governed source identifies which of
these profiles a candidate WS2 role must invoke, and no source establishes
demand for a broader surface. Profile availability, entrypoint availability,
and role demand remain separate.

## Command Contract Matrix

| Field | `git-status` | `git-diff-check` | `approval-marker-write` |
|---|---|---|---|
| Executable | `git` (resolved via `PATH`; no absolute-path pin in source) | `git` (same) | `node` (same) |
| Argv | fixed, immutable array (`governed-command-launcher.ts` lines 55, 61) | fixed, immutable array (line 61) | fixed, immutable array (line 67: `['--version']`) |
| cwd | resolved and validated inside `workspaceRoot` only; `resolveWorkspaceCwd` (lines 231-245) rejects absolute `cwd` and any path escaping the workspace via `realpath` plus relative-path containment check | same | same |
| Environment | not set explicitly; `spawn` call omits an `env` option (lines 114-120), so Node's default child-process behavior applies | same | same |
| Filesystem effect | declared argv requests status inspection; packaged CLI persists preflight audit, atomic receipt-consumption marker, and execution receipt; total child effects are not enforced or proved | declared argv requests diff inspection; packaged CLI persists preflight audit, atomic receipt-consumption marker, and execution receipt; total child effects are not enforced or proved | packaged CLI persists those three common records and performs one profile-specific fixed create-exclusive marker mutation; total child effects remain unenforced and unproved |
| Child processes | one `git` child process per invocation; no further children spawned by the launcher itself | same | one `node` child process; no further children spawned by the launcher itself |
| Network | no explicit socket/network call in the launcher or runner source | same | same |
| Timeout | `DEFAULT_COMMAND_TIMEOUT_MS = 600_000` (10 minutes), enforced by `setTimeout` plus `child.kill()` (lines 31, 133-136) | same | same |
| Output | stdout/stderr captured up to `MAX_CAPTURE_BYTES = 65_536` per stream (line 30, `appendBounded` lines 98-102), then redacted via `redactText` before return (lines 491-492) | same | same |
| Receipt | preflight ALLOW audit persisted through `JsonFileAdapter`, atomic receipt-consumption marker claimed before spawn, and execution intent created/finalized through `GovernedExecutionStore` | same | same, plus a separate T4A approval record consumed via `MutatingProfileApprovalPolicy.evaluate` (lines 411-432) before the profile-specific marker write |

## Environment And Secret Boundary

`DirectGovernedCommandRunner.run` calls Node's `spawn(request.executable,
[...request.args], { cwd, shell: false, detached: false, windowsHide: true,
stdio: ['ignore', 'pipe', 'pipe'] })` (`governed-command-launcher.ts` lines
114-120). No `env` key is present in the spawn options object. Per Node.js
`child_process.spawn` semantics, omitting `env` causes the child process to
inherit the full parent process environment, including any credentials,
tokens, or proxy variables set in the parent shell or CI runner.

`environmentContract` (doc-only field): the current source proves **no**
environment minimization. A minimized or explicit allowlisted child
environment is `NOT_SOURCE_PROVEN`. This matches the WS2-T0 accepted finding
F1 (`docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md`,
Findings table row F1) that the launcher omits an explicit `env` option and
credential/proxy inheritance must be treated as a gap, not as merely
uninspected.

`knownCredentialPatternsRedacted: true` is returned on the response object
(`governed-command-launcher.ts` line 199, backed by `redactText` at lines
491-492), but this redacts known credential patterns from captured
**stdout/stderr text only**, after the child process has already run with
the inherited environment. It is not an environment-minimization control and
does not prevent the child process itself from reading inherited secrets
during execution.

## Filesystem Effect Boundary

`git-status` and `git-diff-check` use fixed argv with no declared write-mode
flag. This proves only the launcher's intended command request. It does not
prove total child filesystem effects: executable resolution is PATH-based,
the child environment is inherited, and no effect interception exists.

The packaged CLI composes three common persistence effects for every admitted
profile (`governed-exec.ts` lines 70-85):

- preflight audit persistence: `serializePreflightPersistence(auditAdapter)`
  delegates `saveAuditEntry` to `JsonFileAdapter`, which writes
  `audit-log.json` (`governance-action-preflight.ts` lines 94-116;
  `json-file.adapter.ts` lines 42 and 62-66, with `saveJson` lines 145-153);
- atomic receipt consumption: `JsonReceiptConsumptionStore.claimReceipt`
  creates one receipt marker with `open(..., 'wx')`, writes, and syncs it
  (`json-receipt-consumption.store.ts` lines 73-86);
- governed execution receipt persistence: `beginExecution` creates a durable
  receipt before spawn and `finalizeExecution` truncates and rewrites it after
  execution (`json-governed-execution.store.ts` lines 73-130).

Beyond the three common persistence effects, `approval-marker-write` has one
additional profile-specific filesystem mutation: creating
`.cvf/delta/approval-marker-write.json` inside the resolved workspace root.
`writeApprovalMarkerFile` (`mutating-profile-approval.ts` lines 166-204):

- resolves the target path with `resolve(workspaceRoot, targetRelativePath)`;
- re-derives the relative path and rejects if it escapes the workspace, is
  absolute, or does not literally equal
  `APPROVAL_MARKER_TARGET_RELATIVE_PATH` (lines 177-183);
- creates parent directories with `mkdir(..., { recursive: true })`
  (line 186);
- writes with `flag: 'wx'` (line 202), which fails if the target already
  exists rather than overwriting it.

This is a single fixed-path, create-exclusive write gated behind a separate
T4A approval record (`JsonMutatingProfileApprovalPolicy.evaluate`,
`mutating-profile-approval.ts` lines 88-136) that must already exist in
`mutating-profile-approvals.json` with a matching action hash, binding hash,
and non-expired timestamp before the write is attempted
(`governed-command-launcher.ts` lines 411-432). `effectClass` (doc-only
field) for this profile is `SINGLE_FIXED_PATH_CREATE_EXCLUSIVE_APPROVAL_GATED`.

The fixed marker is therefore the only profile-specific command mutation, not
the only packaged-launcher write. Preflight audit, receipt-consumption marker,
and governed execution receipt persistence are common to all admitted
profiles.
Source does not prove that the spawned executable performs no other write,
delete, or overwrite because child effects and PATH resolution are not
technically contained.

## Network And Transitive-Child Boundary

No source line in `governed-command-launcher.ts`, `governed-exec.ts`, or
`mutating-profile-approval.ts` calls `http.request`, `https.request`,
`net.connect`, `fetch`, `dgram`, or any other network primitive. The bounded
search for `spawn(`, `exec(`, `execFile(`, `fork(`, `http.request`,
`https.request`, `net.connect`, `fetch(` across
`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli` returned exactly one match:
the single `spawn(` call inside `DirectGovernedCommandRunner.run`
(`governed-command-launcher.ts` line 114).

The response contract explicitly declares
`externalInterceptionProved: false` as a literal `false`-typed field
(`governed-command-launcher.ts` line 200, and again in the return statement
at line 507), and the same literal appears on the persisted execution
receipt (`GovernedExecutionReceipt.externalInterceptionProved`, referenced at
line 359 and in `governed-command-launcher.test.ts` line 81). This is a
source-declared invariant, not an inferred gap: the current code makes no
claim to intercept or observe network or transitive-child activity of the
spawned process.

`transitiveChildBoundary` (doc-only field): the launcher spawns exactly one
direct child process per invocation (`git` or `node`), and the source shows
no containment of what that child process may itself spawn, connect to, or
read from the inherited environment. `git` and `node` are both general-purpose
executables capable of invoking further subprocesses or network I/O
independent of the launcher; the launcher provides no OS-level sandbox,
network namespace, or process-tree containment. This is
`NOT_SOURCE_PROVEN` for both current profiles.

## Platform Feasibility Matrix

| Platform | Fixed-profile admission (current) | Technical zero-network/env/child isolation |
|---|---|---|
| Windows | `spawn` uses `shell: false` and `windowsHide: true` (line 118); this is source-confirmed to launch `git`/`node` directly without a shell wrapper on Windows. Directional only: no Windows-specific sandbox, Job Object, or AppContainer wiring is present in source. | `NOT_SOURCE_PROVEN` |
| Linux | `spawn` with `shell: false` behaves as a direct `execve`-style launch under Node's `child_process` on Linux; source shows no Linux-specific namespace, seccomp, or cgroup wiring. | `NOT_SOURCE_PROVEN` |
| CI | No CI-specific runner script, container profile, or workflow file references `governed-command-launcher.ts` or `governed-exec.ts` in the bounded search; source establishes no CI wiring for this launcher at all (used only via direct CLI invocation and the Vitest test file). | `NOT_SOURCE_PROVEN`; also `commandDemand: NOT_SOURCE_IDENTIFIABLE` for any CI-specific role |

Per the WS2-T0 accepted correction (finding F5), these platform ratings are
directional repository-wiring observations bounded to inspected files, not a
general portability or security claim.

## Threat And Bypass Matrix

| Threat family | Current mitigation | Residual gap |
|---|---|---|
| Unknown/arbitrary profile selection | `getGovernedCommandProfile` returns `null` for any ID outside the fixed three; `launchGovernedCommand` returns `rejected('UNKNOWN_COMMAND_PROFILE', ...)` before any preflight or spawn (lines 278-281); CLI parser rejects unsupported flags and extra argv (`governed-exec.ts` lines 26-42; test lines 384-391) | none identified in source for this specific family |
| Argv injection / extra arguments | `args` is a fixed `readonly string[]` per profile, spread directly into `spawn`'s argv array with `shell: false`; the CLI parser accepts no free-form argument list | none identified in source for this specific family |
| CWD escape | `resolveWorkspaceCwd` rejects absolute `cwd` and any path resolving outside the workspace via `realpath` plus relative-path containment check (lines 231-245); test at line 340-344 asserts `CWD_OUTSIDE_WORKSPACE` for a symlink-based escape attempt | `realpath` resolves symlinks before the containment check, which the existing test exercises; no further symlink race (TOCTOU) analysis is present in source |
| Credential/proxy inheritance | none in the launcher/runner; secrets in the parent environment reach the child process because `env` is not set | `REJECT_CURRENT_RUNTIME_CLAIM` per WS2-T0 F1; no environment minimization exists |
| Transitive child network/process activity | none | `externalInterceptionProved: false` is a source-declared invariant; no sandbox, network namespace, or process-tree containment exists |
| Alternate interpreter path | `executable` values (`git`, `node`) are resolved via `PATH` at spawn time, not pinned to an absolute, verified binary path; source does not show any `PATH` restriction or binary-hash verification | `PATH`-based resolution means the effective binary depends on the parent process's `PATH` environment, which is itself inherited without minimization (compounds the environment gap above) |
| Mutating-profile abuse | `approval-marker-write` requires a pre-existing, non-expired, action-hash-matched, binding-hash-matched approval record (lines 88-136) before the write is attempted; target path is validated twice (`validateApprovalMarkerTarget` and the write-time relative-path check) | approval records are read from a local JSON file (`mutating-profile-approvals.json`) with no signature or tamper-evidence beyond a hash match; file-level tampering by a process with local write access is not addressed by this launcher |
| Timeout / hang | `DEFAULT_COMMAND_TIMEOUT_MS` (10 minutes) with `child.kill()` on timeout (lines 133-136) | `child.kill()` sends a default termination signal to the direct child only; source does not show process-tree-wide termination of any grandchild processes the child may have spawned |

## Cheap-Alternative Comparison

| Option | Cost | What it proves | What it does not prove |
|---|---|---|---|
| Fixed-profile admission only (current, accepted at WS2-T0) | Already implemented; zero new work | Only the three registered `executable`+`args` pairs can be launched through this path; unknown profiles are rejected before spawn | Environment minimization, network isolation, transitive-child containment, or that an allowed executable cannot itself misbehave |
| Reduced/explicit child environment (`env` allowlist on `spawn`) | Small, source-localized change (one new `spawn` option); no new dependency | Would close the specific F1 credential/proxy-inheritance gap for the three current profiles | Does not by itself prove network interception or transitive-child containment |
| OS-native process isolation (Windows Job Object / Linux namespace-cgroup sandbox) | Materially higher: new platform-specific code paths, new test matrix per OS, no existing source foundation to build from | Could technically bound network, filesystem, and child-process scope if correctly implemented | Not source-identifiable today; no current file in `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` implements or wires this |
| Parking the zero-network/isolation claim | Zero cost; explicit non-claim | Keeps the launcher's actual current guarantee (fixed-profile admission) accurately stated | Does not advance technical isolation; leaves the WS2-T0 prerequisite unresolved until a future packet |

The cheapest option that satisfies the current source-backed value case
(three fixed, low-risk, already-tested profiles) is to retain fixed-profile
admission as-is. The cheapest option that would close the specific,
source-identified environment gap (F1) without claiming broader isolation is
an explicit `env` allowlist - but that is a DESIGN/BUILD change, which this
T1 packet does not authorize. No cheap, already-existing, source-backed
seam provides network or transitive-child enforcement; OS-native isolation
is the only option that could close that gap and it is not cheap.

## Adversarial Proof Plan That Runs Nothing In T1

This plan defines future evidence classes only. No case listed here was
executed by this audit.

1. Unknown-profile rejection (already covered by existing tests, lines
   160-163 and 169-190 of `governed-command-launcher.test.ts`): confirms
   profile allowlisting, not network/environment isolation.
2. Allowed-profile environment leak probe (future, not run in T1): launch
   `git-status` with a marker environment variable set in the parent
   process and assert whether the child process can observe it, to
   directly test the F1 gap with a real receipt.
3. Allowed-profile network-attempt probe (future, not run in T1): launch a
   profile whose executable is instrumented or wrapped to attempt an
   outbound connection, and assert whether any interception layer blocks
   or observes it. Current source provides no interception layer to test
   against, so this case would currently be expected to show no blocking.
4. Transitive-child probe (future, not run in T1): launch a profile whose
   executable spawns a further child process, and assert whether the
   launcher's timeout/kill path terminates the full process tree or only
   the direct child.
5. Mutating-profile tamper probe (future, not run in T1): attempt to reuse
   or forge an approval record (mismatched binding hash, expired
   timestamp, wrong target path) and assert `APPROVAL_RECORD_NOT_FOUND`,
   `APPROVAL_EXPIRED`, or `APPROVAL_TARGET_MISMATCH` per
   `mutating-profile-approval.ts` lines 89-127.

`proofBoundary` (doc-only field): any of these cases require live process
execution, which is forbidden scope for T1. They are recorded here as the
future adversarial evidence boundary for a separately authorized DESIGN/BUILD
or live-proof packet.

## Receipt And Diagnostic Requirements

Every successful or failed launch produces a `GovernedCommandLauncherResponse`
(lines 186-203) carrying `contractVersion`, `accepted`, `profileId`,
`receiptId`, `consumptionId`, `bindingHash`, `executionStarted`,
`executionCompleted`, `exitCode`, `signal`, redacted `stdout`/`stderr`,
`knownCredentialPatternsRedacted: true`, `externalInterceptionProved: false`,
`approvalBackedMutationProved`, and an optional `error` object with `code`,
`message`, `retryable`. Execution intents are persisted via
`GovernedExecutionStore.beginExecution`/`finalizeExecution`
(`GOVERNED_EXECUTION_RECEIPT_CONTRACT`, imported from
`../persistence/json-governed-execution.store.js`) before and after the
`spawn` call, so a receipt exists even for a process that starts but never
completes (persisted as `FAILED` with a diagnostic code via
`finalizeFailedIntent`, lines 257-272). A future command contract should
require this same intent-before-spawn/finalize-after-spawn receipt shape,
plus the doc-only `proofBoundary` evidence, before any wider profile is
proposed.

## Governance Cost And Stop Rule

This audit began with one bounded source-read pass across the launcher, CLI,
approval policy, tests, execution store, and bounded call-site and primitive
searches. The initial worker-return authoring then required three repair passes,
reaching the GC-018 third-repair stop condition. Work stopped for independent
review. The operator subsequently authorized one bounded F1-F6 correction;
independent re-review retained CR1-CR3. The operator then explicitly authorized
this second bounded correction limited to CR1-CR3 in the same two worker-owned
files. No repair counter is reset, and neither operator authorization widens
scope. Zero provider, network, package-manager, or bypass calls were made,
consistent with the Governance Cost Budget in the paired GC-018 baseline.

## Findings / Position

The current governed launcher is a source-backed owner for fixed-profile
command admission of exactly three registered profiles (`git-status`,
`git-diff-check`, `approval-marker-write`), each with a receipt-gated admission
path and, for the mutating profile, a separate T4A approval record. The CLI is
the execution entrypoint, not an independent role consumer. No non-test caller
or governed WS2 role contract proves which profile a candidate WS2 role needs.

No source-backed technical boundary exists for environment minimization,
network interception, or transitive-child containment. The `env` option is
absent from `spawn`, so parent credentials/proxies are inherited by design of
Node's default behavior. `externalInterceptionProved: false` is a literal,
source-declared non-claim, not an unproven-but-likely-present control. OS
Job Object/namespace-based isolation that could close this gap is not
present anywhere in the inspected source tree.

Position: profile availability is narrow, but exact WS2 role demand is not
source-identifiable. The enforcement/proof boundary for environment, network,
filesystem effects, and transitive children is also not source-backed. T1
therefore cannot establish a design input without a named role consumer and
command contract.

## Risk / Corrective Action

| Risk | Severity | Corrective action (not authorized in T1) |
|---|---|---|
| Inherited credential/proxy exposure to any of the three fixed-profile child processes | MEDIUM (bounded by fixed, low-risk `args`; not exploitable via argv injection) | A future DESIGN packet could add an explicit `env` allowlist to `spawn`; requires fresh operator authorization and a source-verified work order |
| No transitive-child or network containment for any profile | MEDIUM (bounded by the current three profiles' low-risk nature; would be HIGH if profile set widened) | A future DESIGN packet would need to source-identify and wire OS-native isolation before any zero-network claim is made; not cheap, not started |
| `PATH`-based executable resolution (`git`, `node`) rather than pinned absolute paths | LOW-MEDIUM (mitigated by fixed, well-known executable names; compounds with the environment gap) | A future DESIGN packet could pin absolute, verified binary paths; not authorized here |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Launcher exposes exactly three fixed profile IDs | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 33-37 | `GOVERNED_COMMAND_PROFILE_IDS` | `getGovernedCommandProfile` | ACCEPT |
| Each profile has fixed executable, args, and risk level | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 51-71 | `GovernedCommandProfile` | `getGovernedCommandProfile` | ACCEPT |
| `spawn` call omits an explicit `env` option | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 114-120 | `DirectGovernedCommandRunner.run` | `GovernedCommandRunner` | ACCEPT |
| Response and receipt declare `externalInterceptionProved: false` as a literal | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 200 and 507 | `externalInterceptionProved` | `GovernedCommandLauncherResponse` | ACCEPT |
| Packaged CLI composes serialized preflight persistence through the JSON audit adapter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | lines 70-85 | `preflightPersistence` | `runGovernedExecCli` | ACCEPT |
| Serialized preflight persistence delegates each audit entry to its persistence port | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 94-116 | `serializePreflightPersistence` | `PreflightPersistencePort` | ACCEPT |
| JSON audit adapter persists preflight audit entries to `audit-log.json` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts` | lines 42, 62-66, and 145-153 | `saveAuditEntry` | `JsonFileAdapter` | ACCEPT |
| Receipt-consumption store creates and syncs one create-exclusive marker per consumed receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 73-86 | `claimReceipt` | `JsonReceiptConsumptionStore` | ACCEPT |
| Execution-store begin and finalize persist a durable receipt for every admitted profile | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 73-130 | `beginExecution` and `finalizeExecution` | `JsonGovernedExecutionStore` | ACCEPT |
| CLI parser accepts only `--profile`, `--workspace`, `--cwd`, `--json` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | lines 26-42 | `parseGovernedExecArgs` | `GovernedExecCliArgs` | ACCEPT |
| CLI is the sole production caller of `launchGovernedCommand` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | lines 61-87 | `runGovernedExecCli` | `DirectGovernedCommandRunner` | ACCEPT |
| Parser tests reject unsupported/arbitrary argument surfaces | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts` | lines 369-391 | `cvf-governed-exec parser` | `parseGovernedExecArgs` tests | ACCEPT |
| `receipt-to-execution-evidence-auditor.ts` imports only the profile-lookup function, not `launchGovernedCommand` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts` | lines 12-13 and 98 | `getGovernedCommandProfile` | `receipt-to-execution-evidence-auditor.ts` | ACCEPT |
| Package registers `cvf-governed-exec` as a bin entry pointing at the CLI build output | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | lines 7-10 | `bin` | package manifest | ACCEPT |
| Mutating profile requires a pre-existing, hash-matched, non-expired approval record before the marker write | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | lines 88-136 | `JsonMutatingProfileApprovalPolicy.evaluate` | `MutatingProfileApprovalPolicy` | ACCEPT |
| Marker write is a single fixed-path create-exclusive write with workspace-containment checks | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | lines 166-204 | `writeApprovalMarkerFile` | `mutating-profile-approval.ts` | ACCEPT |
| `resolveWorkspaceCwd` rejects absolute or escaping `cwd` values | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 231-245 | `resolveWorkspaceCwd` | `launchGovernedCommand` | ACCEPT |
| Timeout kills the direct child after 10 minutes | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 31 and 133-136 | `DEFAULT_COMMAND_TIMEOUT_MS` | `DirectGovernedCommandRunner.run` | ACCEPT |
| WS2-T0 accepted `OWNER_FOUND_NEEDS_FOUNDATION` for fixed-profile admission only | VALUE_SET | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | Decision Review, lines 77-84 | `OWNER_FOUND_NEEDS_FOUNDATION` | WS2-T0 independent completion review | ACCEPT |
| WS2-T0 finding F1 established the environment gap as a defect, not an unknown | VALUE_SET | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | Findings table row F1, lines 61 and 71 | F1 | WS2-T0 independent completion review | ACCEPT |
| Worker fast gate runs `git diff --check` as a required step | RUNTIME_BEHAVIOR | `governance/compat/run_worker_return_fast_gate.py` | line 57 | `git diff whitespace check` | `build_commands` | ACCEPT |
| ADIF resolver returned zero defects for this task class | RUNTIME_BEHAVIOR | `governance/compat/run_adif_defect_resolver.py` | command output, this session | `totalCandidates` | ADIF resolver | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current governed launcher (`launchGovernedCommand` via `governed-exec.ts` CLI) | source audit only in T1; no profile or runtime mutation performed by this audit | verified launcher, CLI, approval-policy, and test source cited above | fixed-profile admission only; no environment, network, or transitive-child enforcement claimed | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | `cvf-governed-exec` packaged CLI binary (`package.json` `bin` entry); no MCP tool wraps this launcher in the inspected source | no authentication, network-isolation, or generalized external-agent execution claim; CLI accepts only the four documented flags | `governed-exec.ts` and `package.json` sources cited above | a future source-verified adapter packet is required before any external-agent-facing isolation claim | `DEFERRED_WITH_REASON` |

## Epistemic Process Block

Expected Result / Prediction: the three frozen profiles would prove a callable
fixed-admission surface, but a governed WS2 role contract or independent
non-test consumer might not identify actual role demand; no cheap technical
isolation boundary would be found merely from fixed-profile admission.

Evidence Comparison: source confirmed profile and CLI availability but found no
governed WS2 role contract or independent non-test consumer selecting any
profile. Actual role demand is therefore not source-identifiable. The `spawn`
call's omitted `env` option and the literal
`externalInterceptionProved: false` invariant confirm no environment,
network, or transitive-child enforcement exists in source, matching the
WS2-T0 accepted F1/F2/F3 findings.

Contradiction Or Gap Disposition: no source contradiction was found between
the launcher, CLI, approval policy, test file, and the WS2-T0/L0 completion
reviews. All current-source facts are internally consistent; this audit uses
a narrowed/parked decision rather than `BLOCKED_SOURCE_CONTRADICTION`.

Claim Update: this audit accepts only that a fixed-profile admission surface
exists. It does not infer WS2 role demand from availability, does not recommend
a design-ready command and enforcement/proof boundary, and records both actual
role demand and OS-native isolation as unresolved or parked within the T1
boundary.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Profile and CLI availability are source-identified, but actual WS2 role demand is not; the enforcement boundary also has no existing owner surface | RULE_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | preserve `COMMAND_DEMAND_NOT_SOURCE_IDENTIFIABLE`; no promotion or DESIGN work is authorized by T1 |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this audit made no
provider call or runtime-enforcement execution claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `## Target`/`## Source` group, `## Scope`/`## Methodology` group, `## Findings`/`## Position` group, `## Risk`/`## Defect` group, `## Decision`/`## Disposition` group (review doc-type structural groups); `Field`/`Disposition` table shape for the Delta block; exact `DEFECT_CLASSES` and `DISPOSITIONS` enum tokens; `Expected Result`, `Evidence Comparison`, `Contradiction`, `Claim Update` epistemic labels |
| gateRunPurpose | confirm artifact conformance after source-first authoring; the fast gate is run as evidence, used only for confirmation of required shape |
| claimBoundary | T1 audit readiness only; no design implementation, execution, provider, or external-agent support claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only command-demand and enforcement-boundary analysis of the current governed command launcher |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed by this audit |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists or is required for this audit |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local source reads and bounded `Grep` searches only |
| invocationBoundary | read-only provenance inspection plus this documentation output |
| interceptionBoundary | no direct process, network, filesystem, environment, shell, IDE, CLI, MCP, or provider interception performed by this audit |
| claimLanguage | exact current demand and future enforcement/proof boundary only |
| forbiddenExpansion | runtime, bypass execution, provider/live, downstream, public, deployment, readiness, and universal enforcement claims |

## External Knowledge Intake Routing

Chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: this audit consumed only local CVF-governed source and accepted prior completion reviews |
| Matching local-view guard | N/A with reason: no external intake guard applies to this local-source-only audit |
| Owner surface | N/A with reason: no external owner surface is engaged by this audit |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external comparison, critique, or recommendation was intaken in this tranche |
| Claim boundary | local source-native decision only; no external or downstream authority claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this audit is private provenance source analysis. No public artifact
or public-sync action is authorized by this T1 packet.

## Findings And Position Continued: T1 Decision

`T1Decision` (doc-only field): `COMMAND_DEMAND_NOT_SOURCE_IDENTIFIABLE`.

Rationale: current source proves three profiles and one packaged CLI entrypoint,
but no independent governed caller or WS2 role contract selects those profiles.
Availability is not demand. No cheap technical seam exists for environment,
network, filesystem-effect, or transitive-child enforcement either. The
decision is therefore `COMMAND_DEMAND_NOT_SOURCE_IDENTIFIABLE`; technical
zero-network isolation remains parked, but the stronger fixed-admission-value
token is not claimed without a role consumer.

## Claim Boundary

This audit is a bounded documentation and source-verification analysis of
the exact WS2 command demand and technical enforcement/proof boundary. It
returns exactly one T1 decision token
(`COMMAND_DEMAND_NOT_SOURCE_IDENTIFIABLE`). It does not authorize DESIGN
implementation, SPEC implementation, BUILD, process/network/package
execution, provider calls, downstream edits, public-sync, push, deployment,
or any claim that technical zero-network capability enforcement currently
exists.
