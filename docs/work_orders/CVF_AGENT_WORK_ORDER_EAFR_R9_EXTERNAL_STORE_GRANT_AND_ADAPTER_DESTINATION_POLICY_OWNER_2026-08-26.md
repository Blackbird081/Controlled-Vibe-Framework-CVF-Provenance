# CVF Agent Work Order - EAFR-R9 External Store Grant And Adapter Destination Policy Owner

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Work order ID: EAFR-R9

Date: 2026-08-26

dispatchBaseHead: `52736f4493361088494ce6396262095d3bbdc0a9`

executionBaseHead: worker must capture actual HEAD and require this committed packet as ancestor

closureBaseHead: reviewer captures the committed dispatch head

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer/closer: current independent orchestrator/reviewer

Worker: external-store grant and adapter destination-policy worker role

## Dispatch Prompt Envelope

originalDispatchCommit: `cec7a67ca0664295e6def40e71ea212489218baa`

reviewerRepairDisposition: `REVIEW_REJECTED_REPAIR_APPLIED`

Batch ID: EAFR-R9-EXTERNAL-STORE-GRANT-AND-ADAPTER-POLICY.

Role: no-commit source-verification and design-decision worker.

Canonical packet: this committed work order and its paired baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

providerExecutionAuthority: FORBIDDEN

R9 is a source-verification and design-decision tranche. It makes no provider
call and edits no source or test file, so no orchestrator provider grant is
requested, issued, or consumed.

Current-time notes: R8 is accepted `CLOSED_BLOCKED` at material commit
`fe0ea5937` and session-recorded before repair base `52736f449`; the R7/R8 fail-closed guard is
retained; the external-store grant and adapter destination-policy residuals
were reverified at repair base `52736f449`.

Do-not-misread notes: designing a grant contract or naming a destination-policy
owner is not the same as implementing either. Drafting source code, a package
dependency edit, or a permit-list copy is out of scope and returns
`BLOCKED_WITH_REASON`. Re-accepting the adapter residual without a source-backed
owner decision is not a valid outcome, exactly as under R8's contract.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this packet, paired baseline, the R8 completion review,
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`, every
pinned input, and the applicable checker sources for every output class.

Return contract: the worker return artifact only, no other file, no
stage/commit, `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Worker return path: `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md`

sourceAuthority: paired GC-018 baseline, committed EAFR roadmap, accepted R7/R8
completion reviews, and source-verified cvf-web, gateway, and foundation files
named in this packet

## Purpose

Source-verify and decide, without implementing, a bounded orchestrator-issued
external-store execution grant design and one shared adapter
destination-policy owner disposition, so a later, separately authorized
implementation work order has an exact target instead of another open
residual.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R9 --title "External Store Grant And Adapter Destination Policy Owner" --date 2026-08-26 --base f357d8e50 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified grant-contract precedent, shared-package reachability finding, destination-policy owner disposition set, and egress invariant preservation rule |
| checkerReadAheadConfirmation | applicable dispatch and worker-output checker sources read |
| docOnlyNewFields | External Store Grant Contract; Adapter Destination Policy Owner Contract; Egress Invariant Preservation Rule |
| claimBoundary | dispatch authoring only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R8 blocked closure | `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_COMPLETION_2026-08-26.md`; material commit `fe0ea5937` | ACCEPT |
| R8 corrective scope statement | same review, Risk / Corrective Action naming an orchestrator-issued external-store grant and a shared, non-duplicated adapter destination-policy owner | ACCEPT |
| R7 blocked closure | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md`; material commit `74cf99354` | ACCEPT |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, EAFR-R9 row | ACCEPT |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_2026-08-26.md`.

The worker may create exactly the one path in Write Ownership. No other path
is writable, including no source, no test, no package manifest, no
configuration. The worker must not stage or commit.

## Authority Chain

Operator EAFR authority -> committed roadmap -> accepted R7/R8 closures ->
paired baseline -> this work order -> no-commit worker -> independent
reviewer/closer.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| bounded orchestrator-issued external-store grant | External Store Grant Contract | worker-return grant design decision | source citation of `delegation.contract.ts` precedent | PASS |
| non-duplicated adapter destination-policy owner | Adapter Destination Policy Owner Contract | worker-return owner disposition | source citation of package manifests and adapter file | PASS |
| preserve R8 non-live isolation | Egress Invariant Preservation Rule | unchanged runtime files | `git diff --name-status` shows no source/test path | PASS |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, the bootstrap read model, active
handoff, `docs/reference/guard_orientation/README.md`, governed literal
gotchas, `DESIGN.md`, paired baseline, this work order, the R7 and R8
completion reviews, `delegation.contract.ts`, every pinned source, and
worker-output checker sources named below. Resolve the full session registry
only for a targeted missing or contradictory fact.

