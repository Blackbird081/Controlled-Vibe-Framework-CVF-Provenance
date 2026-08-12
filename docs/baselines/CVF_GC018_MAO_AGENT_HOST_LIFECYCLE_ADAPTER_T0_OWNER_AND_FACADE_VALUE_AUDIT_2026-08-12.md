# CVF GC-018 Baseline - MAO Agent Host Lifecycle Adapter T0 Owner And Facade Value Audit

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: MAO-AHLA-T0

Date: 2026-08-12

Verification base: canonical private Core `4fd1b6177`

Dispatch base head: `4fd1b6177`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Worker target: one role-neutral documentation worker

## Purpose

Authorize no execution. Define the smallest documentation-only decision packet
needed to determine whether a provider-neutral MAO agent-host lifecycle facade
has enough source-backed value to justify later DESIGN authority.

T0 must be able to terminate the roadmap. A positive T0 is not DESIGN release.

## Scope / Target / Owner Boundary

After canonical integration and explicit dispatch, the worker may create only:

1. `docs/audits/CVF_MAO_AGENT_HOST_LIFECYCLE_ADAPTER_T0_OWNER_AND_FACADE_VALUE_AUDIT_2026-08-12.md`;
2. `docs/reviews/CVF_MAO_AGENT_HOST_LIFECYCLE_ADAPTER_T0_OWNER_AND_FACADE_VALUE_AUDIT_WORKER_RETURN_2026-08-12.md`.

The roadmap, this baseline, work order, external critiques, completion review,
source, tests, packages, governance, session, public-sync, and deployment paths
are not worker-writable.

## Decision / Baseline / Proposed Tranche

| Field | Decision |
|---|---|
| roadmap posture | accepted by external re-review only as a PARKED planning artifact |
| current question | whether a thin facade is justified, not whether a missing lifecycle port must be built |
| known ownership | MAO already owns authority, budget, task-state lattice, read model, evidence, lifecycle, launcher, and durable store concepts |
| likely genuine absence | `send` remains a source-verification hypothesis for T0, not a build instruction |
| partial composition candidate | `wait` has owned primitives; absence of a composition function does not establish facade value |
| T0 terminal power | `CANCEL_UPLIFT_NO_FACADE_VALUE` is a legitimate terminal result |
| later authority | any positive result still requires fresh DESIGN authority before T1 |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| repaired roadmap packet | roadmap and R2 worker return now reside at canonical repo-relative paths | review and commit the bounded packet before dispatch | PASS_LOCATION_HOLD_COMMIT |
| round-1 critique | external input marked `NOT_CVF_SOURCE` | retain as input, never authority | PASS_AS_INPUT_ONLY |
| R2 independent re-review | `REVIEWER_ACCEPTED_PARKED`, also `NOT_CVF_SOURCE` | independently re-verify any adopted claim | PASS_AS_INPUT_ONLY |
| operator selection | operator said `next` on 2026-08-12 | permits packet authoring only | PASS_FOR_DRAFT_AUTHORING |
| canonical dispatch base | clean packet-authoring base `4fd1b6177` | worker captures the later committed packet HEAD as execution base | PASS |
| pre-dispatch gate | 76 of 76 commands PASS against six untracked canonical packet files at `4fd1b6177` | rerun after canonical commit/base refresh | PASS_WORKTREE_HOLD_COMMITTED_RERUN |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| authority and budget already have MAO owners | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | declarations near L32-L49 and builder near L138 at `4fd1b6177` | `MaoBudgetAllocation`; `MaoAuthorityEnvelope`; `buildAuthorityEnvelope` | task graph contract | ACCEPT |
| MAO owns a ten-state task lattice and terminal classifier | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | declarations near L16-L37 at `4fd1b6177` | `MaoTaskState`; `MAO_TERMINAL_STATES`; `isTerminalState` | event ledger contract | ACCEPT |
| blocked and timed_out are recoverable nonterminal holds | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | recoverable-hold declaration near L36 at `4fd1b6177` | `isTerminalState` | event ledger contract | ACCEPT |
| deterministic task read model already exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | builder near L54 and equality near L101 at `4fd1b6177` | `buildReadModel`; `readModelsAreEqual` | read model contract | ACCEPT |
| receipt kind, redaction, evidence readout, and retention already have owners | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | declarations near L31, L98, L279, L347 at `4fd1b6177` | `MaoReceiptKind`; `redactFields`; `buildEvidenceReadout`; `evaluateRetention` | evidence readout contract | ACCEPT |
| heartbeat, cancel, retry, timeout, and orphan primitives already have owners | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | lifecycle declarations near L80-L240 at `4fd1b6177` | `recordHeartbeat`; `isHeartbeatStale`; `requestCancel`; `acceptCancel`; `classifyRetry`; `classifyOrphan` | lifecycle controller contract | ACCEPT |
| operational launcher owns launch and cancellation composition | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | launcher and cancellation declarations near L190-L452 at `4fd1b6177` | `requestCancellation`; `acceptCancellation` | operational worker launcher | ACCEPT |
| durable run creation, resume, and append already have owners | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | declarations near L111-L186 at `4fd1b6177` | `MaoFileRunStore`; `createRun`; `resumeRun`; `appendEvent` | durable run store | ACCEPT |
| candidate symbol search returned no exact AgentHost facade identifiers | SEARCH_RESULT | `docs/roadmaps/CVF_MAO_PROVIDER_NEUTRAL_AGENT_HOST_LIFECYCLE_ADAPTER_FOUNDATION_UPLIFT_ROADMAP_2026-08-09.md` | Negative Search And Collision Discipline | `AgentHost` | roadmap evidence declaration | ACCEPT_WITH_LIMIT: name search is not semantic absence proof |
| external critique and re-review are not CVF source | AUTHORITY_BOUNDARY | `AGENTS.md` | Authority Hierarchy | `NOT_CVF_SOURCE` | root instruction carrier | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `MAO-AHLA-T0` | documentation audit batch identifier | DOC_ONLY_NEW |
| `ALREADY_OWNED` | current source already owns the concept | DOC_ONLY_NEW |
| `PARTIALLY_OWNED` | current source owns primitives but lacks a bounded composition | DOC_ONLY_NEW |
| `GENUINELY_ABSENT` | semantic search and reconciliation find no current owner | DOC_ONLY_NEW |
| `CANCEL_UPLIFT_NO_FACADE_VALUE` | stop before DESIGN | DOC_ONLY_NEW |
| `PROCEED_TO_SEPARATE_T1_DESIGN_PACKET` | T0 evidence supports asking for new DESIGN authority | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

