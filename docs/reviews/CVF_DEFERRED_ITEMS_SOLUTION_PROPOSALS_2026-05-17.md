# CVF Deferred Items Solution Proposals — 2026-05-17

Memory class: FULL_RECORD

Status: PROPOSED — solution proposals for evaluation BEFORE any GC-018 opens.
These are not implementation roadmaps; they are concrete solution shapes so
the operator can decide value/cost without ambiguity.

## Purpose

Final consensus roadmap (2026-05-17) đã lock 7 items vào "deferred — wait
for triggers". Phần này dễ bị Codex hoặc agent tương lai hiểu sai thành "chờ
ai đó nghĩ ra sau". Để tránh điều đó, file này đưa **giải pháp cụ thể** cho
từng deferred item, kèm scope, owner surface, effort estimate, và acceptance
criteria — đủ để operator đánh giá có nên hấp thu hay không trước khi mở
GC-018.

Mỗi proposal:

- mô tả giải pháp cụ thể (không chỉ "doctrine");
- map vào owner surface đã tồn tại;
- đưa effort estimate (S/M/L);
- liệt kê acceptance criteria;
- nêu rõ overlap risk với existing CVF;
- final recommendation: ABSORB / DEFER / REJECT.

## Scope

In scope (7 deferred items):

- ADD-W7-SIGNALS
- ADD-B Context Profile Metadata
- ADD-C1 Continuity / Restart / Handoff Doctrine
- ADD-C2 Delegation / Worker / Subagent Contracts
- ADD-E1 Scoped Knowledge / Code Graph Provider
- GAP-AGENT-HANDOFF Cross-agent handoff + delegation receipt

Out of scope:

- the 3 Nhóm 2 items (OBS-1, ADD-PROVIDER, GAP-MEM) — đã có sequence rõ
  ràng trong final consensus roadmap;
- ADD-A, ADD-D, ADD-BRIEF — đã ở Nhóm 1, không deferred;
- Nhóm 4 excluded items.

## Non-Goals

This file is solution proposal only. It does **not**:

- implement any item;
- promote any doctrine;
- open any GC-018 packet;
- change runtime, public claim, or release gate;
- override Final Consensus Roadmap CD-3 ordering rules.

## Work Plan

| Step | Action | Status |
|---|---|---|
| 1 | Read Phase B synthesis to capture deferred item shape | complete |
| 2 | Propose concrete TypeScript shape for each deferred item | complete |
| 3 | Map each proposal to existing owner surface | complete |
| 4 | Estimate effort (S/M/L) and identify overlap risk | complete |
| 5 | Recommend ABSORB / DEFER / REJECT with concrete trigger conditions | complete |
| 6 | Document updated absorption queue order | complete |

## Acceptance Criteria

This proposal file is accepted as input to operator absorption decisions when:

- each deferred item has a concrete solution shape (not just doctrine language);
- each proposal cites the owner surface from existing EXTENSIONS;
- each proposal includes effort estimate and overlap risk analysis;
- each proposal ends with explicit ABSORB / DEFER / REJECT recommendation;
- updated absorption queue replaces "wait for triggers" with explicit
  conditions;
- pre-commit governance hooks pass.

All six criteria are met by this file.

## Verification / Evidence

Verification done before authoring:

- read Phase B synthesis (continuity, delegation, scoped knowledge sections);
- spot-checked CPF agent contracts (registration, boundary, scope, audit,
  orchestration) for overlap analysis;
- spot-checked LPF for memory and reinjection contract overlap;
- read final consensus roadmap CD-3 for ordering rule preservation.

## Authorization / Decision

This file does not authorize implementation. Each ABSORB recommendation
becomes binding only after operator decision to open the corresponding GC-018
packet (or doc promotion packet for ADD-A/D/BRIEF and ADD-W7-SIGNALS).

DEFER recommendations are binding as advisory ordering only; they do not
prevent future operator decision to absorb earlier if a concrete trigger
condition is met.