## Agent Roles

Operator owns scope; dispatcher owns the packet; worker source-verifies and
decides without implementing or committing; reviewer independently challenges,
repairs, closes, and commits.

## Pre-Flight Checks

Confirm clean worktree, empty staging, actual HEAD, committed repaired-dispatch
ancestry, all immutable-input pinned hashes, absent worker-return path, and zero live-test
selection. Capture the current denial-reason and dependency-manifest state
before any read. Hash drift or an existing return path blocks before
authoring.

## Write Ownership

Exactly this one path:

1. `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md`

No source file, test file, package manifest, configuration file, environment
file, checker, roadmap, registry, session, baseline, work order, or public
clone path may be created or edited.

Forbidden: editing `provider-execution-guard.ts`, `delegation.contract.ts`,
`openai-compatible-execute-adapter.ts`, any adapter test file, any package
manifest (including adding a dependency), any vitest or tsconfig
configuration, any environment file, any checker, roadmap, registry, session,
baseline, work order, public clone, or deployment path.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_COMPLETION_2026-08-26.md` | `775a8785de820c8e2bbe163d2045e922a94956fc8dd13f58a121fb446943c5c4` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | `2e4f869bb6d912db9a480b0d178be62bce457991f90f485da13d13f72bc237f5` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | `75f342ce7e09815af99b3ac778b980373986bc54f39608ca3aecf4e823082c74` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `22f264e8e3a8b6cb74d74fad8ae353a6d052a0a4fa2442a7581bcd69169d53c4` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts` | `c04cb4f5391d7dd0096e45d52837be4d20fa257627ce9159d4e0735e3ea06886` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` | `e872962581b31772fbbd4a338723877abef1d2db889c763a261e5c7662cfdd61` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | `b0b287624aa473c5908155b107d7416874626be737b605d044f4617e92f57ee9` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | `5ae505e2b23e2701ba4ab9673f677ea5872e2bac27a434ab18def3a528e26f22` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/package.json` | `d5137fe031a17857ad31117ecbc4e9a922ab46cfd8209672a76cff864a5febc3` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `ed166c492657ab0600af7043f17c2d11b5ca75b52109ef6f3f036bd8c0bd8868` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | `3d0bd39f2f45e734bc9b87351ccce810a1d9854208789f1d775e072aae563ad5` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/storage-adapter.ts` | `d57ea274ac95235ef15fd3d577c8141ba27458576810acb654f505db83a119e6` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts` | `bc573b2a6133b07404c42f797bce43fe73464711e0281f29da8234bf2fed6b27` |

The new worker-return path must be absent. Every hash in this table is
calculated at repair base `52736f449`; mismatch returns `BLOCKED_WITH_REASON`
before any decision is recorded. The active roadmap is intentionally verified
by committed authority and ancestry rather than exact current-file hash because
session synchronization legitimately updates its dispatch-status row.

## Verified Prior State

Verified at dispatch head. The worker must re-derive and report divergence:

