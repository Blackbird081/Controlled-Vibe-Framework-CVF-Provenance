# CVF Implementation-First Absorption Pattern

## Purpose

Binding guidance for all CVF agents deciding whether to build a CVF module first (Hướng B)
or build a concrete product implementation first then absorb into CVF later (Hướng A).
Operator-confirmed 2026-06-08 based on Policy_Local Gap 4 context.

## Scope / Applies To

- All agents dispatched to add new capabilities to CVF L2–L5 layers
- All decisions about whether to build a generic CVF module before concrete product evidence exists
- All LHW absorption wave dispatch decisions

Memory class: FULL

**Authored:** 2026-06-08  
**Status:** OPERATOR_CONFIRMED  

## Claim Boundary

- Claims in this document are operator-confirmed governance guidance, not technical assertions
- No runtime or code behavior claims — this is a process standard, not a source reference
- The absorption trigger conditions are normative (must be met before opening GC-018)
- Evidence paths listed in the "absorbable now" table are source-verified as of 2026-06-08

---

## Decision

**Hướng A confirmed:** Build concrete product implementation first → absorb proven
pattern into CVF after evidence exists.

Operator statement (2026-06-08):
> "Chúng ta sẽ tiến hành Hướng A: Policy_Local trước → absorb lên CVF sau"

---

## The Two Patterns Evaluated

### Hướng A — Implementation First, Absorb Later (CHOSEN)

```
Concrete product (e.g. Policy_Local)
  → build, test, fail fast, iterate
  → proven in production with real domain data
  → abstract pattern → CVF LHW absorption wave
  → CVF rule/module written from observed evidence
```

### Hướng B — CVF First, Products Inherit

```
CVF generic module (abstract)
  → product uses it like existing L1/L2 layers
  → consistent from day 1
  → but: over-engineered before any evidence exists
```

---

## Why Hướng A Is Correct for CVF

### 1. CVF's own philosophy supports it

CVF Agent Error → Governance Learning states:
> *"If a defect pattern repeats, promote it into a written rule.
> If the rule can still be interpreted loosely, promote it into a machine check."*

The inverse applies to capabilities:
> **Do not write a governance rule before the behavior exists to govern.**

A CVF module built before any concrete product uses it is speculative governance —
it anticipates failure modes instead of observing them.

### 2. Domain knowledge cannot be abstracted prematurely

Policy_Local Gap 4 (semantic search) requires:
- Vietnamese diacritic normalization behavior under embedding
- Legal terminology chunk boundaries (articles, clauses)
- Optimal chunk size for Vietnamese legal prose (~1800 chars)
- Freshness status interaction with retrieval ranking

None of these are knowable without running against real Vietnamese legal corpus.
A CVF L2 generic module built before this evidence would be tuned for a
hypothetical consumer, not an observed one.

### 3. Governance overhead cost is real

Building a CVF module requires: GC-018 authorization, blind-spot control block,
corpus completeness verification, source verification table, work order, review.
This is appropriate for proven patterns — premature for unproven ones.

Timeline comparison for Gap 4 example:
- Policy_Local T1–T3 (focused): ~2.5 days, Fast Lane audit
- CVF L2 module (generic): ~2–3 weeks governance + build, blocks Policy_Local

### 4. The decision threshold

| Scenario | Correct pattern |
|---|---|
| Next product needing same capability in **1–2 months** | Consider Hướng B |
| Next product in **6+ months** or uncertain | Hướng A — proven first |
| Domain-specific knowledge required | Always Hướng A first |

---

## Absorption Trigger Conditions

An implementation is ready to absorb into CVF when ALL of the following are true:

1. **Shipped and stable** — running in production, not a prototype
2. **Evidence exists** — benchmark data, failure modes documented, edge cases known
3. **Second consumer identified** — at least one other product would use the abstraction
4. **Pattern is generalizable** — domain-specific details can be separated from core logic

When these conditions are met, open a GC-018 to dispatch an LHW absorption wave.
Do NOT absorb speculatively — wait for the trigger conditions.

---

## Current Application: Policy_Local Gap 4

**Status:** Gap 4 roadmap written (`docs/GAP4_SEMANTIC_SEARCH_ROADMAP.md` in
Policy_Local repo), T1–T3 not yet built.

**Absorption path (future):**
```
Policy_Local Gap 4 T1–T3 (proven)
    │
    ▼  trigger: shipped + stable + second consumer identified
GC-018 dispatch: "CVF-LHW-EMBEDDING: local embedding hybrid retrieval"
    │
    ▼
CVF L2 RAG Pipeline module upgrade
  - embedder.ts pattern → CVF L2 generic embedder contract
  - vec-store.ts pattern → CVF L2 vector store adapter
  - RRF fusion → CVF retrieval standard
    │
    ▼
Future products (Policy_Finance, Policy_HR, ...) inherit from CVF L2
```

**Do not open the GC-018 until Policy_Local T1–T3 is shipped and stable.**

---

## What Policy_Local Has Already Proven (absorbable now)

These patterns from Policy_Local are already evidence-backed and generalizable:

| Pattern | Source | CVF absorption target |
|---|---|---|
| 6-provider LLM adapter (OpenAI-compatible + Anthropic + Gemini) | `api/llm/route.ts` | CVF L5 Adapter Hub |
| API key masked storage (DB persist, last-4 display) | `api/settings/route.ts` | CVF credential management standard |
| EC-02 date-aware disclosure (promulgation vs effective date) | `ec02-exception.md` | CVF governance rule candidate |
| RAG grounded system prompt pattern | `api/llm/route.ts` | CVF L2 RAG Pipeline |
| Per-query receipt with freshnessDisclosureApplied flag | `lib/search.ts` | CVF audit trail standard |

These can be referenced in future LHW absorption waves without waiting for Gap 4.

---

## Guidance for Future Agents

When you encounter a request to "add X capability to CVF":

1. **Check if a concrete product already implements X** — if yes, absorb from evidence
2. **Check absorption trigger conditions** — all 4 must be true before opening GC-018
3. **Do not build CVF module speculatively** — wait for observed behavior
4. **Fast Lane is sufficient** for product-level implementation (GC-021)
5. **GC-018 is required** for CVF-level absorption (governance overhead is intentional)

The goal is CVF rules that reflect reality, not CVF rules that predict it.