## Source

- Final consensus: `docs/roadmaps/CVF_UNABSORBED_KNOWLEDGE_FINAL_CONSENSUS_ROADMAP_2026-05-17.md`
- Inventory amended: `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- Phase B synthesis: `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_PHASE_B_CONTINUITY_DELEGATION_AND_SCOPED_KNOWLEDGE_SYNTHESIS_2026-05-07.md`
- Phase A synthesis: `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_PHASE_A_GOVERNED_CAPABILITY_AND_BOUNDARY_GOVERNANCE_SYNTHESIS_2026-05-07.md`
- Owner-surface promotion map: `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_OWNER_SURFACE_PROMOTION_MAP_2026-05-06.md`

## Solution Proposal 1 — ADD-W7-SIGNALS

### Mô tả giải pháp

Bổ sung 3 signal types vào evidence receipt schema hiện có. Không phải runtime
behavior change, chỉ là schema extension với optional fields.

### Concrete schema extension

Thêm vào W7 receipt record type:

```ts
interface BoundarySignals {
  pathLockSignal?: {
    restrictedPathId: string;
    pathFollowed: boolean;
    deviationReason?: string;
  };
  minimalResponseMatch?: {
    policyId: string;
    boundedScope: string;
    actualScopeMatch: boolean;
  };
  restrictedPathCount?: {
    totalGatesEncountered: number;
    gatesCrossed: number;
    gatesRejected: number;
  };
}
```

Tất cả fields là optional. Existing receipts không bị invalidate.

### Owner surface

`EXTENSIONS/CVF_GUARD_CONTRACT/` — evidence receipt schema definition.

### Overlap risk

Thấp. Không overlap với governance signal schema (đó là policy-side). W7
signals là **outcome-side**: ghi lại policy đã apply như thế nào, không phải
policy là gì.

### Effort estimate

**Small** — schema-only change. 1 type definition + 5-10 tests cho schema
validation. Không có business logic.

### Acceptance criteria

- 3 signal types added to receipt schema;
- existing receipts vẫn parse được (backward compatible);
- 5-10 unit tests for schema validation;
- ADR document tại sao 3 signals này được chọn;
- không có runtime behavior change.

### Dependencies

ADD-D doctrine **phải** promoted trước. Lý do: 3 signals là instrumentation
cho 4 policy classes (hard prohibition / soft constraint / communication
policy / restricted execution path) — schema vô nghĩa nếu policy framework
chưa có.

### Recommendation

**ABSORB sau khi ADD-D promote.** Effort thấp, value cao (audit trail tốt
hơn cho boundary-first governance), risk R0.

---

## Solution Proposal 2 — ADD-B Context Profile Metadata

### Mô tả giải pháp

Một typed advisory record cho phép Context Builder shape context theo session
type và risk. Không phải execution authority, không phải prompt mode system.

### Concrete shape

```ts
interface ContextProfile {
  sessionId: string;
  profileVersion: string;
  budgetHints: {
    maxTokens?: number;
    maxSources?: number;
    compressionAllowed: boolean;
  };
  sourceRelevance: Array<{
    sourceId: string;
    relevanceScore: number;
    freshnessTag: 'canon' | 'recent' | 'stale' | 'rejected';
  }>;
  reinjectionEligibility: Array<{
    sourceId: string;
    eligibleFromPhase: string;
    requiresApproval: boolean;
  }>;
  evidenceSensitivity?: 'standard' | 'redacted' | 'restricted';
}
```

Context Builder consumes profile; Policy Engine validates fields touching
risk; Knowledge Layer owns source-side fields.

### Owner surface

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` — Context Builder consumer.
- `EXTENSIONS/CVF_GUARD_CONTRACT/` — Policy Engine validator cho risk fields.

### Overlap risk

**Trung bình**. Có thể overlap với:

- existing context packager logic;
- existing source-tagging mechanisms;
- knowledge.vault.intake metadata.

Giải pháp: profile là **advisory layer trên top** của các surfaces này, không
replace chúng. Profile fields phải reference existing source IDs, không tạo
ra source registry mới.

### Effort estimate

**Medium** — typed schema + Context Builder consumer integration + Policy
Engine validator + 20-30 tests. Không thay đổi runtime execution path, chỉ
shape input.

### Acceptance criteria

- ContextProfile type defined với strict TypeScript;
- Context Builder consumes profile và return shaped context;
- Policy Engine validates risk fields (evidenceSensitivity);
- knowledge.vault.intake mapping documented (không duplicate IDs);
- 20-30 tests covering: valid profile / invalid profile / missing fields /
  policy violation / source ID mismatch;
- ADR ghi rõ "advisory metadata only, no execution authority".

### Dependencies

Cần OBS-1 close trước để có rate-limit và quota visibility — context budget
hints không có ý nghĩa nếu không thấy quota state.

### Recommendation

**ABSORB sau OBS-1.** Effort medium, value medium-high (giảm token waste,
cải thiện handoff). Overlap risk có thể manage qua ADR.

---

## Solution Proposal 3 — ADD-C1 Continuity / Restart / Handoff Doctrine

### Mô tả giải pháp

Doctrine + record schema cho long-running agent work checkpoint/restore/handoff.
Không phải runtime engine — là vocabulary và schema để các existing surfaces
(W123 continuity, Roadmap closure, Knowledge Layer) write checkpoint records
đồng nhất.

### Concrete shape

```ts
interface ContinuityCheckpoint {
  checkpointId: string;
  taskId: string;
  agentId: string;
  phaseBoundary: string;
  closedDecisions: Array<{
    decisionId: string;
    decision: string;
    reasoning: string;
    irrevocable: boolean;
  }>;
  openItems: Array<{
    itemId: string;
    description: string;
    nextPhase: string;
  }>;
  artifactMemory: Array<{
    path: string;
    hash: string;
    role: 'input' | 'output' | 'evidence';
  }>;
  reinjectionPolicy: 'always' | 'on-request' | 'expired';
  evidenceReceiptIds: string[];
}
```

Schema này được W123 continuation và roadmap closure files reference cùng
format thay vì free-form text.

