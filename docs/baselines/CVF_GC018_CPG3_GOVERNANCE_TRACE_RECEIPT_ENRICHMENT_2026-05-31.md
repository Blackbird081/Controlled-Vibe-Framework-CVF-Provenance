# CVF GC-018 Continuation Candidate

## CPG-3 Governance Trace Receipt Enrichment

Memory class: BASELINE_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-31

---

## Purpose

Authorize the bounded CPG-3 follow-up to CPG-2: add an optional
`governanceTrace` field to the web `GovernanceEvidenceReceipt` so receipt
replay can show summary-level policy checkpoints without exposing raw prompts,
provider keys, secrets, or framework-private memory.

## Scope / Target / Owner Boundary

Target contract: `cvf.governanceTraceReceiptEnrichment.cpg3.v1`.

Owner:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` and
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`.

Allowed runtime change:

- add `GovernanceTraceEntry` as a bounded summary type;
- add optional `governanceTrace?: GovernanceTraceEntry[]` to
  `GovernanceEvidenceReceipt`;
- extend `BuildGovernanceEvidenceReceiptInput` and `buildEvidenceReceipt()` so
  the builder emits bounded trace summaries from existing receipt metadata;
- add focused builder tests and a route-consumer regression test;
- preserve `/api/execute/route.ts` line count by not editing that file.

Forbidden scope:

- no raw prompt, raw output, system prompt, provider key, secret, private
  memory, or framework-private context capture;
- no provider routing, prompt, model, memory, or Learning Plane mutation;
- no new receipt storage backend, migration, public-sync, hosted-readiness,
  production-readiness, or universal bypass-prevention claim;
- no edit to `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`.

Risk ceiling: R2.

## Source / Predecessor Evidence

- Parent CPG roadmap:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- CPG-2 completion:
  `docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md`
- LHW21 T3 advisory:
  `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`