| Check | Current evidence | Disposition |
|---|---|---|
| canonical verification base | Core `4fd1b6177` on 2026-08-12 | PASS_FOR_DRAFT |
| temporary worktree topology | source packet copied byte-exact to Core; temporary worktree is removable and is not a dependency | TRANSIENT_PATH_NOT_A_DEPENDENCY |
| packet state | six canonical documentation paths are untracked and unstaged | PASS_FOR_PARKED_DRAFT |
| source modification | none authorized | PASS |
| dispatch readiness | canonical integration and gates not complete | HOLD |

## Negative Search And Collision Discipline

T0 must use semantic concepts and owned behavior, not only proposed names. Each
search record must name its corpus, exact pattern, hit set, exclusions, and
reconciliation against all 17 MAO files.

Collision tables may list only tokens that the recorded search pattern can
actually match. This carries forward re-review finding N-03.

`send` and `wait` must not be treated as equivalent gaps. T0 must initially test:

- `send`: `GENUINELY_ABSENT` candidate;
- `wait`: `PARTIALLY_OWNED` candidate because all known lifecycle/read-model
  primitives are already owned and only finite-wait composition appears absent.

A composition helper alone does not establish facade value. This carries
forward re-review finding N-01.

## Predecessor Integrity Carry-Forward

The round-1 critique contains independent-reviewer-authored substantive
content. A documentation repair worker added governed wrapper metadata only;
the substantive findings were unchanged. This disclosure carries forward
re-review finding N-02 without rewriting the accepted predecessor artifact.

## Required Decision Evidence

T0 must produce all of the following before a positive decision is reviewable:

1. a hidden/no-ignore 17-file MAO manifest and read ledger;
2. per-concept `ALREADY_OWNED`, `PARTIALLY_OWNED`, or `GENUINELY_ABSENT`
   classification;
3. semantic negative-search evidence with hit reconciliation;
4. direct composition versus facade comparison;
5. at least two consumers with materially different lifecycle shapes;
6. operation-by-operation decision for dispatch, send, wait, interrupt, status,
   and capability discovery;
7. explicit proof that no second state, authority, budget, evidence, lifecycle,
   launcher, store, or handoff owner is proposed;
8. one terminal T0 disposition.

## Evidence / Verification

