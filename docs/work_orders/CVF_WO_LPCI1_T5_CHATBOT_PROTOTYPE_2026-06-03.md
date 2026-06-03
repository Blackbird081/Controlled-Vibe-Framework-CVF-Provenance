# CVF Work Order - LPCI1-T5 Chatbot Prototype

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `24f28870`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: `c7916c35`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Implement the LPCI1 chatbot prototype: a local Next.js UI page (`/lpci`) and
supporting API routes (`POST /api/lpci/query`, `POST /api/lpci/intake`,
`GET /api/lpci/corpus/:corpusId/status`) that satisfy the T4 response boundary
contract (C1–C9), emit a valid `AuditReceipt` per query, and wire the five-stage
T3 filter pipeline into a working prototype.

This is the first runtime tranche for LPCI1. All non-implementation architectural
decisions were made in T1–T4. T5 converts those specifications into executable
prototype code only — no production corpus, no live vector DB, no hosted
deployment, no legal advice claims.

---

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| LPCI1 GC-018 | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | ACCEPT |
| LPCI1 MVP roadmap (T5 row) | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | ACCEPT |
| T4 retrieval boundary spec | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | ACCEPT |
| T3 search/filter index spec | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | ACCEPT |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT |
| T1 architecture | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | ACCEPT |
| Commit choreography standard | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | ACCEPT |

---

## Roadmap-To-Work-Order Trace Matrix

| LPCI1 MVP roadmap requirement | LPCI1-T5 instruction |
| --- | --- |
| T5 — Chatbot Prototype: local UI/API with operator-provided LLM API key | implement `POST /api/lpci/query` with `LPCI_LLM_API_KEY` env var; `NO_PROVIDER_CONFIGURED` receipt when key absent |
| T5 — citations, answer class, audit receipt | satisfy T4 response boundary contract C1–C9; emit AuditReceipt per query |
| T5 dependency: T4 retrieval reviewed | verified — T4 CLOSED_PASS_BOUNDED at commit `5143267f` |
| No runtime before T1 gate | T1 architecture closed; T2–T4 all CLOSED_PASS_BOUNDED; gate satisfied |
| CI2 checkers pass for all LPCI packets | NR-04/NR-05/NR-11 autorun gates; T5 must not create corpus packets outside CI2 enforcement scope |

---

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch after T4 CLOSED_PASS_BOUNDED; confirm no archive hygiene backlog | no implementation |
| Worker | implement prototype routes, UI page, retrieval logic, AuditReceipt emission | no production corpus; no live vector; no legal advice claims |
| Reviewer | verify T4 response boundary contract C1–C9 satisfied; reject scope bleed | reject any route, component, or test outside allowed scope |

---

## Dependency Gate

Dependency satisfied. LPCI1-T4 closed through final handoff commit `24f28870`.

Release evidence:

- T4 completion review: `docs/reviews/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_COMPLETION_2026-06-03.md` — Status: CLOSED_PASS_BOUNDED at commit `5143267f`
- T4 work order: `docs/work_orders/CVF_WO_LPCI1_T4_RETRIEVAL_BOUNDARY_2026-06-03.md` — Status: CLOSED_PASS_BOUNDED
- T4 final session/handoff sync: `24f28870`

