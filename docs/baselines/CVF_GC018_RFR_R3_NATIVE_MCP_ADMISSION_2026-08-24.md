# CVF GC-018 RFR-R3 Native MCP Admission Baseline

Memory class: governed-baseline

Status: ACTIVE_BASELINE

docType: baseline

Date: 2026-08-24

Batch ID: RFR-R3

Base head: `cc08ea2da6f23f3f87b6eec7cb6248ecab365b16`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize the bounded RFR-R3 remediation of verified finding F8: remove
caller-supplied policy trust from the MCP Model Gateway execution adapter and
require native CVF admission before any injected executor can run.

## Authorization / Decision

Decision: `PROCEED_WITH_RFR_R3`.

The operator authorized dependency-ordered continuation through the runtime
findings roadmap on 2026-08-24. RFR-R2 is independently closed bounded at
material commit `84d44889fe2724e574241b5fb74d371e900fd6e3`, releasing R3.

## Scope / Target / Owner Boundary

R3 enriches only the existing MCP Model Gateway execution adapter, its two
existing test owners, the MCP registration call, and the existing MCP/Model
Gateway boundary reference. Model Gateway remains provider-execution authority;
the MCP server remains ingress and native admission owner.

The worker may edit exactly six paths named by the paired work order. It may not
edit Model Gateway production source, Execution Plane source, package manifests,
lockfiles, other MCP tools, governance checkers, session state, or the roadmap.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R2 closure | material `84d44889fe2724e574241b5fb74d371e900fd6e3`; continuity `cc08ea2da` | R2 must be independently accepted before R3 | ACCEPT |
| F8 roadmap order | `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`, R3 row | R3 follows R2 | ACCEPT |
| operator authority | explicit 2026-08-24 instruction to continue autonomously under CVF rules | fresh operator release required | ACCEPT |

## Current Verified Gap

`executeModelGatewayAdapter()` currently accepts `policyResult` in MCP input and
copies it directly into `GatewayExecuteRequestPort.policy`. An allowed caller can
therefore submit `policyResult: 'allow'` to an injected executor without a
native CVF admission decision. The default server has no executor and remains
fail-closed, but the exported adapter contract contains the bypass.

## Required Invariants

1. MCP caller input cannot supply, select, or override the execution policy
   decision. Legacy `policyResult` input must be rejected or ignored fail-closed;
   it must never authorize executor invocation.
2. A server-owned native CVF guard engine evaluates a deterministic request
   context before the injected executor is called.
3. Missing, throwing, malformed, trace-mismatched, `BLOCK`, or `ESCALATE` native
   admission returns a secret-safe rejection and calls the executor zero times.
4. Only a valid native `ALLOW` decision may construct the Model Gateway policy
   envelope and reach the injected executor.
5. Native admission evidence is bound to the exact trace and is returned or
   referenced without claiming that provider execution occurred.
6. The registered MCP tool receives the server-owned engine; absence of either
   admission or executor remains fail-closed.
7. Existing role, schema, credential shielding, executor-error shielding, Model
   Gateway receipt preservation, and zero-live-call boundaries remain intact.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| caller policy is accepted and copied into execution request | BYPASS_PATH_CONFIRMED | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | `ModelGatewayExecuteInput`; policy construction | `policyResult`; `executeModelGatewayAdapter` | MCP Model Gateway execute adapter | ACCEPT |