- Current receipt type:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- Current receipt builder:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- Current route consumer:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| CPG-2 prerequisite is closed | `EXISTS` | `docs/reviews/CVF_CPG2_CP2_HARD_GATE_ENFORCEMENT_COMPLETION_2026-05-31.md` | completion packet | `CLOSED_PASS_BOUNDED` | CPG-2 completion review | ACCEPT |
| LHW21 T3 proposed trace concept exists | `EXISTS` | `docs/reference/CVF_LHW21_T3_RECEIPT_ENRICHMENT_ADVISORY_CONNECTOR_SPEC_2026-05-31.md` | Purpose and S3 contract | `governanceTrace` | LHW21 T3 advisory spec | ACCEPT |
| Current receipt type exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 82-105 | `GovernanceEvidenceReceipt` | web AI types | ACCEPT |
| Current receipt type has required anchor fields | `VALUE_SET` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 83-104 | `GovernanceEvidenceReceipt` | web AI types | ACCEPT: `receiptId`, `evidenceMode`, `routeId`, `decision`, `riskLevel`, `provider`, `model`, `routingDecision`, `policySnapshotId`, `envelopeId`, `generatedAt` |
| Current receipt builder input exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 65-81 | `BuildGovernanceEvidenceReceiptInput` | web governance envelope | ACCEPT |
| Current receipt builder exists | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 107-132 | `buildEvidenceReceipt` | web governance envelope | ACCEPT |
| Current route consumes receipt builder on success path | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 847-863 | `buildEvidenceReceipt` | execute route | ACCEPT |
| Execute route is at hard-threshold boundary | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | command-backed line count | `POST` | execute route | ACCEPT: 999 physical lines |
| Existing builder tests exist | `EXISTS` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.test.ts` | file source | `web-governance-envelope` | vitest suite | ACCEPT |
| Current receipt type lacks runtime `governanceTrace` field | `RUNTIME_BEHAVIOR` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | lines 82-105 plus source search | `GovernanceEvidenceReceipt` | web AI types | ACCEPT: no current runtime owner field before this tranche |

## New Proposed Fields And Symbols

| Proposed item | Intended owner | Purpose | Runtime status now |
| --- | --- | --- | --- |
| `GovernanceTraceEntry` | `ai/types.ts` | Bounded receipt trace entry schema | DOC_ONLY_NEW |
| `governanceTrace` | `GovernanceEvidenceReceipt` | Optional ordered policy summary trace | DOC_ONLY_NEW |
| `buildGovernanceTrace` | `web-governance-envelope.ts` | Internal builder for summary-only entries | DOC_ONLY_NEW |

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory: parent CPG roadmap, LHW21 T3 advisory, CPG-2 completion,
  current receipt type, current receipt builder, current execute route calls,
  and builder/route tests.
- Prior absorption evidence resolved: LHW21 T3 remained documentation-only and
  explicitly required a separate GC-018 before runtime receipt extension.
- Detailed source files used: `ai/types.ts`, `web-governance-envelope.ts`,
  `route.ts`, `web-governance-envelope.test.ts`, `route.test.ts`.
- Source families skipped: provider routing, MCP INT1 enforcement, Learning
  Plane mutation, public-sync, and hosted deployment evidence; all are outside
  CPG-3.
- File-level accepted value: add optional receipt trace summaries in the
  receipt owner, not route inline logic.
- Owner-surface normalization: schema lives in `ai/types.ts`; construction
  lives in `web-governance-envelope.ts`; route receives trace through existing
  builder calls.
- Accept/defer/reject matrix: receipt trace summary ACCEPT_NOW; raw prompt or
  secret capture REJECT; route growth REJECT; live release proof REQUIRED at
  closure; public export DEFER.
- Adversarial roles completed: Implementer (minimal owner edit), Skeptic
  (trace must not leak prompt/secret/private memory), Auditor (line-count guard
  and release proof), Product/Operator Advocate (forensic replay value).
- Thin proof target: builder tests, focused route consumer test, typecheck,
  build, file-size guard, autorun gates, and release governance bundle.
- Blind-spot verdict: CLEAR for bounded receipt enrichment; public,
  production, and universal bypass claims remain out-of-scope.

## GC-018 Continuation Candidate

- Candidate ID: `gc018-cpg3-governance-trace-receipt-enrichment-2026-05-31`
- Parent roadmap / wave:
  `docs/roadmaps/CVF_CONNECTION_POINT_GUARD_ENFORCEMENT_ROADMAP_2026-05-31.md`
- Proposed scope: add optional `governanceTrace` to the web receipt type and
  builder; prove route consumption without editing `route.ts`.
- Continuation class: REALIZATION
- Active quality assessment: CPG-2 closed with release-quality proof; LHW21 T3
  proposal is ready for bounded runtime realization.
- Assessment date: 2026-05-31
- Weighted total: 9/10
- Lowest dimension: operational blast radius (1/2)
- Quality-first decision: EXPAND_NOW
- Why expansion is the better move now: forensic receipt replay becomes useful
  after hard-gate behavior is proven, and the change can stay inside receipt
  ownership.
- Quality protection commitments: summary-only fields, no raw data capture, no
  route growth, no public claim, and live release proof before closure.
- Active-path impact: LIMITED
- Risk if deferred: governance decisions remain less replayable even though
  CPG-1 and CPG-2 already produce connection-point guard decisions.
- Lateral alternative considered: YES
- Why not lateral shift: public-sync and CPG-4-style analytics are premature
  until the bounded receipt field exists.
- Expected enforcement class: RECEIPT_EVIDENCE_ENRICHMENT
- Required evidence if approved: focused tests, route-consumer regression,
  typecheck/build, file-size guard, release governance bundle, autorun gates,
  and git diff scope proof.

### Depth Audit

- Risk reduction: 2
- Decision value: 2
- Machine enforceability: 2
- Operational efficiency: 2
- Portfolio priority: 1
- Total: 9
- Decision: CONTINUE
- Reason: bounded receipt trace improves forensic replay without expanding
  provider execution or route ownership.

### Authorization Boundary

- Authorized now: YES
- Next batch name: `CPG-3 Governance Trace Receipt Enrichment`
- Human authorization: SATISFIED on 2026-05-31 by operator instruction
  "CPG-3 tiep tuc".
- Hard invariants: no raw prompts, no secrets, no private memory, no provider
  mutation, no route growth, no public-sync, no hosted/production claim.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: CPG-3 Governance Trace Receipt Enrichment.

Proposed tranche: add optional bounded `governanceTrace` receipt entries in
the web receipt owner type and builder, with route consumption proven through
existing route builder calls.

## Evidence / Verification

Required before closure:

```powershell
npm run test:run -- src/lib/web-governance-envelope.test.ts src/app/api/execute/route.governance-trace.test.ts
npm run check
npm run build
python governance/compat/check_governed_file_size.py --enforce
python scripts/run_cvf_release_gate_bundle.py --json
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; public-sync requires separate authorized
batch.

## Claim Boundary

This GC-018 authorizes bounded optional receipt trace enrichment only. It does
not authorize raw capture, provider behavior changes, Learning Plane mutation,
public export, hosted readiness, production readiness, or universal bypass
prevention claims.