---

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| API route sketch `POST /api/lpci/query` | EXISTS | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Local API Sketch` | `POST /api/lpci/query` | T1 Architecture API/UI Surface Sketch | ACCEPT |
| API route sketch `POST /api/lpci/intake` | EXISTS | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Local API Sketch` | `POST /api/lpci/intake` | T1 Architecture API/UI Surface Sketch | ACCEPT |
| API route sketch `GET /api/lpci/corpus/:corpusId/status` | EXISTS | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Local API Sketch` | `GET /api/lpci/corpus/:corpusId/status` | T1 Architecture API/UI Surface Sketch | ACCEPT |
| UI sketch `/lpci` page | EXISTS | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Local UI Sketch` | `/lpci` | T1 Architecture API/UI Surface Sketch | ACCEPT |
| RetrievalReceipt schema fields | EXISTS | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `## RetrievalReceipt Schema` | `matched_paths` | T4 Retrieval Boundary Spec | ACCEPT |
| AuditReceipt schema fields | EXISTS | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `## AuditReceipt Schema` | `auditId` | T4 AuditReceipt Schema | ACCEPT |
| Response boundary contract C1–C9 | EXISTS | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `## Response Boundary Contract` | `C1` | T4 Response Boundary Contract | ACCEPT |
| answerClass precedence rule | EXISTS | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `### answerClass Precedence Rule` | `answerClass` | T4 Retrieval Boundary Spec | ACCEPT |
| Five-stage filter pipeline | EXISTS | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | `Stage 1` through `Stage 5` | `Stage 4` | T3 Search Filter Index Spec | ACCEPT |
| Negative receipt types | EXISTS | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Negative Receipt section | `NO_RESULTS` | T3 Search Filter Index Spec | ACCEPT |
| Commit choreography standard | EXISTS | `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | `## CI2-T2 Binding` | `CI2-T2 Binding` | Tranche Commit Choreography Standard | ACCEPT |
| Next.js app directory | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/` | directory exists | `src/app` | CVF Web App | ACCEPT |
| Existing API route pattern | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 40 | `POST` | execute API route | ACCEPT |

---

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/intake/route.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/corpus/[corpusId]/status/route.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.test.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.test.ts` | CREATE | Worker |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.test.ts` | CREATE | Worker |
| `docs/reviews/CVF_LPCI1_T5_CHATBOT_PROTOTYPE_COMPLETION_2026-06-03.md` | CREATE | Worker |

---

## Allowed Scope

- Create the three API routes under `src/app/api/lpci/`;
- Create the `/lpci` dashboard page under `src/app/(dashboard)/lpci/`;
- Create supporting library modules under `src/lib/lpci/`:
  - `types.ts` — TypeScript types for RetrievalReceipt, AuditReceipt, IntakeRecord, FilterPipeline;
  - `filter-pipeline.ts` — five-stage filter execution (Stages 1–5 per T3 spec);
  - `retrieval.ts` — Phase 1 + Phase 2 pipeline, answerClass precedence, conflict/freshness detection;
  - `audit-receipt.ts` — AuditReceipt construction and SHA-256 model_response_hash;
- Create focused unit tests for retrieval, filter-pipeline, audit-receipt, and query route;
- Repair allowed-scope type/lint/test defects within this batch.

Forbidden scope:

- vector database schema, embedding pipeline, or semantic search index implementation;
- live provider API calls (LLM, embedding, search engine) without operator-supplied key;
- production corpus registration or intake beyond the GOVERNANCE_PILOT corpus from CI2-T4;
- legal advice claims, production readiness claims, public SaaS;
- unrelated governance checker rewrites or archive cleanup;
- public-sync;
- deployment configuration beyond `localhost:3000`.

**Operator key rule**: if the prototype integrates a configurable LLM provider call, the
API key must come from environment variable (`LPCI_LLM_API_KEY`) provided by the operator
at runtime. CVF does not supply or store LLM keys. If no key is present, the query route
must return a `NO_PROVIDER_CONFIGURED` receipt, not an error stack trace.

---

## Required First Reads

1. `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` — response boundary contract C1–C9, AuditReceipt schema, RetrievalReceipt schema.
2. `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` — five-stage filter pipeline; negative receipt types.
3. `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` — API/UI surface sketch; retrieval flow pseudocode.
4. `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` — answerClass criteria; dispositionAlias decision matrix.
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — existing API route pattern (auth, response shape).
6. `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` — commit sequence; base anchor rules.

---

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| Capture fresh execution base | `git rev-parse --short HEAD` | record as `executionBaseHead` in worker handoff |
| T4 spec exists | `Test-Path docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | true |
| T4 work order closed | check Status field in `docs/work_orders/CVF_WO_LPCI1_T4_RETRIEVAL_BOUNDARY_2026-06-03.md` | CLOSED_PASS_BOUNDED |
| Archive hygiene clear | `PYTHONUTF8=1 python governance/compat/check_active_archive_hygiene.py --enforce 2>&1 \| tail -5` | exit 0; if backlog exists, run archive script as separate pre-session commit before T5 work |
| Existing web build passes | `npm run build` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` | exit 0 |
| Existing tests pass | `npm run test:run` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` | exit 0 |

