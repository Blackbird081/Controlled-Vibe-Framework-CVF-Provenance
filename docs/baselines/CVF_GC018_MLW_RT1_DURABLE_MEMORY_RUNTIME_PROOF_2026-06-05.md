# CVF GC-018 MLW-RT1 Durable Memory Runtime Proof

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-05

dispatchBaseHead: `acaf9124`

executionBaseHead: `acaf9124`

commitMode: `CODEX_MULTI_ROLE_CLOSEOUT`

## Purpose

Authorize a bounded MLW runtime-proof tranche after MLW1-MLW6 contract closure.

MLW-RT1 proves the current governed `/api/execute` durable-memory route can
write a summary-only durable memory receipt and read that stored summary in a
later governed execution request.

## Decision / Baseline / Proposed Tranche

Decision: CLOSED_PASS_BOUNDED.

Baseline: `acaf9124`.

Proposed tranche: MLW-RT1 Durable Memory Runtime Proof.

Dispatch condition: use only existing file-backed durable-memory runtime
surfaces and close with deterministic plus live governed-route proof.

## Scope

Allowed scope:

- add focused deterministic regression coverage for write-to-read durable
  memory continuity;
- add one Alibaba live proof for the same governed route behavior;
- update MLW roadmap/session/registry evidence;
- create closure artifacts for the runtime proof.

## Non-Goals

- no durable backend replacement;
- no SQLite/Postgres/Redis/vector-store selection;
- no production-grade durability claim;
- no public-sync or public claim;
- no autonomous memory, learning, policy, provider, or prompt mutation;
- no MLW7 or MLW8 implementation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Durable memory store supports file-backed persistence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | source file | `createFileBackedDurableMemoryStore` | durable memory store | EXISTS | ACCEPT |
| Durable memory receipt preserves summary-only invariants | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | source file | `DurableMemoryReceipt` | durable memory store | EXISTS | ACCEPT |
| Execute route reads durable memory before provider call | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts` | source file | `evaluateDurableMemoryRoute` | durable memory route helper | EXISTS | ACCEPT |
| Execute route writes durable memory after successful output | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts` | source file | `evaluateDurableMemoryWrite` | durable memory route helper | EXISTS | ACCEPT |
| Execute route attaches durable memory evidence receipt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | source file | `durableMemoryRead`, `durableMemoryWriteReceipt` | final response builder | EXISTS | ACCEPT |
| Existing deterministic durable-memory route tests exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.durable-memory.test.ts` | source file | `durable memory route wiring` | vitest route test | EXISTS | ACCEPT |
| Alibaba live proof key resolver exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | source file | `resolveAlibabaApiKey` | provider env resolver | EXISTS | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control | Evidence | Disposition |
| --- | --- | --- |
| Prior source map resolved | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | PASS |
| Contract dependency resolved | MLW1 and MLW2 contract artifacts closed | PASS |
| Runtime owner verified | durable memory helper, route final response, and store files cited above | PASS |
| Blind spot | backend choice beyond existing file-backed route remains deferred | ACCEPT_WITH_BOUNDARY |

## Corpus Completeness And Report Integrity

- Corpus task class: RUNTIME_PROOF_CLOSURE.
- Corpus root: bounded changed source set for MLW-RT1.
- Snapshot time: 2026-06-05T00:00:00+07:00.
- Enumeration command: `Get-ChildItem -LiteralPath EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute, docs/baselines, docs/work_orders, docs/reviews, docs/corpus-intelligence, docs/roadmaps, CVF_SESSION -Force`.
- Manifest artifact or inline manifest: inline file-level processing ledger below.
- Manifest hash: 1dcfdfc6dc7b2b74779c528d56bc830bc4e9a8bd193db0e93044734a52b9c3aa.
- Processing ledger artifact or inline ledger: inline file-level processing ledger below.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=9 ledger_terminal=9 exclusions=3 unresolved=0.
- Unresolved files: 0.
- Declared exclusions: broader MLW7/MLW8, backend migration, and public-sync are out of scope.
- Unreadable or unsupported files: none.
- Aggregation check: PASS.
- Drift check: PASS.
- Output traceability: each ledger row maps to MLW-RT1 closure scope.
- Adversarial verification: write action must satisfy real guard authority with `cvfPhase=BUILD` and `aiCommit`; read action remains read-only.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

File-level processing ledger:

| Path | Status | Disposition |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | READ_DEEP | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | READ_DEEP | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.durable-memory.test.ts` | READ_DEEP | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.mlw-rt1-durable-memory.alibaba.live.test.ts` | READ_DEEP | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/alibaba-env.ts` | READ_DEEP | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts` | READ_DEEP | ACCEPT |
| `docs/baselines/CVF_GC018_MLW_RT1_DURABLE_MEMORY_RUNTIME_PROOF_2026-06-05.md` | READ_DEEP | ACCEPT |
| `docs/work_orders/CVF_WO_MLW_RT1_DURABLE_MEMORY_RUNTIME_PROOF_2026-06-05.md` | READ_DEEP | ACCEPT |
| `docs/reviews/CVF_MLW_RT1_DURABLE_MEMORY_RUNTIME_PROOF_COMPLETION_2026-06-05.md` | READ_DEEP | ACCEPT |

## Evidence / Verification

Required evidence:

| Evidence | Command or path | Status |
| --- | --- | --- |
| Deterministic route proof | `npm run test:run -- src/app/api/execute/route.durable-memory.test.ts` | PASS |
| Alibaba live governed-route proof | `npm run test:run -- src/app/api/execute/route.mlw-rt1-durable-memory.alibaba.live.test.ts --reporter=verbose` | PASS |
| Completion review | `docs/reviews/CVF_MLW_RT1_DURABLE_MEMORY_RUNTIME_PROOF_COMPLETION_2026-06-05.md` | CLOSED_PASS_BOUNDED |
| Work order | `docs/work_orders/CVF_WO_MLW_RT1_DURABLE_MEMORY_RUNTIME_PROOF_2026-06-05.md` | CLOSED_PASS_BOUNDED |
| JSON continuity parse | `node -e "JSON.parse(...)"` | PASS |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md`.
- Predecessor intake artifact: `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md`.
- Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.
- Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS.
- Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | RT1 item | Disposition |
| --- | --- | --- |
| UNCHANGED_FROM_INTAKE | MLW1/MLW2 contracts require summary-only governed memory receipts and deterministic context packaging | retained |
| CHANGED_DISPOSITION | Durable memory moved from contract-only proof to bounded runtime proof | upgraded to CLOSED_PASS_BOUNDED |
| NEW_FINDING | File-backed store can prove continuity but not distributed durability | routed as separate backend tranche |
| REMOVED_OR_REJECTED | Production durability, public readiness, and autonomous learning claims | rejected from RT1 scope |