### Owner surface

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` — checkpoint record contract.
- W123 continuation (existing) — consumer.
- Roadmap closure files (existing) — consumer.

### Overlap risk

**Cao**. W123 continuation đã handle root/follow-up chain semantics. Risk:
C1 doctrine duplicate hoặc compete với W123 ownership.

Giải pháp: C1 là **schema standard** mà W123 implement, không phải replacement.
ADR phải nêu rõ W123 vẫn own execution continuity; C1 chỉ standardize record
shape.

### Effort estimate

**Medium** — schema + ADR + W123 audit (existing files đã follow shape chưa?)
+ 15-20 tests. Có thể cần update một số existing W123 closure files để
conform.

### Acceptance criteria

- ContinuityCheckpoint type defined;
- W123 continuation files audited và update để conform (có thể là batch
  doc update);
- 15-20 tests covering schema validation;
- ADR rõ "W123 owns execution; C1 owns record shape";
- no runtime engine added.

### Dependencies

Không cần Nhóm 2 close trước. Có thể parallel với OBS-1 nếu owner surface
khác nhau.

### Recommendation

**ABSORB conditional.** Effort medium, value medium. **Chỉ absorb nếu có
multi-agent scenario đang active** (e.g., khi mở W7/W8 orchestration). Nếu
không có active scenario, defer thêm — schema-without-consumer là dead
weight.

---

## Solution Proposal 4 — ADD-C2 Delegation / Worker / Subagent Contracts

### Mô tả giải pháp

Contract language cho multi-agent delegation: explicit file ownership, bounded
write scope, final-report-of-changed-files, subagent boundary inheritance.

### Concrete shape

```ts
interface DelegationContract {
  parentTaskId: string;
  workerAgentId: string;
  delegationId: string;
  ownership: {
    ownedFiles: string[];
    ownedModules: string[];
    forbiddenPaths: string[];
    writeScope: 'append-only' | 'modify-listed' | 'create-only';
  };
  inheritedBoundaries: {
    riskCeiling: 'R0' | 'R1' | 'R2' | 'R3';
    policyIds: string[];
    sandboxTier: number;
  };
  reportRequirement: {
    finalChangedFiles: 'required';
    finalEvidenceReceipts: 'required';
    interimCheckpoints: 'optional';
  };
  blockedActions: Array<{
    action: string;
    reason: string;
  }>;
}
```

Mỗi delegation tạo một contract record. Worker session chỉ có thể act trong
contract boundary; final report bắt buộc.

### Owner surface

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/agent.governed.session.contract.ts`
  — đã có session contract, mở rộng cho delegation.
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` — execution boundary enforcement.

### Overlap risk

**Trung bình-cao**. CPF đã có:

- `agent.governed.session.contract.ts` (session boundary)
- `agent.definition.boundary.contract.ts` (permission profile)
- `agent.scope.resolution.batch.contract.ts` (scope resolution)
- `orchestration.contract.ts` (orchestration rules)

Risk: C2 contract có thể duplicate scope với 4 contracts trên.

Giải pháp: C2 là **integration layer** giữa session + scope + orchestration,
không phải contract mới. Specifically: wire `agent.scope.resolution` output
vào `agent.governed.session` input qua delegation contract.

### Effort estimate

**Medium-Large** — schema + integration của 4 existing contracts + worker
session enforcement + 30-40 tests. Đây là item phức tạp nhất trong deferred
group.

### Acceptance criteria

- DelegationContract type defined;
- integration wired qua 4 existing CPF contracts;
- worker session enforcement: write attempt outside ownership = reject;
- final report enforcement: missing final-changed-files = block closure;
- 30-40 tests bao gồm: valid delegation / scope violation / missing report /
  forbidden path / risk ceiling exceeded;
- ADR ghi rõ relationship với 4 existing CPF contracts.

### Dependencies

Cần GAP-AGENT-HANDOFF close trước (xem Proposal 6) — handoff protocol là
một use case cụ thể của delegation contract.

### Recommendation

**DEFER thêm**. Effort medium-large, value chỉ realize được khi có
multi-agent orchestration thực sự. Hiện tại CVF chủ yếu single-agent. Mở GC-018
chỉ khi W7/W8 orchestration roadmap mở.

---

## Solution Proposal 5 — ADD-E1 Scoped Knowledge / Code Graph Provider

### Mô tả giải pháp

Read-only bounded knowledge provider contract cho code intelligence patterns
(code graph, cortex, indexed reference). Không phải knowledge runtime — là
contract định nghĩa làm thế nào để register, query, và bound các knowledge
sources external.

### Concrete shape

```ts
interface ScopedKnowledgeProvider {
  providerId: string;
  providerClass: 'code-graph' | 'cortex' | 'source-map' | 'indexed-reference';
  scope: {
    repoPaths: string[];
    excludePaths: string[];
    languageFilter?: string[];
  };
  metadata: {
    sourceClass: 'canon' | 'reference' | 'example' | 'rejected';
    freshness: 'live' | 'cached' | 'stale';
    confidence: number;
    lastSync: string;
  };
  queryContract: {
    readOnly: true;
    maxResultsPerQuery: number;
    cachingPolicy: string;
  };
  blockedFromActing: true;
}
```

Providers register vào Knowledge Layer; Context Builder query qua bounded
contract; Policy Engine cấm provider classifying risk hoặc overriding
governance.

### Owner surface

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/knowledge.vault.intake.contract.ts`
  — extend cho scoped provider class.