---

## Execution Plan

1. Read all six required-first-read documents.
2. Verify pre-flight checks; record `executionBaseHead`.
3. Create `src/lib/lpci/types.ts` — TypeScript interfaces for all T4/T3 schemas.
4. Create `src/lib/lpci/filter-pipeline.ts` — five-stage filter; returns ranked result set or negative receipt.
5. Create `src/lib/lpci/retrieval.ts` — Phase 1 (filter-pipeline), Phase 2 (answer assembly, answerClass precedence, conflict/freshness detection), negative receipt passthrough.
6. Create `src/lib/lpci/audit-receipt.ts` — `buildAuditReceipt()` function; SHA-256 of model response.
7. Create three API routes; implement response boundary contract; `NO_PROVIDER_CONFIGURED` receipt when key absent.
8. Create `/lpci` dashboard page per T1 UI sketch: corpus selector, query input, response panel with answer boundary badge, freshness/conflict warnings, AuditReceipt export.
9. Create focused unit tests for each lib module and the query route.
10. Run `npm run test:run`, `npm run lint`, `npm run build`; fix defects.
11. Run component-level gate commands; do not commit (WORKER_MUST_NOT_COMMIT).

---

## Execution Instructions

### API Routes

**`POST /api/lpci/query`**

```
body: { query: string; corpusId: string; filters?: FilterParams }
response (success): AuditReceipt
response (no provider): { receiptType: "NO_PROVIDER_CONFIGURED"; query: string }
response (phase1 negative): { receiptType: "NO_RESULTS" | "FILTERED_OUT" | "ESCALATED"; query: string }
```

Steps:
1. Run five-stage filter pipeline (Phase 1) against the registered corpus for `corpusId`.
2. If Phase 1 returns a negative receipt, return it directly; do not invoke LLM (C9).
3. Compute `RetrievalReceipt` with most restrictive `answer_class` (precedence rule).
4. If `answer_class = ESCALATE_OR_ABSTAIN`, return abstention message; do not invoke LLM (C6).
5. If `LPCI_LLM_API_KEY` is absent, return `NO_PROVIDER_CONFIGURED` receipt; do not error.
6. Invoke LLM with explicit answer boundary instruction encoding Rules A1–A4.
7. Build and emit `AuditReceipt`; populate `model_response_hash` with SHA-256 of the emitted LLM response, abstention response, or negative receipt payload (C8).

**`POST /api/lpci/intake`**

```
body: { corpusRoot: string; manifestPath: string }
response: { rowCount: number; gaps: string[]; sourceHashSummary: string }
```

