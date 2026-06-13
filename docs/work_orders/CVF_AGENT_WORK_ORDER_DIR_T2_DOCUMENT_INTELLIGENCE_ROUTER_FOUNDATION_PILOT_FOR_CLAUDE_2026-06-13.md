# CVF Agent Work Order - DIR-T2 Document Intelligence Router Foundation Pilot

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `30e6d174`

executionBaseHead: `30e6d174`

closureBaseHead: `639405b1`

sourceAuthority:
`docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

Predecessor tranche:
`docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`

## Purpose

Implement a bounded DIR-T2 foundation pilot harness for the deterministic
Document Intelligence Router. Claude must prove that the current DIR-T1 router
composes EXA-T2 scan-route outputs across a small synthetic metadata-only
fixture corpus while preserving scan ownership, authorization-gate boundaries,
and downstream use-case separation.

This work order is not a Document Translator implementation. Document
Translator is only a downstream use-case context for claim-boundary pressure.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator instructed Codex to audit and proceed with DIR-T2 as CVF foundation hardening, not use-case deepening | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | ACCEPT |
| DIR-T1 completion | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches fresh GC-018 and this work order |
| Worker | Claude | authors allowed-scope test harness and worker-return packet only |
| Reviewer / closer | Codex | reviews, fixes reviewer-owned issues, runs closure gates, commits |

## Intake Role Routing Decision

Intake summary: operator approved proceeding to DIR-T2 after confirming that
DIR-T2 must harden the CVF foundation and must not become Document Translator
implementation work.

Scope classification: bounded local deterministic pilot harness over synthetic
metadata fixtures plus one worker-return packet.

Risk sensitivity: medium governance risk because the tranche uses runtime
proof language, but risk is bounded by local deterministic execution only, no
provider/API/OCR/retrieval action, no external repo access, and no readiness
claim.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude acts as worker under `WORKER_MUST_NOT_COMMIT`;
Codex remains reviewer, closer, and committer.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if Claude needs real
documents, external Document Translator files, OCR, provider/API calls,
retrieval runtime, corpus ingestion, public-sync, session-state edits, or a
claim that exceeds local deterministic foundation pilot proof.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
5. `docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md`
6. `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`
7. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`
8. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
9. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py`
10. this work order

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=dir_t2_document_intelligence_router_foundation_pilot_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DIR-T2; next allowed move=Claude implements allowed-scope DIR-T2 local deterministic foundation pilot test harness under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=DT-CVF-T0, Policy_Local PL-S1, external Document Translator repo, OCR/provider/retrieval, corpus ingestion, public-sync, T12, readiness/cost/quality claims remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `30e6d174` | Codex | ACCEPT |
| executionBaseHead | `30e6d174` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| DIR-T0 contract matrix | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` at commit `082b02ff` | ACCEPT |
| DIR-T1 source and tests completion | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md` at commit `4bf991f3` | ACCEPT |
| DIR-T1 router source present | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | ACCEPT |
| DIR-T2 fresh GC-018 | `docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md` | ACCEPT |
| Sample corpus approval | synthetic metadata-only fixture corpus in this work order, no external files | ACCEPT |
| Runtime authorization | local deterministic Python tests only; no external service action | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: DIR route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 25 | `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR claim boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 27 | `CLAIM_BOUNDARY` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR authorization gate | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 35 | `AuthorizationGate` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR downstream capability | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 43 | `DownstreamCapability` | DIR-T1 router module | ACCEPT |
| EXISTS: scan-to-gate map | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 51 | `SCAN_ROUTE_TO_AUTHORIZATION_GATE` | DIR-T1 router module | ACCEPT |
| EXISTS: document profile | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 68 | `DocumentProfile` | DIR-T1 router module | ACCEPT |
| EXISTS: structure signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 86 | `DocumentStructureSignals` | DIR-T1 router module | ACCEPT |
| EXISTS: route decision | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 105 | `DocumentIntelligenceRouteDecision` | DIR-T1 router module | ACCEPT |
| EXISTS: route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 139 | `decide_document_intelligence_route` | DIR-T1 router module | ACCEPT |
| EXISTS: EXA-T2 scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan route module | ACCEPT |
| EXISTS: EXA-T2 scan disposition | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan route module | ACCEPT |
| EXISTS: EXA-T2 scan signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 40 | `DocumentScanSignals` | EXA-T2 scan route module | ACCEPT |
| EXISTS: EXA-T2 scan function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 71 | `decide_scan_route` | EXA-T2 scan route module | ACCEPT |
| EXISTS: DIR-T2 roadmap gate | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 368-388 | `DIR-T2` | parent roadmap | ACCEPT |