- Context Builder — consumer.

### Overlap risk

**Trung bình**. Knowledge vault intake đã có. Risk: scoped provider duplicate
intake mechanism.

Giải pháp: scoped provider là **subclass** của knowledge intake (provider
class = `code-graph` thay vì `manual-intake`). Không tạo registry mới.

### Effort estimate

**Medium** — schema + knowledge vault intake extension + Context Builder
integration + 20-25 tests.

### Acceptance criteria

- ScopedKnowledgeProvider type defined as knowledge.vault.intake subclass;
- 1 reference implementation (code-graph) hoặc 1 mock implementation cho
  testing;
- Context Builder query API;
- Policy Engine blocks provider classification và override attempts;
- 20-25 tests bao gồm: valid registration / scope violation / read-only
  enforcement / policy override blocked.

### Dependencies

Cần ADD-B Context Profile close trước. Lý do: scoped provider output phải
được consume qua context profile sourceRelevance field.

### Recommendation

**DEFER thêm**. Effort medium, value conditional. **Chỉ absorb nếu có concrete
use case** (e.g., refactor wave cần code impact analysis, security audit cần
indexed reference). Hiện tại không có use case active.

---

## Solution Proposal 6 — GAP-AGENT-HANDOFF Cross-agent Handoff Protocol

### Mô tả giải pháp

Một small contract bổ sung kết nối các agent contracts đã có (registry,
boundary, scope, orchestration) thành end-to-end handoff flow với delegation
receipt.

### Concrete shape

```ts
interface AgentHandoffRecord {
  handoffId: string;
  sourceAgentId: string;
  targetAgentId: string;
  taskId: string;
  handoffPhase: string;
  contextSnapshot: {
    closedDecisions: string[];
    openItems: string[];
    artifactRefs: string[];
    evidenceReceiptIds: string[];
  };
  delegationContractRef?: string;
  policyContinuity: {
    inheritedPolicies: string[];
    riskCeiling: string;
    sandboxTier: number;
  };
  acceptanceCriteria: {
    requiredFinalEvidence: string[];
    returnToSourceCondition?: string;
  };
  receiptId: string;
}
```

Mỗi handoff event tạo một record. Target agent không thể act cho đến khi
handoff record được committed; source agent không thể consider task closed
cho đến khi target acknowledge.