### Follow-Up Routing Matrix

| Routing lane | Item | Route disposition |
| --- | --- | --- |
| DO_NOW | Deterministic write-then-read route regression | completed in RT1 |
| SEPARATE_RUNTIME_TRANCHE | Backend migration or distributed durable storage | defer to fresh GC-018 |
| STRATEGIC_OPERATOR_DECISION | Public-safe memory/learning summary and public-sync wording | operator checkpoint required |
| OUT_OF_SCOPE | MLW7/MLW8, hosted release proof, production durability | excluded from RT1 |
| RESOLVED_BY_DESIGN | Raw memory reinjection | summary-only receipt and `canReinject=false` retained |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MLW-RT1-S1 | durable-memory store source | store emits durable memory receipt | accepted | receipt might expose raw memory | PASS: test asserts summary-only evidence |
| MLW-RT1-S2 | durable-memory route helper | read path injects governed durable context | accepted | read path might bypass governance receipts | PASS: receipt and prompt block checked |
| MLW-RT1-S3 | live Alibaba proof | real route call proves runtime behavior | accepted with boundary | live output could be mistaken for quality proof | PASS: claim limited to route behavior |

## Claim Boundary

This baseline authorizes a bounded runtime proof for existing file-backed
durable memory behavior. It does not claim production durability, distributed
storage, public readiness, hosted readiness, or autonomous learning.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime proof in provenance workspace. Public summary requires
separate public-sync authorization and public-safe wording.
