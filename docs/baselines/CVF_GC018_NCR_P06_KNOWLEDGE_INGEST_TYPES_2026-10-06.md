# NCR P06 - Knowledge ingest input types

Memory class: FULL_RECORD

docType: baseline

Status: LOCAL_IMPLEMENTED_VERIFIED_BOUNDED

Date: 2026-10-06

executionBaseHead: `45b1a48d4f97e221adcd3e3bd21610b54d6f5f5a`

## Purpose

Continue the wider NCR backlog with a bounded input-integrity repair for the
existing project-knowledge consumer. Reject malformed JSON values before an
ephemeral collection is registered; do not coerce unsupported values into text.

## Source Verification Block

| Source | Disposition | Finding |
|---|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.ts | ACCEPT | Parsed root/chunks are cast without object checks; null can throw; keywords elements and collectionName type are not checked |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/knowledge/ingest/route.test.ts | ACCEPT | Existing tests cover valid ingest/query and one malformed chunk, not null/mixed-type inputs |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-store.ts, KnowledgeChunk and registerEphemeral | ACCEPT | Existing types require string id/content/name and string-array keywords; registration follows validation and is process-local for this route |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/knowledge-retrieval.ts, scoreChunk/queryKnowledgeChunks | ACCEPT | Retrieval uses admitted collection/chunk values; this repair concerns type integrity, not semantic trust or relevance |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/knowledge/page.tsx, handleIngest | ACCEPT | Current UI submits string collectionName or omits it and forwards parsed chunks |
| docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md, P06/W02-C | ACCEPT | Existing input type validation owner; no separate knowledge pipeline is created |

## Decision / Scope

Operator requested continuation after the previous P06 body-read delta. Local
owns this reversible source-maintenance selection, implementation and technical
disposition. Prior eighteen material paths remain outside this repair except
the existing NCR roadmap selection paragraph. No delegation or dispatch occurs.

Two product paths: the ingest route and its existing route.test.ts. Also write
this baseline and update the existing roadmap paragraph, keeping its line budget.
Reject non-object roots, non-object chunks, non-string keyword elements and
non-string non-null collectionName. Preserve the existing absent/null name
fallback to collectionId and accepted string/empty-array behavior.
Validate the complete batch before registerEphemeral; an invalid replacement
must not change the prior collection or add a registration audit event.

Keep auth, raw signing, storage, retrieval, chunk projection and response shape
for valid requests. No new schema/checker/helper, size policy, persistence,
org/team rights, SOT3 provenance policy or provider integration is authorized.
Q001/Q004, send/B2, P11, deploy and public checkpoints retain their dispositions.

## Evidence / Verification Plan

Use signed synthetic requests and the test-mode in-process store. Counterexample
cases cover null roots/chunks, keywords containing JSON non-string values,
wrong collection names and a mixed valid/invalid replacement batch. Assert 400
and zero registration for invalid input, preserving the prior collection/audit.
Retain positive ingest/query coverage and absent/null name compatibility.
Run only the affected route suite plus existing ingest/query regression, then
typecheck, targeted lint and applicable static gates. These deterministic tests
do not assert AI governance or real service/provider behavior.

## Verification Results

Preflight passed before product edits (preflight.log, 8.69s).
Red: ten added cases failed on the old route, nineteen passed (red.log, 9.73s).
Failures were null-root/chunk exceptions, acceptance of four non-string keyword
values, three non-string collection names, and exception on the mixed batch.
The route now checks roots/chunks and every keyword element before registration.
Non-string non-null names return 400; absent/null fallback is retained.

Green: 36/36 across route.test.ts and the existing ingest/query delta regression
passed (green.log, 10.40s). The route file has twenty added cases; controls cover
rejected primitive/array shapes and source-preserving valid fallback. The mixed
replacement test confirms the prior collection and audit are retained. Typecheck
and targeted lint exit 0; git diff --check on the product pair passed.
Evidence directory: .cvf/runtime/ncr-p06-knowledge-types-20261006/.
Final applicable static confirmation is recorded in final-static.log.
Earlier spec-input/body-read tests are consumed, not repeated for this delta.
Provider requests for this repair: zero. These are deterministic local input
and in-process-store checks, not AI governance or real deployment proof.

## Execute Payload Shape Follow-Up - 2026-10-06

Fresh operator `ok.next` admits one Local reversible P06 payload-shape batch.
Source ACCEPT: execute/route.ts admits arrays as object roots and applies
Object.entries/String to inputs before checking shape; ExecutionRequest in
lib/ai/types.ts owns the existing core input and selector types. Named consumer
inspection only. No new public schema, checker, provider or spec-generation job.