Dispatch evidence consists of refreshed Source Verification anchors, a
reconciled hidden/no-ignore MAO manifest, an exact changed-set check, the
applicable documentation gates, and reviewer semantic acceptance. Current
evidence supports only a draft HOLD packet because the six canonical paths are
untracked and no committed dispatch base exists.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | existing MAO contracts and possible doc-only facade decision | read-only inventory and architecture decision; no source mutation | current MAO source plus T0 audit | internal composition only; no runtime adapter in T0 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no current lifecycle facade authorized | no ingress, authentication, provider, network, secret, or mutation authority | absence/value decision deferred to T0 evidence | adapter remains explicitly deferred; T0 may only recommend a later packet | `DEFERRED_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defect count: 22 at canonical Core `4fd1b6177`.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006 |
| Dispatch impact | no completeness claim without a reconciled ledger; external critique remains input only; checker read-ahead, exact source symbols, path ownership, bounded execution time, and literal-safe packet shape are mandatory |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_gc018_stop_boundary_semantics.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | status, source-verification columns, stop boundary, no-commit ownership, dual-agent rows, operation trace labels, delta claim tokens, public export token, and machine closure fields |
| gateRunPurpose | confirm packet shape as evidence after source and checker read-ahead; gates are not used for first discovery |
| claimBoundary | checker compliance does not prove facade value or runtime readiness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher documentation author |
| Provider or surface | local governed workspace |
| Session or invocation | MAO-AHLA-T0 draft authoring, 2026-08-12 |
| Working directory | canonical repository plus temporary same-repository worktree |
| Command or tool surface | source reads, targeted searches, ADIF resolver, patch edits, packet checks |
| Target paths | this baseline and companion work order |
| Allowed scope source | operator `next`; accepted PARKED re-review |
| Before status evidence | canonical Core clean at `4fd1b6177`; four untracked packet files in temporary worktree |
| After status evidence | six untracked canonical packet files; temporary worktree removed after byte-exact verification |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | draft T0 documentation authority only |
| Claim boundary | no T0 execution, DESIGN, BUILD, provider, live, commit, merge, or worktree removal |
| Agent type | dispatcher |
| Invocation ID | `mao-ahla-t0-draft-2026-08-12` |
| Expected manifest | baseline and work order additions only |
| Actual changed set | dispatcher records after validation |
| Manifest delta | none expected |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only T0 dispatch draft |
| claimDisposition | `CLAIM_REJECTED`: no execution-control behavior is created |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: no runtime receipt is created |
| actionEvidence | `CLAIM_REJECTED_NO_ACTION`: no provider or runtime action occurs |
| invocationBoundary | local source inspection and documentation authoring |
| interceptionBoundary | no CLI/MCP ingress, provider, browser, network, process, or secret access |
| claimLanguage | draft authority packet pending canonical integration and operator dispatch |
| forbiddenExpansion | no T0 execution, DESIGN, SPEC, BUILD, live proof, public-sync, deployment, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance draft only.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | companion work order | draft HOLD token | BLOCKED with reason: canonical commit, pre-dispatch, and operator dispatch pending |
| Completion or reviewer artifact | future reviewer-owned completion | absent | BLOCKED with reason: T0 not executed |
| Roadmap state | parked roadmap | PARKED status | BLOCKED with reason: T0 not executed |
| Registry JSON | none selected | no registry update authorized | N/A with reason: decision audit only |
| Registry Markdown | none selected | no registry update authorized | N/A with reason: decision audit only |
| External evidence digest | critique and re-review | external input remains `NOT_CVF_SOURCE` | N/A with reason: no external evidence promoted |
| System loop interlock | roadmap T0 gate | positive T0 cannot open T1 automatically | BLOCKED with reason: operator decision remains required |
| Session continuity | active session surfaces | unchanged | BLOCKED with reason: no dispatch or closure transition yet |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| packet integration | canonical repo-relative paths | six untracked canonical paths | PASS_LOCATION_ONLY |
| clean dispatch base | packet-authoring base plus committed packet before execution | `4fd1b6177`; packet commit pending | PASS_BASE_HOLD_EXECUTION_UNTIL_COMMIT |
| pre-dispatch gates | PASS | 76 of 76 at untracked working-tree state | PASS_PENDING_COMMITTED_RERUN |
| worker evidence | audit and worker return | absent | BLOCKED |
| reviewer decision | independent governed review | `REVIEWER_ACCEPTED_T0_DOCUMENTATION_ONLY` | PASS |

## Reviewer Dispatch Decision

Disposition: `REVIEWER_ACCEPTED_T0_DOCUMENTATION_ONLY`.

The owner/facade-value audit is semantically accepted and the pre-dispatch
autorun bundle passed 76 of 76 commands against the six untracked canonical
packet files at HEAD `4fd1b6177`. The packet is dispatch-ready for operator
copy/paste after an authorized canonical commit and clean-status confirmation.
The worker must capture that committed HEAD as `executionBaseHead`. This
decision opens no T1 or implementation authority.

## Claim Boundary

This baseline authorizes documentation-only T0 after canonical packet commit,
clean-status confirmation, and explicit operator copy/paste dispatch. It does
not authorize any DESIGN,
SPEC, BUILD, runtime, provider, live, public-sync, deployment, or production
work.