## New Doc-Only Fields

No new doc-only runtime fields are authorized. Synthetic fixture IDs such as
`DIR-T2-S1` through `DIR-T2-S4` are test fixture identifiers only.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Roadmap evidence | Work-order section | Verification |
| --- | --- | --- | --- |
| DIR-T2 is a bounded pilot | roadmap lines 368-388 | Purpose; Runtime Authorization | worker-return evidence |
| operator supplies bounded sample corpus | roadmap line 375 | Operator-Approved Sample Corpus Boundary | fixture tests |
| runtime scope explicitly authorized | roadmap line 376 | Runtime Authorization | proof manifest |
| keep Document Translator separate | roadmap line 388 | Forbidden Path Manifest | worker-return negative evidence |
| no readiness/cost/quality claim | roadmap claim boundary | Claim Boundary | worker-return boundary |

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures without asking the operator.
Claude must ask or return `BLOCKED_SCOPE_EXPANSION` only if the repair would
touch forbidden paths, alter claim boundary, require real documents, run OCR,
call a provider/API, mutate retrieval/corpus/session state, use public-sync, or
make readiness/cost/quality claims.

## Pre-Flight Checks

Before implementation, Claude must:

1. Read every Required First Reads path.
2. Confirm `git status --short` and record pre-existing dirty paths.
3. Confirm `Thong_tin.md` remains operator-owned and outside this work order.
4. Confirm the external Document Translator tree is not read, listed, hashed,
   modified, or imported.
5. Run the dispatch package checks only if Claude changes this work order.

## Single-Agent Multi-Role Control Block

| Control item | Requirement | Disposition |
| --- | --- | --- |
| Role separation ledger | Codex=orchestrator/reviewer/closer; Claude=worker; no role-by-role closure authority is delegated to the worker | ACCEPT |
| Evidence basis independent of memory | closure must rely on git diff, source files, tests, reviewer-fast, pre-closure, and pre-push gate evidence, not memory-only claims | ACCEPT |
| Self-review boundary | Claude worker return is not independent review and no independent review is claimed until Codex reviews | ACCEPT |
| Escalation conditions | stop condition is any need for external files, OCR/provider/API, retrieval, session mutation, public-sync, or widened claim | ACCEPT |
| Gate sequence | Codex dispatch uses pre-dispatch; Claude worker uses required proofs; Codex review uses reviewer-fast, pre-closure, and pre-push as applicable | ACCEPT |
| Raw memory boundary | rawMemoryReleased=false | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`

recomputeReason: DIR-T2 must produce fresh local deterministic pilot evidence over the bounded fixture corpus

unicodePathHandling: literal UTF-8-safe repository paths only

extractedTextAuthority: N/A with reason

Evidence reuse is limited to source-verified contracts and current runtime
source. The synthetic fixture corpus must not contain extracted text.

## Allowed Implementation Scope

Claude may create:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py`
- `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md`

Claude may update this work order only to add worker-return evidence if needed.

## Allowed / Forbidden Scope

Allowed scope:

- create the focused DIR-T2 pilot test file;
- create the DIR-T2 worker-return packet;
- run local deterministic Python tests and governance checkers listed in the
  Required Proof Manifest.