| Fact | Evidence | R9 ownership |
| --- | --- | --- |
| provider-execution grant contract exists, scoped to `provider` only | `delegation.contract.ts` lines 5-91 | REUSE_AS_PRECEDENT |
| `classifyDestination` exists only in a test-only file | `provider-execution-guard.ts` line 118 | NAME_AS_RESIDUAL |
| gateway package has zero declared runtime/workspace dependencies | `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` | REJECT_INCOMING_DEPENDENCY_DESIGNS |
| cvf-web already depends on cvf-model-gateway | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | TEST_GATEWAY_AS_SHARED_OWNER |
| gateway is the approved official gateway surface and runtime-primitives implementation owner | `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | TEST_GATEWAY_AS_SHARED_OWNER |
| adapter calls injected fetch with no destination check | `openai-compatible-execute-adapter.ts` lines 47-70 | UNCHANGED_RESIDUAL |

R9 owns only the design-decision output. Editing any of the above files is out
of scope, and reporting a design as implemented would be false.

## Verified Root Cause

- `evaluateProviderExecutionAuthority` proves the orchestrator-grant pattern
  works for provider egress: subject/delegation/grant-id/provider/call-budget/
  expiry checks, all evaluated before the guard permits a `provider`-classified
  request;
- the same pattern has no external-store analogue because
  `ProviderExecutionGrant.allowedProviders` and
  `ProviderExecutionRequest.provider` are typed as a single provider identity
  string, not a general destination-class identifier;
- `classifyDestination`'s logic (protocol/hostname classification) is
  conceptually destination-general, but its concrete implementation lives only
  inside `cvf-web`'s test tree and is invisible to any other package;
- the gateway package declares no runtime dependency, so a design that makes
  it import from `cvf-web` or `cvf-control-plane-foundation` is a new
  package-boundary decision;
- `cvf-web` already depends on `cvf-model-gateway`, so gateway-local ownership
  requires no new dependency edge: the adapter can call the policy locally and
  the Web guard can consume the same exported interface through its current
  dependency;
- copying `classifyDestination`'s logic into the gateway would create the
  exact forbidden second permit list the R8 work order already named.

## External Store Grant Contract

A deliberate external-store execution capability must be authorized the same
way deliberate provider execution is: by an orchestrator-issued, bounded,
expiring grant evaluated before the operation, never by a test-selection
variable or an ambient credential.

1. **Grant shape precedent.** Reuse the subject/delegation/call-budget/expiry
   shape already proven by `ProviderExecutionGrant` and
   `evaluateProviderExecutionAuthority`. Decide, without implementing, whether
   this is achieved by (a) a new sibling contract type in the same owning file
   or package scoped to an external-store identifier, or (b) a generalized
   field on the existing contract; either decision must preserve
   `ProviderExecutionGrant`'s existing behavior for callers that do not use the
   new field.
2. **No ambient authority.** An environment variable, local `.env` file value,
   or test-selection flag must never itself constitute a grant.
3. **Fail-closed default.** Absent a valid grant, external-store execution
   remains denied exactly as it is today.
4. **Bounded scope.** This is a contract-and-evaluator design decision only;
   wiring it into `rate-limit.ts` or `storage-adapter.ts` is out of scope
   unless a later work order explicitly authorizes it.

## Adapter Destination Policy Owner Contract

`classifyDestination` must become reachable by both the cvf-web guard and the
gateway adapter through one shared, non-duplicated owner, not by copying its
logic into a second permit list and not by silently re-accepting the residual.

Acceptable dispositions, in preference order:

- **DESIGNATED_SHARED_PACKAGE_OWNER**: source-verify and name the exact shared
  package and interface. Test `cvf-model-gateway` first because the adapter can
  call a local module and cvf-web already depends on the gateway package.
  Creating/exporting the module and replacing the test-only owner is
  implementation deferred to the follow-on work order.
- **BOUNDED_WITH_NAMED_RESIDUAL**: no such shared owner can be source-verified
  after the gateway candidate is tested against current owner/package rules.
  Name the disqualifying source, blocking condition, and exact authority
  required. The gateway's empty dependency list alone is not a valid blocker.

`ACCEPTED_AS_IS` and silent carry-forward are forbidden. The residual was
accepted once in R7 and again in R8; R9 exists to either name its shared owner
or explain precisely why none exists yet, not to re-accept it without new
evidence.

If naming an owner requires importing classification logic that currently
lives only in the cvf-web test guard, the worker must not recommend copying
that logic into a second permit list. It must either name a shared package the
logic could move to, or return `BOUNDED_WITH_NAMED_RESIDUAL` naming the missing
shared surface.

### Provider registry accounting for this boundary

`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` remain provider-identity-keyed, established in
R6 and preserved through R7/R8. Neither declares a hostname, so neither can
decide destination coverage. The worker must not resolve this boundary by
checking a `providerId` against either registry: a covered provider identity
can still carry an uncovered endpoint, the exact false green R6 recorded.

## Egress Invariant Preservation Rule

The R7/R8 fail-closed default must survive R9 unchanged:

- an unrecognised hostname must still be denied before network I/O;
- provider endpoints must still be derived from gateway constants;
- loopback and non-egress protocols must remain the only ungranted permits;
- an external-store grant design or a shared destination-policy owner
  disposition must not itself widen provider egress and must not recommend a
  second permit list a future endpoint could hide behind.

Because this tranche edits no runtime file, the invariant is preserved by
construction; the worker must confirm this with an unchanged-hash proof over
every pinned runtime file rather than a behavioral test.

## Required Implementation

### Decision A - external-store grant design

- Cite the exact precedent lines in `delegation.contract.ts` for
  `ProviderExecutionGrant`, `ProviderExecutionRequest`, and
  `evaluateProviderExecutionAuthority`.
- Record one design decision: sibling contract type or generalized field, with
  the exact proposed field names and their types.
- State explicitly that no code implementing this decision is written in this
  tranche.

### Decision B - adapter destination-policy owner

- Assign exactly one disposition from the Adapter Destination Policy Owner
  Contract.
- Inspect the cvf-web dependency on `cvf-model-gateway`, the gateway package
  role, and its export barrel before deciding.
- If `DESIGNATED_SHARED_PACKAGE_OWNER`, name the exact package path and the
  exact function/interface the adapter would call.
- If `BOUNDED_WITH_NAMED_RESIDUAL`, name the exact blocking condition (for
  example, a cited owner rule that disqualifies gateway-local policy ownership)
  and the exact authority a follow-on work order would need.

## Adversarial Proof Matrix

| Vector | Boundary under test | Required result |
| --- | --- | --- |
| worker edits a source or test file to "prove" the design | write-ownership boundary | forbidden; only the worker-return path may be created |
| grant design widens `ProviderExecutionGrant`'s existing behavior for provider callers | precedent-preservation rule | forbidden; existing callers must be unaffected |
| destination-policy owner recommends copying classification logic into the gateway | shared-owner rule | forbidden; must name a shared package or return bounded |
| owner disposition makes the gateway import cvf-web or cvf-control-plane-foundation | package-boundary fact | forbidden without fresh dependency authority; gateway-local ownership requires neither import |
| owner disposition ignores the existing cvf-web to gateway dependency | owner-reachability evidence | forbidden; test gateway-local ownership before returning a residual |
| provider registry keyed by `providerId` proposed as the destination-policy owner | R6 false-green rule | forbidden; destination classification must remain endpoint-keyed |
| ambient credential or test-selection flag proposed as a valid external-store grant | no-ambient-authority rule | forbidden; only an orchestrator-authored grant object is valid |
| a design decision is reported as already implemented | scope honesty | forbidden; this tranche is decision-only |
| provider or external-store call made during verification | zero-call rule | forbidden; blocked return with disclosure |

## Acceptance Criteria

- only the worker-return path is created; staging is empty;
- every pinned runtime/package hash is unchanged from dispatch;
- Decision A cites exact precedent lines and states one concrete design, with
  an explicit no-implementation statement;
- Decision B assigns exactly one disposition, not `ACCEPTED_AS_IS`;
- if `DESIGNATED_SHARED_PACKAGE_OWNER`, the named package and interface are
  real and source-checkable; if `BOUNDED_WITH_NAMED_RESIDUAL`, the blocking
  condition and required authority are named;
- zero provider calls and zero external-store calls, explicitly stated;
- worker-return fast gate passes; staging empty; worker HEAD unchanged.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R9",
    "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "NONE",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_2026-08-26.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_2026-08-26.md",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json"
  ],
  "claims": ["a bounded external-store grant design and one adapter destination-policy owner disposition are source-verified and recorded, with zero implementation"],
  "requiredProof": ["source citations", "unchanged runtime/package hashes", "grant design decision", "adapter owner disposition", "hashes", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["source edit", "test edit", "package manifest or config edit", "provider or external-store call", "widening egress permits", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| worker role | no-commit external-store grant and adapter destination-policy worker |
| reviewer role | independent reviewer/closer |
| external intake | none; all claims verified in CVF-owned sources |
| escalation condition | hash drift, a required source/test/config edit, inability to name a real shared-owner candidate, any external call, or a needed extra path |
| risk sensitivity | preserving fail-closed egress while naming, not granting, new authority surfaces |
| scope classification | bounded single-path source-verification and design-decision output |

## Required Commands

Run from repository root:

1. recompute pinned hashes for all inputs named in this packet;
2. a search confirming no other source or test file was modified
   (`git diff --name-status`);
3. `git status --short --untracked-files=all` and
   `git diff --cached --name-only`;
4. `python governance/compat/run_worker_return_fast_gate.py`.

Do not run `npm run build`, `npm run test:run`, `npm run check`,
`npm run test:live`, Playwright, any provider, network, credential,
release-gate, package-install, public-sync, deployment, or installation
command. Do not run any command whose purpose is to contact the external
store, since no runtime file changes in this tranche.

## Execution Plan

1. Capture startup, clean status, empty staging, HEAD, ancestry, return-path
   absence, and pinned hashes.
2. Read `delegation.contract.ts` and record Decision A's precedent citations
   and proposed design.
3. Read both package manifests, the gateway README/export barrel, and adapter
   source; test gateway-local policy ownership before recording Decision B.
4. Confirm no runtime/package hash changed.
5. Write the worker return, run the fast gate, and return without staging or
   committing.

## Verification Commands

Run every Required Command, including the full:

`python governance/compat/run_worker_return_fast_gate.py`

Individual checker substitution is forbidden.

## Evidence Requirements

Report pre/post HEAD and status; the one created path; unchanged-hash proof
for every pinned runtime/package file; Decision A's precedent citation and
proposed design; Decision B's disposition and its supporting citation; the
negative search confirming no prior EAFR-R9 artifact existed before dispatch;
worker-return fast gate output; empty staging; an explicit zero-provider-call
and zero-external-store-call statement; and explicit zero external-effect
evidence.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for hash drift, an attempted source/test/config
edit, inability to name a real shared-owner candidate or a real blocking
condition, any provider or external-store call, a needed extra path, or any
design that would restore silent external egress or make deliberate live
external-store use permanently unreachable.

## Worker Autonomy / No-Question Rule

Decide and record both dispositions without asking the operator. Do not expand
scope into implementation. If Decision B cannot name a real shared owner,
return `BOUNDED_WITH_NAMED_RESIDUAL` with the blocking condition named, and
keep Decision A's design honest rather than inflating it into a claimed
implementation.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R9 is a fresh source-verification and design-decision
tranche; prior R7/R8 evidence establishes the residuals but not their
resolution, so citations and hashes must be freshly recomputed against the
pending worker tree

priorVerificationArtifact: accepted R8 completion review and R7 completion
review

priorVerificationAnchor: pinned SHA-256 values in this work order

freshRecomputeRequired: source citations, hashes, and the negative-search
result

unicodePathHandling: use literal repository-relative paths and UTF-8-safe
readers

extractedTextAuthority: CVF-governed sources and fresh local command output
only

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R9 is scoped to exactly two design decisions named by R8's corrective lane | ROADMAP_AUTHORITY | `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_COMPLETION_2026-08-26.md` | Risk / Corrective Action | EAFR-R9 | R8 completion review | ACCEPT |
| the orchestrator-grant contract and evaluator already exist for provider execution | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | lines 5-14, 48-55, 57-91 | ProviderExecutionGrant; ProviderExecutionRequest; evaluateProviderExecutionAuthority | cvf-control-plane-foundation delegation contract | ACCEPT |
| `classifyDestination` is defined only in a test-only file | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | line 118 | classifyDestination | cvf-web provider execution guard | ACCEPT |
| the gateway package declares zero runtime or local workspace dependencies | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` | `dependencies`/`devDependencies` fields | cvf-model-gateway package manifest | cvf-model-gateway | ACCEPT |
| cvf-web already depends on cvf-model-gateway | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies entry | cvf-model-gateway | cvf-web package manifest | ACCEPT |
| cvf-model-gateway is the approved official gateway surface and a gateway-runtime implementation owner | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | package role and current-cycle execution class | CVF_MODEL_GATEWAY | cvf-model-gateway README | ACCEPT |
| the adapter still calls a caller-injected fetch with no destination check | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `execute()` body, lines 47-70 | createOpenAiCompatibleExecuteAdapter | OpenAI-compatible execute adapter | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | dispatch status; Source Verification Block; Current Runtime Freshness Verification; Evidence Reuse scalar fields; worker-return headings; trace and delta labels; providerExecutionAuthority declaration; equivalence disposition tokens |
| gateRunPurpose | confirm as evidence that the completed source-verified packet matches checker shape |
| claimBoundary | checker conformance does not prove either design decision is implementable or the owner reachable at runtime |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external store execution authority`, role=`worker`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external store execution authority" --role worker --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R9 baseline, work-order and return paths | all absent before dispatch authoring | PASS |
| token search | `EAFR-R9` existed only in the EAFR roadmap's next-tranche row and the R8 completion review's corrective-lane text | PASS |
| shared-owner candidate survey | cvf-web already depends on cvf-model-gateway; the adapter is local to that gateway; gateway-local ownership is reachable without a new dependency edge | PASS |
| collision decision | create at most the one worker-return path; no new helper module, contract file, or package | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | cvf-web grant contract precedent and gateway adapter package boundary | design/decision documentation only; no runtime product change | source citations and unchanged pinned hashes | local source only | HARDEN_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP read, authority, or adapter behavior is created or changed | unchanged adapter contract surfaces | separate source-verified work order required | DEFERRED_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | dispatch pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=52736f449; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | one worker-return path only |
| traceScope(phase, actor) | external-store grant design and adapter destination-policy owner decision |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; RFR, BuildAuthority, provider/live, build and all external effects parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read every checker source applicable to its
docType, path family, and conditional content. Derive actual headings and
literal tokens before authoring; checklist prose is not a substitute for the
real sections.

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| external-store grant design | cite precedent, state one concrete sibling-type-or-generalized-field decision, and state explicitly that no implementation occurred |
| adapter destination-policy owner | assign one disposition with real supporting citations |
| worker return | record complete uncommitted evidence, both decisions and honest scope-boundary reporting |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must carry the full review-family/no-commit shape, cite this work
order, report the actual dirty paths (the single worker-return file only),
carry one disposition per decision, and preserve every residual without
relabeling.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_COMPLETION_2026-08-26.md` |
| reviewerOwnedClosurePaths | worker return, optional completion review, EAFR roadmap and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Reviewer must independently verify both citations against live source, confirm
no runtime or package file changed, challenge whether the named shared-owner
candidate (or blocking condition) is real, and decide whether a follow-on
implementation work order may be dispatched next.