Steps:
1. Verify `corpusRoot` in GC-051 registry (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`); abort with `NOT_REGISTERED` if absent.
2. Load and parse manifest JSON.
3. For each entry: compute SHA-256 hash or accept manifest proxy per NR-04; compute `normalizedPath` per NR-05; validate `documentType` enum.
4. Return `IntakeReport`; do not write a permanent classification ledger in this route (T2 scope).

**`GET /api/lpci/corpus/:corpusId/status`**

```
response: { registered: boolean; classificationStatus: string; rowCount: number }
```

Reads GC-051 registry only. Does not perform new scan.

### Library Modules

**`filter-pipeline.ts`** — implement Stages 1–5 per T3 spec exactly:
- Stage 4 (answerClass post-filter) is mandatory and non-overridable.
- Return typed negative receipts (`NO_RESULTS`, `FILTERED_OUT`, `ESCALATED`) from Stages 1–4.

**`retrieval.ts`** — implement Phase 1/Phase 2 boundary per T4 spec:
- Phase 2 is invoked only when Phase 1 returns a non-empty result set with ≥1 non-ESCALATE record.
- `answer_class` = most restrictive in result set (T4 precedence rule).
- Set `freshness_flag` and `conflict_flag` per T4 freshness and conflict protocol.
- Conflict resolution is by `authorityLevel` and `effectiveDate` fields only — no LLM content reasoning.

**`audit-receipt.ts`** — `buildAuditReceipt()` must populate all required fields; `model_response_hash` must be SHA-256 hex of the emitted LLM response, abstention response, or negative receipt payload; `auditId` must be a UUIDv4; `response_boundary_class` must be one of `ANSWER_EMITTED`, `ABSTAINED`, `ESCALATED`, `NEGATIVE_RECEIPT`.

### UI Page (`/lpci`)

Implement per T1 UI sketch:
- Corpus selector dropdown (registered corpora from GC-051 registry only).
- Query input with submit.
- Response panel: retrieved sources (normalizedPath, documentType, effectiveDate), answer boundary badge, freshness/conflict warnings, AuditReceipt JSON export button.
- No corpus upload or admin intake UI in this page (that is `/lpci/admin/intake` scope — implement only if line count permits within GC-023 limits).

### Response Boundary Contract Enforcement (C1–C9)

Every code path in `POST /api/lpci/query` must satisfy:

| Obligation | Implementation rule |
| --- | --- |
| C1 — Citation-first | every non-abstention LLM answer boundary instruction must require ≥1 `normalizedPath` and `effectiveDate` in response |
| C2 — answerClass enforcement | LLM system prompt must contain explicit per-answerClass instruction from T4 Rule A1 |
| C3 — No legal advice | LLM system prompt must contain explicit no-legal-advice constraint from T4 Rule A4 |
| C4 — Freshness warning | if `freshness_flag = true`, append freshness warning to LLM instruction per T4 Rule A2 |
| C5 — Conflict notice | if `conflict_flag = true`, inject conflict notice into LLM instruction per T4 Rule A3 |
| C6 — Abstention | if `answer_class = ESCALATE_OR_ABSTAIN`, skip LLM; return abstention message only |
| C7 — AuditReceipt | every query execution (including negative receipts and abstentions) must emit AuditReceipt |
| C8 — model_response_hash | SHA-256 of LLM response or negative receipt payload; never null |
| C9 — Phase 1 passthrough | Phase 1 negative receipt returned unchanged; Phase 2 not invoked |

---

## Commit Choreography / Reviewer Closure

LPCI1-T5 inherits
`docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`.

Worker obligations:

- capture a fresh `executionBaseHead` before any edits;
- run archive hygiene check (`check_active_archive_hygiene.py --enforce`) before implementation;
- keep implementation inside allowed scope only;
- do not commit (WORKER_MUST_NOT_COMMIT);
- run `npm run test:run && npm run lint && npm run build` in cvf-web; fix failures before returning;
- do not claim `pre-closure` PASS on pending working-tree artifacts;
- return any archive drift, stale session state, or unrelated governance issues to orchestrator.

Reviewer / committer obligations:

- capture a fresh `closureBaseHead` immediately before committing;
- commit implementation artifacts separately from closure metadata and session sync;
- stage a Core Guard Self-Protection Authorization doc in the same commit if any protected governance or session paths are changed;
- run committed-range pre-closure gates with `--base <closureBaseHead> --head HEAD`;
- session sync and handoff sync in dedicated follow-on commits.

---

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Three API routes implemented | query, intake, corpus status routes exist and return typed responses |
| `/lpci` page implemented | corpus selector, query input, response panel with badge + warnings + AuditReceipt export |
| T4 response boundary C1–C9 satisfied | every obligation enforced in query route code |
| AuditReceipt emitted per query | all fields populated per T4 schema; `model_response_hash` never null |
| Five-stage filter pipeline | Stages 1–5 implemented; Stage 4 non-overridable |
| Phase 1 / Phase 2 boundary | Phase 2 not invoked when Phase 1 returns negative receipt |
| `NO_PROVIDER_CONFIGURED` receipt | returned when `LPCI_LLM_API_KEY` absent; no error stack trace |
| Unit tests pass | retrieval, filter-pipeline, audit-receipt, query route tests all pass |
| `npm run lint` clean | zero ESLint warnings/errors |
| `npm run build` passes | TypeScript compilation and Next.js build exit 0 |
| No vector DB, embedding, or live corpus | none created or referenced |
| No legal advice claim | no response text or comment claims legal advice quality |

---

## Evidence Requirements

- `npm run test:run` output for all new tests.
- `npm run lint` output (zero warnings).
- `npm run build` exit 0.
- Sample query execution trace (dry-run with `NO_PROVIDER_CONFIGURED` receipt) showing AuditReceipt fields.

---

## Required Gates

```powershell
# In EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/:
npm run test:run
npm run lint
npm run build

# Governance gates (repo root):
PYTHONUTF8=1 python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
PYTHONUTF8=1 python governance/compat/check_core_guard_self_protection.py --base <executionBaseHead> --head HEAD --enforce
PYTHONUTF8=1 python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD

# Reviewer/committer only, after artifacts are committed:
PYTHONUTF8=1 python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <closureBaseHead> --head HEAD
PYTHONUTF8=1 python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
git diff --check
git status --short
```

---

## Review Gate

Reviewer must verify:

1. T4 response boundary C1–C9 are satisfied in query route code.
2. Stage 4 answerClass post-filter is non-overridable in filter-pipeline.
3. Phase 1 negative receipt passthrough — Phase 2 not invoked.
4. `AuditReceipt.model_response_hash` is populated as SHA-256 hex in every code path.
5. `NO_PROVIDER_CONFIGURED` receipt returned (not an error) when API key absent.
6. No vector DB, embedding, live corpus, or production deployment code present.
7. No legal advice claim in response text or code comments.

---

## Closure Checklist

| Item | Required final state |
| --- | --- |
| Three API routes | implemented |
| `/lpci` page | implemented |
| `src/lib/lpci/` library modules | implemented |
| Unit tests | implemented and PASS |
| `npm run lint` | zero warnings |
| `npm run build` | exit 0 |
| T4 boundary contract C1–C9 | satisfied |
| AuditReceipt per query | emitted |
| No forbidden scope entered | confirmed |

---

## Return Conditions

Return to orchestrator when prototype implementation is complete and all
acceptance criteria are met, or when a forbidden-scope request is encountered.
Stop on: vector DB schema, embedding pipeline, live provider call without
operator key, production corpus registration, public-sync, legal advice claims.

---

## Operator Checkpoint

No additional operator checkpoint is required for the allowed prototype scope
listed above. Operator input is required for:

- adding a production corpus beyond the GOVERNANCE_PILOT pilot;
- configuring a specific LLM provider beyond the `LPCI_LLM_API_KEY` env var pattern;
- extending the UI to multi-tenant or hosted modes;
- adversarial evaluation (T6 scope).

---

## Worker Autonomy / No-Question Rule

Worker must independently fix allowed-scope TypeScript, lint, test, and build
failures and rerun gates. Worker must stop for any request to touch vector DB,
production corpus, live provider setup, legal advice generation, public-sync,
secrets, destructive git commands, or unrelated governance checkers.

---

## Claim Boundary

LPCI1-T5 claims:

- a working local chatbot prototype satisfying T4 response boundary contract C1–C9;
- AuditReceipt emission per query with SHA-256 model_response_hash;
- five-stage T3 filter pipeline implemented in code;
- unit tests covering retrieval, filter, and audit logic.

LPCI1-T5 does NOT claim:

- production readiness or hosted deployment;
- vector-based semantic search (Stage 3 uses keyword/in-memory for prototype);
- legal answer correctness or compliance certification;
- tested retrieval accuracy against a real legal corpus;
- public-sync authorization.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: work order references internal governance chain, private corpus
intelligence baselines, and GC-018 authorization documents not exported
to the public-sync repository.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