- reviewer-owned closure may update this work order, the paired GC-018,
  `docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md`,
  `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`,
  `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`,
  `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md`,
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py`,
  `docs/corpus-intelligence/registry/entries/dir-t2-document-intelligence-router-foundation-pilot-tests.json`,
  and `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- reviewer gates may observe pre-existing operator-owned `Thong_tin.md` as an
  untouched untracked file; it is not a work artifact and must not be committed.

Forbidden scope:

- external Document Translator source access;
- Policy_Local mutation;
- OCR/provider/API/service execution;
- retrieval runtime or corpus ingestion;
- session-state, handoff, or front-door mutation by Claude;
- public-sync;
- readiness, cost, quality, hosted, production, or public claims.

## Required Artifact Manifest

| Artifact | Required content | Owner |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py` | synthetic metadata-only fixture corpus and focused deterministic pilot tests | Claude |
| `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md` | worker return, evidence, findings, and claim boundary | Claude |

## Forbidden Path Manifest

| Path / Pattern | Boundary |
| --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator/**` | do not read, list, hash, modify, or import |
| `D:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF-public-sync/**` | public-sync not authorized |
| `Policy_Local/**` | Policy_Local mutation not authorized |
| `CVF_SESSION/**` | worker session-state mutation not authorized |
| `CVF_SESSION_MEMORY.md` | worker front-door mutation not authorized |
| `AGENT_HANDOFF*.md` | worker handoff mutation not authorized |
| `.env*` | secret reads not authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Evidence owner |
| --- | --- | --- |
| external Document Translator tree | NOT_AUTHORIZED_FOR_WORKER_INSPECTION | Claude worker return must not cite file listings or hashes |
| public-sync clone | NOT_AUTHORIZED_FOR_WORKER_INSPECTION | Claude worker return must not cite public-sync actions |
| session-state files | NOT_AUTHORIZED_FOR_WORKER_MUTATION | Codex reviewer owns any session sync |

## Work-Order Fulfillment Manifest

Claude must report each Required Artifact Manifest row as created, updated, or
blocked. Claude must also report each Forbidden Path Manifest row as untouched
or blocked.

## Write Ownership