| adapter is exported with an injected executor port | RUNTIME_BOUNDARY | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | `ModelGatewayExecutorPort`; adapter signature | `execute` | MCP execute adapter | ACCEPT |
| default registration currently passes neither native admission nor executor | COMPOSITION_FACT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | execute-tool registration | `registerModelGatewayExecuteTool(server)` | MCP server entry point | ACCEPT |
| direct tests encode caller-supplied allow/deny | TEST_GAP | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | `VALID_INPUT`; policy-denied test | `policyResult` | MCP execute unit tests | ACCEPT |
| composition proof forwards caller policy into ProviderExecutionBridge | TEST_GAP | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `VALID_INPUT`; `makeCompositionExecutor` | `executeModelGatewayAdapter` | MCP-to-Model-Gateway proof | ACCEPT |
| server has a native guard engine singleton | EXISTING_OWNER | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | singleton guard engine | `engine`; `createGuardEngine` | MCP Guard Runtime | ACCEPT |
| boundary assigns ingress to MCP and execution to Model Gateway | GOVERNANCE_REFERENCE | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | Boundary Decision | MCP ingress / Model Gateway execution | MCP Gateway reference | ACCEPT |
| F8 is the accepted R3 finding | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position; Risk / Corrective Action | F8 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.ts` | `24f86294935993fa70bdfe66e204a821bcd4a8378f1d3dfcd2a1242d5f8389e9` |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-execute.test.ts` | `3e5b37eb8a827ebcbcdabca6dc89d1f5bb64e50c3e2743f509a0e06a1ef9fc33` |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/model-gateway-composition-proof.test.ts` | `24fce042df76fa68032617165d12be125f853419acab7a03454353f76d4cd99d` |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | `76d1bdfa92cc2897b646d91238c29bc5907a74fe5f95424244e92a095ae5b82b` |
| `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | `457c4928155b151f8f49b0f8662c50309570e159b595672195de0f7cc21efe99` |

## Acceptance Criteria

1. Caller `policyResult: 'allow'` cannot reach an executor.
2. Native `BLOCK` and `ESCALATE` decisions stop before executor invocation.
3. Missing/throwing/malformed/trace-mismatched admission stops before executor.
4. Native `ALLOW` produces a trace-bound policy/evidence envelope and preserves
   downstream Model Gateway receipt behavior in a hermetic composition proof.
5. Both direct adapter and registered-tool paths are covered.
6. Focused, full MCP package, TypeScript build, governance, manifest, staging,
   and no-commit proofs pass with zero provider/live calls.

## Risk / Corrective Action

This is a security-sensitive runtime authority boundary. Do not preserve legacy
caller-policy compatibility by accepting a self-attested allow. If an additional
production path is required, return `BLOCKED_WITH_REASON`; do not widen scope.

## Decision / Baseline / Proposed Tranche

Decision: `PROCEED_WITH_RFR_R3`.

Baseline: RFR-R2 is closed bounded. F8 remains a verified local MCP execution
admission gap in existing owners.

Proposed tranche: one external no-commit worker implementation followed by
independent review, one reviewer-owned material commit, and a separate
continuity commit only after acceptance.

## Evidence / Verification

Worker evidence must identify exact source hashes, execution base, changed set,
staging state, focused/full/build results, boundary-reference reconciliation,
worker-return gate, file-size result, and zero external calls. Reviewer must
independently probe caller-policy injection, invalid native decisions, trace
binding, registered-tool composition, and executor call counts before acceptance.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | MCP server guard engine and execute adapter | server-owned admission before injected executor | focused and package tests | repository-local TypeScript only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | `cvf_model_gateway_execute` | MCP caller supplies intent/data only and cannot self-authorize | registered-tool and direct-adapter negative tests | native admission mandatory; no provider/live invocation | IMPLEMENTED |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_changed_corpus_registry_coverage.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; Agent Operation Trace labels; Public Export Disposition; worker-return shape |
| gateRunPurpose | confirm the paired R3 dispatch shape and evidence after source verification; not first discovery |
| claimBoundary | structural pass is not implementation or closure proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint; worker runs its own pre-execution resolver |

## Epistemic Process Block

### Expected Result / Prediction

The existing native MCP guard engine and injected executor seam should allow F8
to close without changing Model Gateway production code or making live calls.

### Evidence Comparison

Source inspection confirms the caller-policy bypass, the native engine owner,
the registered tool, and hermetic Model Gateway composition proof all exist in
the bounded owner set.

### Contradiction Or Gap Disposition

No owner gap was found. The contradiction is behavioral: an injected executor
is fail-closed when absent but trusts caller policy when present. R3 removes that
trust at the MCP boundary.

### Claim Update

R3 is authorized for construction and local proof only; F8 remains open until
independent review and material commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch; public sync remains forbidden.

## Claim Boundary

This baseline authorizes only bounded local RFR-R3 implementation and proof. It
does not authorize provider/live calls, credentials, deployment, public sync,
push, production, R4-R6, or worker commit.