## Review Gate

Only the independent reviewer/closer may accept, repair authorized defects,
run closure gates and commit. Acceptance requires direct source inspection and
fresh recomputation, not worker self-report.

## Closure Checklist

- only the worker-return path changed, and staging is empty;
- every pinned runtime/package hash is unchanged;
- Decision A cites real precedent lines and states one concrete, unimplemented
  design;
- Decision B assigns exactly one disposition, not `ACCEPTED_AS_IS`;
- zero provider and zero external-store calls.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all acceptance evidence, including
a disposition for both decisions. Otherwise return `BLOCKED_WITH_REASON`,
naming the first unresolved condition and preserving partial or failed
evidence.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: R9 creates one worker-return document only; it creates no foundation family file or storage topology |
| Protected storage paths | memory foundation filenames, folder front door, generated aggregates and indexes remain unchanged |
| Follow-up condition | any new stable foundation file, split, relocation, or generated-state edit needs separate authorization |

## Operator Authority Boundary

operator.checkpoint.waiver: none. Provider/live/network, build, credential
access, RFR resumption, BuildAuthority repair, package-dependency edits,
public sync, deployment, and push all require fresh explicit authority.

## Core Guard Self-Protection Authorization - R9 Dispatch Repair State Hashes

Authorized guard-maintenance scope: update only the active-authority hashes
for the reviewer-repaired baseline and work order, regenerate the aggregate,
and preserve the current mode until the material repair commit exists.