| Path | Owner | Boundary |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py` | Claude | create/update allowed |
| `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md` | Claude | create/update allowed |
| `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` | Codex | reviewer-owned closure only |
| `CVF_SESSION/**` | Codex | reviewer-owned session sync only |
| `CVF_SESSION_MEMORY.md` | Codex | reviewer-owned session sync only |
| `AGENT_HANDOFF*.md` | Codex | reviewer-owned session sync only |

## Required Proof Manifest Atomic Literal Discipline

Each Required Proof Manifest row contains one atomic command or one atomic
literal check. Do not combine multiple commands in a single row.

## Required Proof Manifest

| Proof item | Command or literal | Expected result |
| --- | --- | --- |
| focused DIR-T2 pilot tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py -q` | PASS |
| existing DIR-T1 router tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py -q` | PASS |
| DIR overlap checker | `python governance/compat/check_dir_disposition_no_scan_overlap.py` | PASS |
| worker worktree state | `git status --short` | shows only Claude-authored allowed-scope artifacts plus pre-existing `Thong_tin.md` if still present |

## Implementation Requirements

1. Build the DIR-T2 pilot as a test-only harness in the allowed test file.
2. Use synthetic metadata-only fixtures, not real document files.
3. Cover all current EXA-T2 `ScanRouteDisposition` values through supplied
   `ScanRouteDecision` objects or `DocumentScanSignals` fixtures.
4. Assert the derived `AuthorizationGate`, `operator_action`, and
   `downstream_eligibility` for each sample.
5. Assert no fixture or decision exposes raw text, raw bytes, OCR output,
   provider response, or Document Translator file paths.
6. Assert downstream capability values remain foundation-level and do not add
   use-case names such as translation or policy-specific route values.
7. Preserve DIR-T1 source unchanged unless an allowed-scope test exposes a
   deterministic bug that cannot be tested around. If source change becomes
   necessary, return `BLOCKED_SCOPE_EXPANSION`.

## Execution Plan

1. Build a synthetic fixture helper in the focused DIR-T2 test file.
2. Add four samples covering the current EXA-T2 scan dispositions.
3. Route each sample through `decide_document_intelligence_route`.
4. Assert gate, action, eligibility, digest, version, and claim-boundary
   invariants.
5. Assert no sample contains raw content or external use-case path strings.
6. Run the Required Proof Manifest commands.
7. Create the worker-return packet with command summaries and findings.

## Evidence Requirements

Claude's worker-return packet must include:

- `WORKER_MUST_NOT_COMMIT observed`;
- `rawMemoryReleased=false`;
- changed-file list from `git status --short`;
- proof command summaries;
- sample corpus ledger with four synthetic sample IDs;
- explicit statement that no external Document Translator tree, public-sync,
  OCR/provider/API, retrieval runtime, corpus ingestion, or session-state
  mutation was used;
- Finding-To-Governance Learning Disposition, using `N/A_WITH_REASON` only if
  no reusable finding appears.

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| Four synthetic samples cover all scan dispositions | pilot test assertions |
| DIR gates remain disjoint from scan dispositions | overlap checker PASS |
| Document Translator remains downstream context only | worker-return boundary |
| No external files or services are used | worker-return negative evidence |
| Worker does not commit | `git status --short` and return packet |

## Reviewer Closure Conversion

Codex must treat Claude's worker return as pending evidence, not closure.
Codex owns the completion review, any session-state sync, final gates, and
commit.

## Review Gate

Codex reviewer must verify:

- Claude honored `WORKER_MUST_NOT_COMMIT`;
- all Required Artifact Manifest rows are present or explicitly blocked;
- Required Proof Manifest commands pass or have safe diagnostics;
- no forbidden path or external runtime was used;
- claim boundary remains foundation-only.

## Closure Checklist

| Item | Required closure disposition |
| --- | --- |
| Worker return reviewed | PASS, BLOCKED, or N/A with reason |
| Required proofs reviewed | PASS, BLOCKED, or N/A with reason |
| Forbidden scope checked | PASS, BLOCKED, or N/A with reason |
| Finding-To-Governance disposition reviewed | PASS, BLOCKED, or N/A with reason |
| Session continuity updated by reviewer | PASS, BLOCKED, or N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | `Status: DIR_T2_CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline state | `docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 entry added for the DIR-T2 pilot test harness; checker PASS | PASS |
| Registry Markdown | BLOCKED with reason | no Markdown quick-lookup row is required for this generated registry-source update | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source tree was read or hashed | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop, route, retrieval, or interlock mutation | N/A with reason |
| Worker return artifact | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md` | `Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED` then accepted | PASS |
| Session continuity | active state/front door/handoff | reviewer-owned dedicated session-sync follows material closure commit | N/A with reason |

## Operator Checkpoint

No operator checkpoint is required for the synthetic local deterministic
fixture pilot. Operator checkpoint is required if Claude or Codex needs real
documents, external Document Translator access, OCR/provider/API execution,
retrieval runtime, corpus ingestion, public-sync, or readiness/cost/quality
claims.

## Return-To-Orchestrator Conditions

Return `BLOCKED_SCOPE_EXPANSION` if any required result needs:

- real document files;
- external Document Translator source access;
- OCR/provider/API execution;
- retrieval runtime or corpus ingestion;
- session-state or handoff mutation by Claude;
- public-sync;
- readiness, quality, cost, hosted, production, or public claim.

## Claim Boundary

This work order authorizes local deterministic DIR foundation pilot evidence
only. It does not claim document understanding, translation readiness,
Document Translator readiness, Policy_Local readiness, OCR quality, provider
behavior, retrieval quality, hosted readiness, production readiness, public
readiness, memory reinjection, high-risk promotion, or autonomous mutation.

rawMemoryReleased=false
