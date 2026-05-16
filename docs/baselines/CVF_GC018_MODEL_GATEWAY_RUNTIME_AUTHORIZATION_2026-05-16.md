<!-- Memory class: SUMMARY_RECORD -->

# CVF GC-018 Model Gateway Runtime Authorization Candidate - 2026-05-16

> Type: TRANCHE AUTHORIZATION CANDIDATE
> Candidate: Model Gateway Runtime Adoption
> Date: 2026-05-16
> Status: ROADMAP-READY PACKET IN PREPARATION
> Operator decision required before implementation

---

## 1. Authorization Decision

**ROADMAP PREPARATION AUTHORIZED; IMPLEMENTATION NOT YET AUTHORIZED.**

The operator clarified that one-file-at-a-time review is too passive. This file
therefore belongs to a roadmap-ready packet that may include the roadmap draft,
ADR candidate, source adoption matrix, and test/proof plan.

Implementation may begin only after the operator explicitly approves this
roadmap-ready packet.

---

## 2. Predecessor Evidence

| Artifact | Role |
|---|---|
| `docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_2026-05-16.md` | Docs-only absorption packet, amended after rebuttal |
| `docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_CLAUDE_REBUTTAL_2026-05-16.md` | Independent rebuttal that required path/schema corrections |
| `docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_CODEX_RESPONSE_TO_CLAUDE_2026-05-16.md` | Codex response accepting corrective action |
| `docs/reference/CVF_MODEL_GATEWAY_PROXY_PROVIDER_BOUNDARY_SPEC_2026-05-16.md` | Boundary spec identifying Model Gateway as priority runtime candidate |
| `EXTENSIONS/CVF_MODEL_GATEWAY/README.md` | Existing official Model Gateway wrapper/re-export surface |

Current standing decision: the 16.5 intake tranche is absorbed as docs-only. It
does not yet authorize runtime adoption.

---

## 3. Proposed Tranche

**Model Gateway Runtime Adoption**

Proposed objective:

Adopt the useful `freellmapi` gateway TypeScript artifacts into the existing
CVF Model Gateway owner surface, through Guard Contract integration, without
copying the source files wholesale and without creating a second gateway.

Primary adoption source:

`.private_reference/legacy/CVF 16.5/freellmapi/`

Candidate source files:

- `provider.registry.ts`
- `provider.health.ts`
- `quota.ledger.ts`
- `routing.policy.ts`
- `fallback.policy.ts`
- `sticky.session.ts`
- `credential.vault.ts`
- `gateway.receipt.ts`

Target owner surface:

- `EXTENSIONS/CVF_MODEL_GATEWAY/`

Required integration posture:

- preserve `EXTENSIONS/CVF_MODEL_GATEWAY/` as the official owner surface;
- integrate through CVF Guard Contract and gateway policy boundaries;
- adapt types and behavior to CVF naming, receipts, risk classes, and tests;
- do not copy source files unchanged;
- do not import any free-tier or bypass framing;
- do not claim governance enforcement without live proof.

---

## 4. Wrapper vs Implementation-Owner Decision

The future roadmap must explicitly declare one of these decisions and record it
in a new or amended ADR:

1. **Wrapper-only-kept**
   - `EXTENSIONS/CVF_MODEL_GATEWAY/` remains a wrapper/re-export package.
   - Runtime implementation stays in existing source modules.
   - The 8 `freellmapi` candidates can only become adapter references, tests,
     or docs until a later structural authorization upgrades ownership.

2. **Implementation-owner upgrade**
   - `EXTENSIONS/CVF_MODEL_GATEWAY/` becomes the implementation owner for the
     adopted provider registry, health, quota, routing, fallback, sticky
     session, credential boundary, and receipt logic.
   - This is a material ownership change and requires ADR coverage plus
     package-level tests.

Recommended decision for the roadmap: **implementation-owner upgrade**.

Reason: the requested work is runtime adoption of 8 TypeScript gateway artifacts.
Keeping `EXTENSIONS/CVF_MODEL_GATEWAY/` as wrapper-only would preserve current
lineage but would not create a useful runtime adoption owner. The roadmap and
ADR may still reject the upgrade if review finds a stronger existing owner.

---