Exact follow-up products under EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src:
lib/execute-request-validation.ts, app/api/execute/route.ts, route.test.ts and
route.request-validation.test.ts (new tests rotated at existing size threshold).
This baseline plus two replaced roadmap lines record selection/evidence. Preserve
prior work, bounded body reader and auth ordering; raw signed body is unchanged.
After existing authentication and before normalization, reject root/inputs arrays,
non-object inputs, nested input values and wrong primitive types on the existing
core text/selectors, boolean skill-preflight flag and string-list fields. Existing
scalar input normalization (string/number/boolean/null) remains compatible.
Optional null selectors retain existing absence behavior; enum/business/authority
decisions and nested memory/commit/chain owners remain downstream. This is not
complete ExecutionRequest schema validation or authorization of request claims.

Return 400 with existing request_validation/invalid_input diagnostic; invalid
shape cannot reach enforcement, approval binding, store or provider call. Verify
malformed cases and scalar/VI controls through the actual handler using its
existing synthetic adapter fixture. No AI governance behavior is asserted.
Local implements/reviews; decision owner=Local; current parked checkpoints stay.
No live test is needed to establish local pre-provider type rejection.

Follow-up results: preflight PASS 85/85 before product edits, 16.49s
(preflight.log); ADIF resolver zero candidates, no truncation (adif.json).
Red run: 18 new malformed cases failed against old source; 37 controls passed,
19.90s (red.log). Green: execute plus existing knowledge/language route suites
PASS 72/72, 25.22s (tests.log), including four new root controls and the scalar/VI
positive control. Existing signature, body-limit, output, role and approval cases
remain in the handler suite. No provider calls: synthetic mocked execute fixture,
not live AI governance or semantic fidelity evidence. Evidence directory:
.cvf/runtime/ncr-p06-execute-types-20261006/. Typecheck/lint and final static
confirmation use typecheck.log, lint.log and final-static.log in that directory.
Expected/actual follow-up manifest is the four product paths above, this baseline
and two replaced roadmap lines; prior delta retained. Initial knowledge-only trace
below remains historical evidence; no commit/public/deploy or new checkpoint.

## Current Runtime Freshness Verification

Local 2026-10-06 source inspection at HEAD 45b1a48d4 plus disclosed worktree:
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts now calls
validateExecuteRequestShape after existing signature/session auth and before
Object.entries/String normalization; lib/execute-request-validation.ts supplies
the bounded shape checks. Earlier counterexamples use this same named handler's
old source, not historical runtime inference. No repository-wide absence claim.
Initial final-static.log failed size/readout requirements: rotate new payload
tests into a dedicated handler suite and add this freshness binding. Preserve
the failed gate receipt; rerun after these named repairs. Original 72/72 result
remains evidence before test rotation. No product behavior changed in rotation.
Rotated suites: 72/72 PASS in four files, 34.38s (rotated-tests.log).
Rotated typecheck exit 0 (rotated-typecheck.log); removed one unused copied test
helper after lint. Final targeted lint is final-lint.log. git diff --check PASS.
Final static confirmation follows in final-static-repaired.log; no additional
model sampling or live run is needed to disposition these local shape checks.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | Source/Decision/Evidence/Claim Boundary headings; four read-ahead fields; complete trace labels; Resolver query; Returned defects; Public Export Disposition |
| gateRunPurpose | Confirm authored scope and verification evidence; not first discovery of packet shape |
| claimBoundary | Local packet/static evidence; not runtime governance or release proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED. Zero candidates and no truncation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local implementer/reviewer |
| Provider or surface | Local workspace |
| Session or invocation | NCR-P06 knowledge ingest types, 2026-10-06 |
| Working directory | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | Source reads, apply_patch, focused Vitest, typecheck/lint, static autorun |
| Target paths | Two product paths in Source Verification Block, this baseline, existing NCR roadmap |
| Allowed scope source | Operator continuation request and existing P06 backlog |
| Before status evidence | Eighteen prior modified/untracked material paths; ingest route/test initially clean |
| After status evidence | Local type repair complete; 36/36 focused tests, typecheck/lint and product whitespace checks passed |
| Diff evidence | git diff for ingest route/test and roadmap; baseline untracked |
| Approval boundary | Local reversible type-validation maintenance; effects not admitted |
| Claim boundary | Existing ingest JSON type contract, not semantic trust or AI behavior |
| Agent type | Local implementer/reviewer |
| Invocation ID | NCR-P06-KNOWLEDGE-TYPES-20261006 |
| Expected manifest | Two product paths, baseline, roadmap selection paragraph |
| Actual changed set | Two product paths, this baseline and existing roadmap selection paragraph; prior delta retained |
| Manifest delta | No additional tranche paths authorized |

## Claim Boundary

This repair is type integrity at one existing knowledge ingress. It does not
establish source trust, data ownership/isolation, complete provenance, resource
caps, durable knowledge acceptance or AI governance. Tests use synthetic data
only. No release, real-provider operation, public/deploy or commit is requested.
Local repair is complete in this manifest; material remains uncommitted. Next
selection returns to the wider roadmap, not automatic expansion across routes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - local maintenance and bounded test evidence.
