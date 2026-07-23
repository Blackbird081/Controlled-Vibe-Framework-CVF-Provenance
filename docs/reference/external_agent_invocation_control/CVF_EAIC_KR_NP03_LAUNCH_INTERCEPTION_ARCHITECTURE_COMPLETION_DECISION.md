# CVF EAIC-KR NP-03 Launch Interception Architecture Completion Decision

Memory class: FULL_RECORD

docType: reference

Status: REVIEWER_ACCEPTED_NO_VIABLE_BOUNDED_PATTERN_WITH_BOUNDARY_REPAIR

Date: 2026-07-23

Batch ID: CVF-EAIC-KR-NP03

## Purpose

Decide whether NP-03 (launch bypass detection: an external agent process
started outside the proposed EAIC coordinator's admission path) can receive
a source-backed accountable owner, covered launch surfaces, platform
boundary, smallest build slice, and deterministic proof seam under a
bounded CVF design. This packet compares at least five bounded pattern
families against fresh current-source evidence, separates prevention,
detection, post-launch observation, result quarantine, and universal
interception, and issues exactly one `np03ArchitectureReadiness` verdict.
It implements nothing, launches or observes no external-agent process or
process under study, and does not authorize T5. Local Git, search, and
governance-check tooling is ordinary repository evidence work.

## Scope / Applies To

Applies only to the NP-03 launch-interception architecture-completion
decision for the CVF-EAIC-KR roadmap, as the sole isolated pre-T5 reopen
named by the T4 completion review. Does not apply to T5 authoring,
implementation, runtime execution, provider/model selection, or any
external action.

## np03ArchitectureReadiness

`NO_VIABLE_BOUNDED_PATTERN`

No bounded, provider-neutral, non-invasive pattern compared below can
detect an out-of-band external-agent launch that never calls any
CVF-governed surface, without either (a) claiming host-wide process
observation authority this packet has no source basis to assert, or
(b) reducing to a narrower, already-partially-proven pattern (governed
result quarantine) that this packet does name a bounded owner, slice, and
seam for, but whose claim is strictly narrower than "detects launch
bypass"  -  it can only reject an *uncorrelated result claim*, not detect,
observe, or reject the *launch* itself. Because the work order's mandatory
NP-03 requirement is detection of the launch bypass "before it can produce
an accepted governed result" (per the T3 NP-03 wording verified below),
and no compared pattern meets that bar for the actual out-of-band case,
`NO_VIABLE_BOUNDED_PATTERN` is the correct verdict rather than
`PARTIAL_NOT_READY`, which would misleadingly imply that closing a
remaining gap is merely a matter of degree. The one partial component found
(governed-result quarantine) is recorded in full below because it has real,
narrower value and must not be discarded, but it does not itself satisfy
NP-03 as worded.

## Source Verification

Fresh current-source evidence, re-verified at this tranche's
executionBaseHead rather than reused from T3/T4 without recheck.

| Claimed item | Source file | Verified section/lines | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- |
| NP-03 requires bypass detection before an accepted governed result, with `NOT_DETECTED` as explicit FAIL | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T3_OWNER_ARCHITECTURE_AND_THREAT_MODEL_DECISION_PACKET.md` | T4 Negative-Proof Plan, NP-03 row | `NP-03` | ACCEPT |
| current launch-bypass owner is absent (`OWNER_SURFACE_NOT_FOUND`) | same file | Threat Model, THREAT-04 | `OWNER_SURFACE_NOT_FOUND` | ACCEPT |
| T4 requires owner/surfaces/platform/slice/seam before T5; NP-03 has no assigned build slice under CANDIDATE-D's current scope | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T4_BUILD_READINESS_AND_NEGATIVE_PROOF_DECISION_PACKET.md` | Pre-T5 Architecture Completion Requirement; Negative-Proof Feasibility Matrix, NP-03 row | `NP-03` | ACCEPT |
| T5 roadmap authoring is `NOT_READY`; NP-03 is the sole isolated pre-T5 reopen | `docs/reviews/CVF_EAIC_KR_T4_BUILD_READINESS_AND_NEGATIVE_PROOF_COMPLETION_REVIEW_2026-07-23.md` | Decision / Disposition; Finding-To-Governance Learning Disposition | `t5RoadmapAuthoringReadiness` | ACCEPT |
| governed command launcher accepts only registered profile commands, resolves a governed workspace path, and runs one child process via a direct spawn-and-kill runner; explicitly does not claim external interception | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 168-186 (interfaces); lines 274-359 (`launchGovernedCommand`); `DirectGovernedCommandRunner.run` | `launchGovernedCommand`; `externalInterceptionProved: false` | ACCEPT (freshly re-read this tranche; unchanged from T3/T4) |
| governed command runner uses `child.kill()` on a non-detached child process; T1 confirms this is not a whole-process-tree mechanism | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`; `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | `DirectGovernedCommandRunner.run`; T1 ledger row S8/S9 | `DirectGovernedCommandRunner` | ACCEPT |
| Windows Job Objects and POSIX process groups are documented external prior art, explicitly not used by any current CVF launcher, and remain `RUNTIME_CANDIDATE` with no implementation | `docs/reference/external_agent_invocation_control/CVF_EAIC_KR_T1_PRIMARY_SOURCE_INTAKE_LEDGER.md` | Value Conversion Matrix rows S8, S9, S10, S11; Cross-Source Reconciliation | `RUNTIME_CANDIDATE` | ACCEPT (fresh re-read this tranche) |
| governance-action preflight evaluates one planned action, persists a secret-safe audit entry, and fails closed on persistence failure; explicitly does not prove execution or interception | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 181-283 (`preflightGovernanceAction`) | `preflightGovernanceAction`; `governedActionClaimAllowed` | ACCEPT (fresh re-read this tranche) |
| governance-action receipt consumer validates one fresh matching ALLOW receipt against an exact action/target binding and atomically claims it once; explicitly does not prove action execution or external interception, and has no launch-identity, PID, or CLI/MCP-session field on its input or response shape | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-receipt-consumer.ts` | lines 1-340, entire file, freshly read this tranche (not cited by T3 or T4) | `consumeGovernanceActionReceipt`; `RECEIPT_CONSUMER_CONTRACT` | ACCEPT (new source, not previously cited in T3 or T4) |
| receipt-consumption store claims one receipt with create-exclusive file semantics only, keyed by `receiptId`, with no process/launch identity field | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 36-80 (`claimReceipt`) | `claimReceipt` | ACCEPT (fresh re-read this tranche) |
| MCP tool-call audit wrapper records only voluntary, cooperative tool calls (success, duration, argument keys) made through this MCP server's own registered tools; produces zero entries for any process that never calls a registered tool | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/mcp-tool-audit.ts` | lines 1-91, entire file, freshly read this tranche (not cited by T3 or T4) | `withMcpToolAudit`; `recordMcpToolCall` | ACCEPT (new source, not previously cited in T3 or T4) |
| MAO operational worker launcher composes a durable run store, a lifecycle controller, and an injected adapter port; its own module comment states it makes no real provider/network/process/queue call, and the adapter it calls is a fake/local delegation adapter, not a real external-agent process launcher | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | lines 1-16 (module comment); lines 190-365 (`MaoOperationalWorkerLauncher.launch`) | `MaoOperationalWorkerLauncher` | ACCEPT (freshly re-read this tranche; unchanged from T4's cited row) |
| a governance/security-labeled sandbox-execution contract (`SandboxExecutor`) exists with typed containment-violation detection (filesystem/network/resource), but its own module comment states `worker_threads` provide thread isolation, not a process/filesystem/network containment security boundary, and the currently wired default executor is an explicit no-op stub returning fabricated stdout | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts` | `SandboxIsolationContract` types; `stubExecutor`; module header comment | `SandboxExecutor`; `stubExecutor` | ACCEPT (new source, not previously cited in T3 or T4; found by fresh repo-wide search this tranche) |
| `SandboxExecutor` has exactly four consumers repository-wide, all within its own contract/adapter/test cluster; no code path routes an external CLI/MCP agent's own process launch through this sandbox mechanism | fresh repo-wide search this tranche | `Grep` for `SandboxExecutor` across `EXTENSIONS/*.ts`, 4 files, all in `CVF_v1.7.1_SAFETY_RUNTIME`/`CVF_v1.7.3_RUNTIME_ADAPTER_HUB` | `SandboxExecutor` | ACCEPT (fresh negative-search evidence, not reused) |
| no `sandbox`/`broker`/`containment` mechanism anywhere in `EXTENSIONS/` mediates an externally-initiated CLI/MCP agent process; the 191-file substring hit set is dominated by an unrelated in-browser code-execution sandbox (`cvf-web`) and this repository's own delegated-execution sandbox contract, neither of which observes external launches | fresh repo-wide search this tranche | `Grep` for `sandbox\|Sandbox\|broker\|Broker\|containment\|Containment` across `EXTENSIONS/`, 191 files; each candidate file individually classified below in the Pattern Comparison Matrix | (no single symbol; classification result) | ACCEPT (fresh negative-search evidence, not reused) |
| no admission-owner, process-tree binder, cumulative-envelope aggregator, stop-state model, or provider/model reconciliation schema exists anywhere in `EXTENSIONS/` (unchanged from T4's fresh finding) | fresh repo-wide search this tranche, re-run rather than assumed | `Grep` for `EAICCoordinator\|EaicCoordinator\|ExternalAgentCoordinator\|admissionDecision\|AdmissionDecision`; `processTree\|process-tree\|jobObject\|JobObject\|processGroup\|ProcessGroup`; `cumulativeEnvelope\|CumulativeEnvelope\|parentAssignmentEnvelope\|crossRetryEnvelope` across `EXTENSIONS/` | (no true matches for any) | ACCEPT (freshly re-run this tranche, not reused from T4) |
| zero commits touched `EXTENSIONS/` between T4's closure base and this tranche's executionBaseHead | `git log --oneline 19a4ecc6f..60da7b40b` | full range | commit range `19a4ecc6f..60da7b40b` | ACCEPT (freshly recomputed this tranche) |
| internal helpers inherit the parent session unless they cross the external perimeter | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule | `INTERNAL_AGENT` | ACCEPT |
| aggregate decision must not exceed per-item authority evidence | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0028.md` | Purpose; Remediation | `ADIF-0028` | ACCEPT |

## Pattern Comparison Matrix

Common rubric for all six families: `controlStage` (PREVENT, DETECT,
QUARANTINE, or COMPOSED), what it can observe, what bypasses it entirely,
and whether NP-03 as worded (detect bypass before an accepted governed
result) can pass under it.

| patternId | Pattern family | controlStage | Source-backed component (if any) | Can it satisfy NP-03 as worded? |
| --- | --- | --- | --- | --- |
| PAT-01 | Mandatory governed launch path or wrapper | PREVENT (for cooperative callers only) | governed command launcher (`launchGovernedCommand`); requires a registered profile and a preflight receipt before it will start a process | NO. It prevents unregistered commands from launching *through it*, but any process started by any other means (shell, IDE task runner, ad hoc script, a different MCP server, a directly invoked binary) never touches this code path at all. A wrapper can only govern callers who choose to call it. |
| PAT-02 | Host-controlled broker, sandbox, or process containment boundary | PREVENT/CONTAIN (if real) | `SandboxExecutor` contract exists with typed containment-violation detection, but the wired default is `stubExecutor` (fabricated result, no real containment), and the contract's own comment states `worker_threads` is not a security boundary for process/filesystem/network containment; real containment would require `docker`/`v8_isolate`, neither of which has a concrete adapter in this repository | NO. Even setting aside that no adapter provides real host-level containment today, this pattern family governs code CVF *itself* chooses to delegate into a sandbox. It does not observe or contain a process an external agent launches independently of CVF, because there is no OS-level supervisory boundary (no Job Object, no cgroup, no container runtime) wrapping the host session itself. |
| PAT-03 | OS observation followed by reject or quarantine | DETECT (if implemented) | none; T1 confirms Windows Job Objects and POSIX process groups are `RUNTIME_CANDIDATE` external prior art, not a CVF-governed source or binding | NO. No source anywhere in the repository enumerates, polls, or subscribes to OS process-creation events. This is not merely unbuilt; this packet does not attempt to design it, because doing so would require host-wide process-enumeration authority (observing all processes on the operating system, not only ones CVF started), which is explicitly out of this packet's non-goals ("no universal OS, IDE, shell, filesystem, or user-process control claim") and has no current CVF authorization. |
| PAT-04 | Surface-specific IDE, shell, or MCP integration | DETECT (surface-scoped, if implemented) | none found; `withMcpToolAudit` records only cooperative calls to this MCP server's own registered tools | NO. `withMcpToolAudit` produces exactly zero audit entries for a process that never calls one of this server's registered tools. No IDE extension, shell hook, or other MCP host integration exists anywhere in `EXTENSIONS/` (fresh repo-wide search found zero matches for IDE-extension/shell-hook/MCP-host vocabulary). Even if such an integration existed, it would only cover the one specific surface it is built for, never a bypass through a different surface  -  this is the platform-boundary limitation the work order requires this packet to name, not a defect unique to CVF's current source. |
| PAT-05 | Governed-result admission that quarantines outcomes lacking a correlated launch receipt | QUARANTINE (partially proven, narrower claim) | `consumeGovernanceActionReceipt`/`RECEIPT_CONSUMER_CONTRACT` (`governance-action-receipt-consumer.ts`) validates one fresh ALLOW receipt against an exact `actionClass`/`action`/`targetFiles` binding, rejects mismatched, expired, ambiguous, or already-consumed claims, and atomically claims it once via `JsonReceiptConsumptionStore.claimReceipt`'s create-exclusive semantics | PARTIAL, NOT NP-03 AS WORDED. This is real, source-backed, and does reject an *uncorrelated or replayed result claim* presented to this specific consumer tool. But it has no launch-identity field (no PID, no CLI/MCP session ID, no process-tree binding) on either its input or its persisted marker, so it cannot distinguish "this result came from the launch this receipt was actually issued for" versus "this result came from any process that happens to know a valid, unconsumed receipt ID for a superficially matching action/target binding." More fundamentally: nothing requires any external agent's result to ever be routed through this consumer at all. An out-of-band launch that simply never calls `cvf_consume_governance_action_receipt` produces a result CVF never sees through this path, so quarantine never triggers  -  it is not that quarantine fails, it is that quarantine is never invoked. This satisfies the Decision Safety Rule's own worked example ("a receipt quarantine design may claim rejection of uncorrelated results, but it must not claim that it prevented or terminated the underlying process") but not NP-03's literal detect-the-bypass requirement. |
| PAT-06 | Composed pattern | COMPOSED | PAT-01 (launcher) + PAT-05 (receipt quarantine) composed | NO, for the same reason as each part individually. Composing a mandatory-path wrapper with a receipt-quarantine consumer narrows what a *cooperative* caller can get away with (it must present a valid, matching, unexpired, once-only receipt), but composition does not create host-wide launch visibility. Any process that bypasses both by never calling either surface remains completely unobserved. Composition cannot manufacture detection capability that no constituent part has. |

Six pattern families were compared (the five mandatory families plus the
required composed-pattern check), one more than the work order's minimum
of five.

## Prevention, Detection, And Quarantine Matrix

| patternId | Prevention capability | Detection capability | Quarantine capability |
| --- | --- | --- | --- |
| PAT-01 | Exact: denies an unregistered command profile or a preflight-rejected action from launching *through this specific launcher call path*. Cannot prevent a launch that never calls this code. | NONE | NONE |
| PAT-02 | NONE (wired executor is a stub; no real adapter provides host-level containment for an externally-initiated launch) | NONE | NONE |
| PAT-03 | NONE | NONE (not implemented; not attempted, per this packet's non-goals) | NONE |
| PAT-04 | NONE | NONE (no IDE/shell/MCP-host integration exists) | NONE |
| PAT-05 | NONE | NONE (does not observe the launch) | Exact: rejects a result claim whose receipt is missing, mismatched, expired, ambiguous, or already consumed, for calls that are actually routed to this consumer |
| PAT-06 | Same as PAT-01, bounded to cooperative callers | NONE | Same as PAT-05, bounded to callers who route through it |

No pattern claims prevention, detection, or quarantine beyond what its cited
source demonstrates. No pattern is described as having "detected" a bypass
merely because it saw a cooperative, correctly-routed call.

## Owner And Authority Boundary

No accountable CVF owner exists today for launch-bypass detection as NP-03
requires it (`OWNER_SURFACE_NOT_FOUND`, confirmed unchanged by fresh
repo-wide search this tranche). The one component with a real, narrower,
bounded claim is the governance-action receipt consumer
(`consumeGovernanceActionReceipt` / `RECEIPT_CONSUMER_CONTRACT`), which
could be named the accountable owner for a *narrower* quarantine
sub-capability (rejecting an uncorrelated result claim presented to it) if
a future, separately authorized packet chooses to build on it. This packet
does not name it as the NP-03 owner, because NP-03 as worded requires
detecting the bypass, not merely rejecting a voluntarily-presented,
mismatched claim.

## Covered And Excluded Launch Surface Matrix

| Surface | Coverage under any current or proposed bounded pattern | Basis |
| --- | --- | --- |
| A registered command launched through `launchGovernedCommand` with a valid preflight receipt | COVERED (admission-gated) | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` |
| A result voluntarily submitted to `cvf_consume_governance_action_receipt` with a matching, fresh, unconsumed receipt | COVERED (quarantine-gated for replay/mismatch) | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-receipt-consumer.ts` |
| A shell command run directly by an operator or script outside any CVF tool | EXCLUDED | no source observes or mediates it |
| An IDE task runner, extension, or built-in terminal launching a process | EXCLUDED | no IDE integration exists anywhere in `EXTENSIONS/` |
| A different MCP server or MCP host launching an external agent | EXCLUDED | no MCP-host-wide interception exists; this server's audit only covers calls voluntarily made to its own registered tools |
| A provider-native internal helper reasoning inside an already-authorized parent session | EXCLUDED FROM SCOPE BY DESIGN, NOT A BYPASS | per the roadmap's Agent Internal Autonomy And Invocation Perimeter and this work order's Non-Goals, this is not a governed perimeter crossing at all; excluding it is correct, not a gap |
| Any process whose result is never routed to the receipt consumer | EXCLUDED | quarantine is opt-in per result; nothing forces routing |
| Windows Job Object or POSIX process-group-based whole-tree observation | NOT IMPLEMENTED ANYWHERE | T1 confirms these remain `RUNTIME_CANDIDATE`; no CVF source binds to either mechanism |

## Platform Boundary Matrix

| Platform/surface | Boundary |
| --- | --- |
| Windows | No Job Object binding exists; `DirectGovernedCommandRunner` uses plain `child.kill()`, which does not terminate a process tree and cannot observe processes it did not start |
| POSIX (Linux/macOS) | No process-group (`setpgid`) binding exists; Node's own `child_process` documentation (cited via T1 S9) explicitly confirms killing a direct child does not terminate grandchildren by default |
| IDE hosts | No CVF-governed IDE extension or hook exists in this repository |
| Shell | No CVF-governed shell hook, profile injection, or command interception exists in this repository |
| MCP host (this server) | Covers only voluntary calls to its own registered tools (`launchGovernedCommand`, `preflightGovernanceAction`, `consumeGovernanceActionReceipt`, etc.); has no authority over any other MCP server or host process |
| Result-admission (receipt consumer) | Covers only a result deliberately submitted with a receipt ID; has no visibility into results that are never submitted |

## Smallest Build Slice

`NOT_DESIGNABLE`

No current source and no combination of currently named components
provides an observation point from which a future implementation could
detect an out-of-band launch. A "smallest build slice" requires at least
one proof-seam-adjacent hook to attach to; PAT-01 through PAT-04 provide no
such hook for the actual bypass case, and PAT-05/PAT-06 provide a hook only
for the narrower, already-cooperative quarantine sub-case, which this
packet declines to mislabel as an NP-03 build slice. Naming a slice here
would require this packet to either invent an unproven interception
mechanism or silently narrow NP-03's scope without operator authorization,
both of which this work order's Decision Safety Rule and Non-Goals forbid.

If a future, separately authorized packet wishes to build only the
narrower quarantine capability (not NP-03 as worded), the smallest such
slice would be: extend `ReceiptConsumptionMarker`/`consumeGovernanceActionReceipt`
with an optional launch-identity field, populated only when a launch
already goes through `launchGovernedCommand`, and require it to reconcile
against the caller's own claimed identity at consumption time. That slice
is out of scope for this packet's own verdict because it does not close
NP-03; it is recorded only so a future decision is not authored from a
blank slate.

## Deterministic NP-03 Proof Seam

Because no pattern satisfies NP-03 as worded, this section records why a
deterministic fixture cannot be designed for launch-bypass *detection*
today, and separately records the deterministic fixture that *does* exist
for the narrower quarantine sub-case, so the distinction is explicit rather
than silently merged.

### NP-03 detection fixture (launch bypass): `NOT_DESIGNABLE`

No observation point exists to attach a fixture to. Any fixture claiming to
"detect" a bypass would have to fabricate a signal no current source
produces, which the Decision Safety Rule expressly forbids ("a wrapper-only
design that sees only cooperative launches cannot claim out-of-band
detection").

### Quarantine fixture (narrower, already-source-backed sub-case)

- Fixture inputs: a `receiptId` from a real prior `preflightGovernanceAction`
  ALLOW decision; an `actionClass`/`action`/`targetFiles` binding.
- Expected evidence: `consumeGovernanceActionReceipt` returns
  `accepted: true, receiptConsumed: true` exactly once for a fresh, matching
  receipt.
- Pass condition: a second call with the identical `receiptId` returns
  `RECEIPT_ALREADY_CONSUMED`; a call with a mismatched `action`/`targetFiles`
  against a real receipt returns `RECEIPT_BINDING_MISMATCH`; a call with an
  unknown `receiptId` returns `RECEIPT_NOT_FOUND`.
- Fail condition: any of the above three negative cases instead returns
  `accepted: true`.
- False-positive protection: a fresh, correctly bound, unconsumed, unexpired
  receipt must return `accepted: true` exactly once, so the fixture also
  proves the mechanism does not reject legitimate cooperative use.

This fixture is deterministic and requires no provider call or uncontrolled
host action (it exercises pure functions against an injectable in-memory
store, matching the existing pattern in
`governance-action-receipt-consumer.test.ts`). It is recorded as evidence
for a future, narrower, separately authorized packet. It does not prove
NP-03 as worded and is not claimed as doing so.

## Internal-Helper Non-Interference Proof

Consistent with the EAIC-KR roadmap's Agent Internal Autonomy And
Invocation Perimeter section and the T3/T4 THREAT-13/NP-09 boundary, this
packet's own authoring (including internal Explore/Grep/Glob search helpers
used inside this same parent session to run every negative search and
source verification above) does not treat any internal helper as a
separately governed invocation. An internal helper becomes a separately
governed invocation only when it independently crosses a process, external
service, provider/account, credential, durable-action, scope, or authority
boundary. No such boundary was crossed while authoring this packet: no
external CLI/MCP agent was invoked, no provider/API/account/network/browser
action occurred, and no external-agent process or process under study was
launched, enumerated, observed, intercepted, or controlled. Local Git, search,
and governance-check tooling remained inside the repository evidence workflow.
None of the patterns compared above (PAT-01
through PAT-06) propose gating, charging, or separately admitting a
parent-session-internal helper; every proposed or existing mechanism
targets only an externally-initiated CLI/MCP agent process boundary.

## Residual Bypass Register

| Residual bypass | Why it remains open | What would be required to close it |
| --- | --- | --- |
| Any shell command, script, or binary launched outside every CVF tool | No observation point exists | host-wide process-creation observation (Windows ETW/Job Objects, Linux `ptrace`/eBPF, or equivalent), which is explicitly out of this packet's non-goals and would require fresh, explicit operator authorization for host-wide surveillance scope, not merely a build slice |
| An IDE task runner or extension-launched process | No CVF-governed IDE integration exists | a surface-specific IDE extension built and maintained per-IDE, each covering only that one IDE |
| A different MCP server or MCP host launching an agent | No MCP-host-wide interception exists; this server only sees its own tool calls | either a host-level MCP proxy (which would need to intercept every MCP host, not just this server) or per-host cooperative integration |
| A result whose author simply never calls the receipt consumer | Quarantine is opt-in per result | making result-consumption mandatory for some accepted-outcome definition, which is a policy/architecture decision outside this packet's authority and was not requested |
| A caller who obtains a legitimately-issued receipt for one action and replays its ID against a different but string-identical `action`/`targetFiles` binding under a different, correlated launch | `bindingHash` binds `action`/`targetFiles` strings, not launch/process identity | adding a launch-identity field to the receipt marker and reconciling it at consumption time, per the narrower slice described above |

## T5 Authoring Consequence

This verdict is advisory only. `np03ArchitectureReadiness:
NO_VIABLE_BOUNDED_PATTERN` does not open, authorize, or imply readiness for
T5 roadmap authoring, implementation, or any external action. Per the T4
completion review's Pre-T5 Architecture Completion Requirement, if no
viable, provider-neutral, non-invasive pattern can be source-backed for
NP-03, the lane remains parked rather than opening an implementation
roadmap that cannot reach its own final acceptance condition. That
condition is met here: NP-03 remains parked.

## Minimal Unblock Condition

Because the verdict is `NO_VIABLE_BOUNDED_PATTERN`, not `PARTIAL_NOT_READY`,
there is no incremental build-slice unblock path recorded (per Smallest
Build Slice above, `NOT_DESIGNABLE`). The condition that would change this
verdict is an explicit, fresh operator decision to authorize one of the
following, each of which is a scope-expansion decision outside this
packet's authority, not a build task this packet can size:

1. authorize host-wide process-creation observation (a materially larger
   authority grant than any prior EAIC-KR tranche, with its own security,
   privacy, and platform-support review); or
2. explicitly accept the narrower governed-result-quarantine claim (PAT-05)
   as sufficient NP-03 coverage for CVF's purposes, formally narrowing
   NP-03's own wording rather than this packet silently doing so; or
3. supply new primary-source evidence (per the T1 intake discipline) of a
   CVF-appropriate, non-invasive launch-observation mechanism this packet's
   fresh search did not find.

Absent one of these three operator-owned decisions, no future
documentation-only packet can change this verdict by re-analysis alone,
because the blocking fact is source absence, not analysis depth.

## Epistemic Process Block

### Expected Result / Prediction

Per this work order's Epistemic Process Block, universal interception was
expected to remain unsupported, while a bounded mediated-launch plus
result-quarantine pattern might be viable if its claim stayed narrower than
process prevention.

### Evidence Comparison

Fresh direct re-inspection of the two previously-cited launcher sources,
plus two newly-cited sources not previously used in T3 or T4
(`governance-action-receipt-consumer.ts` and `mcp-tool-audit.ts`), plus a
fresh repo-wide search for sandbox/broker/containment vocabulary (191
substring hits, individually triaged to two relevant clusters: an unrelated
in-browser code-execution sandbox and this repository's own delegated
in-process sandbox contract with a stub-only wired executor), confirmed the
prediction's second half only partially: a bounded result-quarantine
pattern (PAT-05) is real and source-backed, but its claim is narrower than
NP-03 requires (it quarantines a voluntarily-submitted, uncorrelated
result; it does not detect an out-of-band launch). The prediction's first
half (universal interception remains unsupported) was fully confirmed.

### Contradiction Or Gap Disposition

No contradiction was found between fresh evidence and the expected
prediction. The gap is that PAT-05's real capability is narrower than what
NP-03's wording requires; this packet does not paper over that gap by
labeling PAT-05 (or the PAT-06 composition built on it) as satisfying
NP-03, per the Decision Safety Rule's explicit instruction that a
receipt-quarantine design "must not claim that it prevented or terminated
the underlying process," which by direct extension means it must not claim
to have detected a launch it never observed.

### Claim Update

`np03ArchitectureReadiness=NO_VIABLE_BOUNDED_PATTERN` is the source-backed
conclusion. This is not a prediction carried forward by default: the
worker's initial expectation before evidence review was that a composed
pattern (PAT-06) might narrowly qualify, and this packet's own evidence
review is what narrowed that expectation once the receipt consumer's exact
scope (opt-in, result-only, no launch-identity field) was directly read
rather than assumed from its name. T5, implementation, and the invocation
moratorium remain unaffected and parked.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | one documentation-only NP-03 launch-interception architecture-completion comparison and verdict |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, launch-observation, or process-control behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this packet itself |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action, process launch, process observation, or negative-proof case is executed |
| invocationBoundary | no agent CLI/MCP, provider, browser, network, or process invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, process, or user-activity interception claim |
| claimLanguage | architecture comparison, owner/surface/platform/slice/seam analysis, and residual-bypass register only |
| forbiddenExpansion | runtime control, live proof, T5 authorization, provider/model selection, host-wide surveillance authority, cost claim, public claim, or moratorium lift |

## NP-03 Architecture Completion Boundary Statement

This packet is
`REVIEWER_ACCEPTED_NO_VIABLE_BOUNDED_PATTERN_WITH_BOUNDARY_REPAIR`. It
does not implement, launch, enumerate, observe, intercept, or control any
external-agent process or process under study. It does not claim that CVF can detect an arbitrary out-of-band
external-agent launch today. It preserves the one narrower, real,
source-backed governed-result-quarantine component (PAT-05) as future
reference evidence without claiming it satisfies NP-03. The global
external-agent CLI/MCP invocation moratorium remains fully in force. T5
and all runtime/external-action lanes remain parked pending a fresh,
separate, explicit operator decision among the three Minimal Unblock
Condition options above.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private architecture decision with no implementation,
public artifact, or public-sync authorization.

## Claim Boundary

This packet proves a source-traceable, freshly re-verified comparison of
six bounded interception/quarantine pattern families against NP-03's
literal wording, and issues one verdict:
`np03ArchitectureReadiness=NO_VIABLE_BOUNDED_PATTERN`. It does not prove or
implement arbitrary launch observation, process prevention, OS containment,
IDE/shell interception, receipt quarantine as a build, or external-agent
control. It does not authorize T5, implementation, provider/model
selection, host-wide surveillance authority, or lift the CLI/MCP invocation
moratorium.