### Owner surface

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` — handoff contract.
- Existing `agent.governed.session.contract.ts` — referenced.
- Existing `agent.scope.resolution.batch.contract.ts` — referenced cho
  policy continuity.

### Overlap risk

**Thấp**. Đây là **bridge contract** kết nối các existing contracts. Không
duplicate, chỉ wire.

### Effort estimate

**Small-Medium** — schema + integration + 15-20 tests. Smaller than C2 vì
chỉ focus vào handoff event, không bao gồm worker session enforcement.

### Acceptance criteria

- AgentHandoffRecord type defined;
- handoff event creates record và blocks target agent acting until committed;
- policy continuity verified (target inherits source's risk ceiling);
- 15-20 tests bao gồm: valid handoff / missing acknowledgment / policy
  downgrade attempt / orphan handoff;
- ADR ghi rõ relationship với 4 existing CPF agent contracts.

### Dependencies

Không. Có thể standalone implement.

### Recommendation

**ABSORB conditional.** Effort small-medium, value depends on multi-agent
usage. **Khuyến nghị absorb nếu có ≥2 governed multi-agent handoffs trong
production** (hiện tại có Claude ↔ Codex handoff pattern thực sự). Nếu chỉ
single-agent CVF thì defer.

---

## Tóm tắt Recommendations

| Item | Effort | Value | Recommendation | Trigger if deferred |
|---|---|---|---|---|
| ADD-W7-SIGNALS | S | Medium-High | **ABSORB** sau ADD-D | (auto-trigger) |
| ADD-B Context Profile | M | Medium-High | **ABSORB** sau OBS-1 | (auto-trigger) |
| ADD-C1 Continuity | M | Medium | DEFER conditional | Multi-agent scenario active |
| ADD-C2 Delegation | M-L | Medium-High | **DEFER** | W7/W8 orchestration roadmap |
| ADD-E1 Scoped Knowledge | M | Medium | DEFER conditional | Concrete use case (refactor/audit) |
| GAP-AGENT-HANDOFF | S-M | Medium | **ABSORB conditional** | ≥2 multi-agent handoffs in prod |

### Reclassification từ "wait for triggers" sang concrete recommendations

3 items đề xuất **ABSORB** (có thể đưa vào Nhóm 2 absorption queue sau OBS-1):

1. **ADD-W7-SIGNALS** — sau ADD-D doctrine promote, effort S, R0.
2. **ADD-B Context Profile** — sau OBS-1 close, effort M, R0.
3. **GAP-AGENT-HANDOFF** — nếu có ≥2 multi-agent handoffs thực sự trong
   production CVF. Hiện tại Claude ↔ Codex pattern qualifies → recommend
   ABSORB.

2 items **DEFER conditional** (có concrete trigger condition cụ thể, không
phải "wait"):

4. **ADD-C1 Continuity** — defer cho đến khi có long-running multi-phase
   agent task hoạt động.
5. **ADD-E1 Scoped Knowledge** — defer cho đến khi có refactor/audit
   roadmap cần code intelligence.

1 item **DEFER** thực sự (effort cao, value chưa rõ):

6. **ADD-C2 Delegation** — effort M-L, value chỉ realize khi multi-agent
   orchestration mature. Defer cho đến W7/W8 roadmap.

## Updated Absorption Sequence Recommendation

Sequence cập nhật từ CD-3 của final consensus roadmap:

1-2. Inventory + reporting rule amendments (đã applied)
3. ADD-A + ADD-D + ADD-BRIEF doctrine promotion (Nhóm 1)
4. OBS-1 Observability Plane Foundation GC-018 (Nhóm 2 priority 1)
5. ADD-PROVIDER Output Contracts GC-018 (Nhóm 2 priority 2)
6. GAP-MEM 3 memory sub-contracts GC-018 (Nhóm 2 priority 3)
7. **ADD-W7-SIGNALS schema extension** (promoted từ Nhóm 3, effort S, sau ADD-D)
8. **ADD-B Context Profile metadata** (promoted từ Nhóm 3, effort M, sau OBS-1)
9. **GAP-AGENT-HANDOFF protocol** (promoted từ Nhóm 3, effort S-M, conditional)
10+. ADD-C1, ADD-C2, ADD-E1 deferred với concrete trigger conditions

Tổng cộng 9 items được đưa vào absorption queue với concrete plan, 3 items
defer với explicit trigger conditions thay vì "wait for triggers".

## Claim Boundary

File này là solution proposal, không phải:

- implementation authorization;
- doctrine promotion;
- GC-018 packet;
- public claim change;
- runtime behavior change.

Mỗi proposal vẫn cần GC-018 packet riêng khi absorption thực sự begin. Các
recommendations chỉ thay đổi **ordering và conditional triggers**, không
authorize work.

Final consensus roadmap (CD-3) vẫn binding. File này là **extension** của
CD-3 với concrete solution shapes cho deferred items.

## Related Artifacts

- `docs/roadmaps/CVF_UNABSORBED_KNOWLEDGE_FINAL_CONSENSUS_ROADMAP_2026-05-17.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_INVENTORY_2026-05-16.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CLAUDE_REVIEW_2026-05-17.md`
- `docs/reviews/CVF_UNABSORBED_KNOWLEDGE_CODEX_RESPONSE_TO_CLAUDE_2026-05-17.md`
- `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_PHASE_B_CONTINUITY_DELEGATION_AND_SCOPED_KNOWLEDGE_SYNTHESIS_2026-05-07.md`