## 5. GC-018 Continuation Candidate Packet

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-MODEL-GATEWAY-RUNTIME-ADOPTION-2026-05-16
- Date: 2026-05-16
- Parent roadmap / wave: CVF 16.5 external knowledge intake, docs-only absorption amended by Claude rebuttal
- Proposed scope: Adopt 8 legacy freellmapi TypeScript gateway artifacts into the official CVF Model Gateway owner surface through Guard Contract integration, tests, ADR, and live-proof boundary
- Continuation class: STRUCTURAL
- Active quality assessment: docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_2026-05-16.md
- Assessment date: 2026-05-16
- Weighted total: 7.5/10
- Lowest dimension: Runtime proof status (0/10) — no runtime adoption or live enforcement proof exists yet
- Quality-first decision: EXPAND_NOW only if operator approves the roadmap-ready packet; otherwise DEFER
- Why expansion is still the better move now: Claude rebuttal identified 8 already-written TypeScript gateway artifacts and an existing official Model Gateway surface. A bounded adoption roadmap can reduce token waste and prevent future agents from rewriting provider registry, health, quota, routing, fallback, sticky session, credential, and receipt logic from scratch.
- Quality protection commitments: docs-first roadmap before code; ADR for wrapper-only vs implementation-owner decision; Guard Contract integration; per-file vitest coverage; live proof only when enforcement is claimed; GC-023 split-before-exception rule; no public/provider bypass framing.
- Remediation target if not expanding: Keep docs-only absorption status and do not modify runtime.
- Why now: The intake/rebuttal cycle is complete and points to one high-leverage owner surface, Model Gateway, with concrete source artifacts and destination path.
- Active-path impact: MATERIAL if implementation-owner upgrade is selected; LIMITED if wrapper-only-kept is selected.
- Risk if deferred: Future agents may rediscover and rewrite the same gateway primitives, or create a parallel gateway surface despite the existing `EXTENSIONS/CVF_MODEL_GATEWAY/`.
- Lateral alternative considered: YES
- Why not lateral shift: A lateral docs-only note already exists; the next value-bearing move is a bounded runtime adoption roadmap, not another broad review.
- Real decision boundary improved: YES — forces the wrapper-only vs implementation-owner decision before code.
- Expected enforcement class:
  - GATEWAY_PRECONDITION
  - RUNTIME_GUARD
  - CI_REPO_GATE
  - GOVERNANCE_DECISION_GATE
- Required evidence if roadmap is approved:
  - Roadmap declaring wrapper-only-kept vs implementation-owner upgrade
  - ADR recording the chosen ownership posture
  - Guard Contract integration design
  - Adapted implementation for each of the 8 source candidates, not wholesale copy
  - Vitest coverage for every adopted file
  - Package-level check for touched package
  - GC-023 file-size compliance, splitting files before any exception request
  - Live governance proof before claiming enforcement
  - End-of-tranche commit with descriptive message following `commit_and_rules` feedback
```

---

## 6. Depth Audit

| Dimension | Score | Note |
|---|---:|---|
| Risk reduction | 2 | Reduces risk of parallel provider gateways and hidden routing behavior |
| Decision value | 2 | Forces a clear owner decision for `EXTENSIONS/CVF_MODEL_GATEWAY/` |
| Machine enforceability | 2 | Can be tested with per-file vitest, package check, and release/live proof gates |
| Operational efficiency | 2 | Reuses 8 already-written TypeScript candidates instead of rewriting |
| Portfolio priority | 2 | Model Gateway is a central runtime boundary and the highest-leverage next surface from the intake |
| **Total** | **10** | **REVIEW REQUIRED UNTIL OPERATOR APPROVES** |

Decision: **ROADMAP-READY PACKET MAY BE PREPARED; IMPLEMENTATION PENDING
OPERATOR APPROVAL**.

---

## 7. Scope Lock If Approved

Allowed before implementation approval:

- Create the roadmap draft.
- Create the ADR candidate.
- Create the source adoption matrix.
- Create the test and proof plan.
- Update handoff/progress records for review readiness.

Allowed after implementation approval:

- Create a bounded roadmap for Model Gateway runtime adoption.
- Create or amend an ADR for wrapper-only-kept vs implementation-owner upgrade.
- Adapt the 8 `freellmapi` TypeScript artifacts into CVF-owned code.
- Integrate route decisions with Guard Contract and gateway policy boundaries.
- Add vitest coverage for each adopted file.
- Add live proof only for actual governance enforcement claims.
- Split files if any source/test file approaches GC-023 thresholds.

Forbidden:

- Copy `freellmapi` files wholesale without CVF adaptation.
- Import free-provider, bypass, or unlimited-access claims.
- Create a second Model Gateway surface.
- Claim runtime governance enforcement from docs or unit tests alone.
- Request a GC-023 file-size exception before attempting a responsibility split.
- Modify public-facing claims before evidence exists.
- Start implementation before roadmap-ready packet approval.

---

## 8. Approval Gate

Operator approval required:

```text
APPROVE CVF_GC018_MODEL_GATEWAY_RUNTIME_AUTHORIZATION_2026-05-16
```

Equivalent approval may approve the whole roadmap-ready packet by name. Until
that approval is given, runtime code implementation remains blocked.