Protected paths: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`.

Operator authorization: operator directed the current orchestrator/reviewer to
clean every R9 dispatch finding before worker handoff.

Rollback boundary: revert only the R9 dispatch-repair hash synchronization if
the repaired material packet is rejected; retain prior EAFR closure history.

Not authorized: worker source/test/package edits, provider/live/network or
external-store calls, credentials, build, RFR, BuildAuthority repair, public
sync, deployment or push.

## Commit Prompt Readiness

- worker commit: forbidden;
- reviewer material commit: only after independent acceptance;
- session sync: separate commit;
- push/public sync: unauthorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator plus independent reviewer repair |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R9 dispatch authoring and reviewer repair, 2026-08-26 |
| Working directory | repository root |
| Command or tool surface | source reads, searches, hashes, scaffold, ADIF resolver, packet authoring, reviewer repair and gates |
| Target paths | R9 baseline and work order |
| Allowed scope source | accepted R8 completion review corrective lane and EAFR roadmap |
| Before status evidence | clean worktree at repair base `52736f4493361088494ce6396262095d3bbdc0a9`; staging empty |
| After status evidence | corrected baseline and work order pending material repair commit |
| Diff evidence | direct diff over the two exact dispatch documents; mutable roadmap pin removed; omitted dependency evidence added |
| Approval boundary | R9 dispatch only |
| Claim boundary | no worker implementation, live, provider, external-store, build, or public effect |
| Agent type | dispatcher |
| Invocation ID | `eafr-r9-dispatch-2026-08-26` |
| Expected manifest | baseline and work order |
| Actual changed set | baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R9 dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: pinned source hashes and source-verified residual citations |
| actionEvidence | ACTION_EVIDENCE_PRESENT: committed baseline/work order after gates |
| invocationBoundary | local documentation authoring plus safe read-only source verification |
| interceptionBoundary | no universal runtime, CLI, MCP, provider, or coding-control interception claim beyond the already-accepted R7/R8 test-harness guard |
| forbiddenExpansion | paths and effects outside the single worker-return path, including source edits, configuration, environment files, provider or external-store calls, build, package-dependency edits, and RFR |
| claimLanguage | packet authorizes bounded source-verification and design-decision output only after commit |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | no new external input; every R9 claim derives from CVF-owned sources and fresh local measurement |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap, R7/R8 completion reviews, and current cvf-web, gateway, and foundation sources |
| Disposition | N/A_WITH_REASON: no new external knowledge intake in this tranche |
| Claim boundary | accepted CVF reviews are authority; no external report is cited as authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named-file source verification and a design decision, not an intake
refresh.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - R9 makes no repository-wide or
  all-surface completeness claim. The shared-owner survey is a bounded
  targeted search over two named packages.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: inspection would show a real, reusable grant
  precedent for provider execution but no equivalent for external-store
  destinations; independent review would also test whether the claimed
  package-boundary blocker survives the complete dependency direction.
- Evidence Comparison: the grant precedent held. The original package-blocker
  claim did not: cvf-web already depends on cvf-model-gateway, the adapter is
  local to that gateway, and the gateway is the approved runtime-primitives
  implementation owner. Gateway-local destination-policy ownership is
  therefore a real candidate requiring no new dependency edge.
- Contradiction or Gap Disposition: the tempting resolution is to copy
  `classifyDestination`'s logic directly into the gateway adapter, which would
  appear to close the residual immediately while creating the forbidden
  second permit list. This packet forbids that explicitly and requires a
  named shared-owner decision or an honest bounded residual instead.
- Claim Update: R9 is ready for bounded no-commit worker execution after the
  reviewer-repaired packet is committed and continuity is synchronized. A
  `BOUNDED_WITH_NAMED_RESIDUAL` outcome on Decision B is acceptable only with a
  source-backed rule that actually disqualifies gateway-local ownership.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| the orchestrator-grant pattern proven for provider execution has no destination-general or external-store-scoped analogue | GOVERNANCE_CONTROL_PLANE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | R9 names the exact extension shape; implementation remains a separate, later-authorized tranche |
| the original dispatch omitted the existing cvf-web to gateway dependency and overstated the package-edge blocker | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | repaired packet makes gateway-local ownership the leading source-verified candidate and permits a residual only with a real disqualifying source |

## Machine Closure Package

| Surface | R9 closure requirement |
| --- | --- |
| Work order | reviewer converts pending dispatch state only after acceptance |
| Completion/reviewer artifact | reviewer-owned decision with citations, dispositions, diff and claim boundary |
| Roadmap | R9 accepted or blocked; RFR remains parked |
| Registry JSON/Markdown | N/A with reason: no corpus/generated registry classification changes |
| External evidence digest | N/A with reason: no external dataset is consumed |
| System loop interlock | R7 -> R8 -> R9 -> follow-on implementation decision remains explicit |
| Session continuity | separate post-material sync required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source-verification and design-decision tranche; no
public-sync authority.

## Claim Boundary

This work order authorizes only bounded source verification and design
decisions across two named residuals. It authorizes no provider, live,
network, credential, build, dependency, environment-file, guard,
configuration, checker, roadmap, registry, public-sync, deployment, or push
action, no RFR resumption, no BuildAuthority repair, and no implementation of
the grant contract, the evaluator, the shared package, or the adapter change.
Naming a design decision is not a security proof and makes no claim about
credential hygiene, past traffic, or production readiness.
