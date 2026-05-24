# CVF Review-CVF Residual Closure Roadmap — Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED — MIXED_NON_BLOCKING_WITH_BLOCKING_FINDINGS

Reviewer: Codex

Date: 2026-05-19

Reviewed artifacts:

- `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`
- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md`

Static review base:

- Claude filing anchor: `71829253`
- Current local HEAD during rebuttal: `7f7ca6de`
- `71829253` is an ancestor of current HEAD.

---

## Purpose

Provide the Codex rebuttal requested by the active handoff before any
Review-CVF residual candidate proceeds to GC-018 or implementation.

This rebuttal checks Claude's residual assessment and closure roadmap against
current working-tree evidence. It does not authorize implementation, does not
file GC-018, and does not change public claims.

---

## Scope / Target / Owner Boundary

In scope:

- Static rebuttal of the predecessor assessment and residual closure roadmap.
- Verification of the six candidates A1, C1, D1, E1, G1, and H1 against
  current working-tree evidence.
- Per-candidate verdicts before any GC-018 or work order.

Out of scope:

- Editing Claude's assessment or roadmap directly.
- Filing GC-018 baselines.
- Implementing CLI, provider, benchmark, role-catalog, freeze-doc, or memory
  tier changes.
- Public-sync edits or public claim changes.

Owner:

- Codex holds reviewer authority for this rebuttal packet.
- Orchestrator or operator may revise the roadmap after this packet.
- Worker implementation remains blocked until the relevant downstream GC-018
  is authorized.

---

## Target / Source Under Review

Primary target:

- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md`

Predecessor source:

- `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`

Original audit source:

- `.private_reference/legacy/CVF 17.05/Review CVF.md`

Supporting current-state files:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`

---

## Scope / Methodology

Method:

1. Resolve the active session handoff and review the two Claude artifacts.
2. Check whether the Claude filing anchor `71829253` is an ancestor of the
   current local HEAD.
3. Use direct repository search to verify cited command names, contract files,
   metrics, governed-pack policy fields, role-catalog paths, freeze-doc paths,
   and memory-contract surfaces.
4. Compare each candidate against active session boundaries and the roadmap's
   own sequencing rules.
5. Return per-candidate verdicts without modifying implementation files.

No live API call, release gate, or test suite is required because this is a
static rebuttal artifact.

---

## Executive Verdict

Claude's roadmap is directionally useful, but the filing is not clean enough
to dispatch as-is.

The assessment's headline verdict is not accurate as written. It says `5 of
8 pain points are CLOSED` and places Problem E in the CLOSED group, but the
Problem E section itself says `Verdict: PARTIAL` because four audit-named
metrics still have no compute path. The corrected static score is:

- CLOSED: B, D, F, G-runtime-surface
- PARTIAL: A, C, E, H
- OPEN: none found

Problem G may remain treated as runtime-closed, but the role-catalog residual
must be described as a catalog absorption residual, not as evidence that the
full execution-identity ask is already complete.

Roadmap disposition:

| Candidate | Codex verdict | Reason |
| --- | --- | --- |
| A1 | NON_BLOCKING | Correctly requires a GC-018 necessity audit before authoring or rejecting freeze docs. |
| C1 | BLOCKING_FINDINGS | The candidate says no GC-018 is required, contradicting the roadmap's own all-candidate gate and under-scoping new CLI verbs. |
| D1 | NON_BLOCKING_WITH_GATE_UPDATE | Decision-baseline shape is sound; prerequisite must cite the completed D2/W1 evidence or remain held. |
| E1 | NON_BLOCKING_AFTER_ASSESSMENT_FIX | Schema-first metric expansion is sound; assessment must mark Problem E PARTIAL overall. |
| G1 | NON_BLOCKING | Absorption-only role catalog is bounded if re-authored and runtime gate remains unchanged. |
| H1 | NON_BLOCKING_WITH_GATE_UPDATE | Single-path tier contract decision is sound; prerequisite must cite completed H2 evidence or remain held. |

At least one candidate is NON_BLOCKING, so the roadmap need not be rejected in
full. Candidate C1 must be revised before it can proceed.

---

## Evidence Checks

Static checks passed:

- `git merge-base --is-ancestor 71829253 HEAD` confirms the filing anchor is
  not ahead of current HEAD.
- The provider contract files exist for complete, stream, tool call,
  reasoning, JSON mode, vision, embedding, and receipt surfaces under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/`.
- `retry-contract.ts`, `cost-contract.ts`, and `risk-contract.ts` do not
  exist as parallel gateway method contracts.
- `command.registry.ts` registers `help`, `version`, `status`, `evaluate`,
  `execute`, `benchmark`, `session`, `report`, and `audit`; it does not
  register `run`, `skill`, `receipt`, `trace`, or `provider`.
- `governance-reliability-metrics.ts` exports nine current metric functions
  and does not define hallucination recovery, human correction, long-horizon
  stability, or rollback-success metrics.
- The three governed pack policy files carry
  `allowedActorRoles: ["OPERATOR", "BUILDER", "REVIEWER", "SERVICE_AGENT"]`
  and `streamingEnabled: false`.
- No canonical `docs/reference/CVF_AGENT_ROLE_CATALOG.md` exists. The only
  role catalog found is the legacy private-reference source.
- No `CVF_KERNEL_LAW.md`, `CVF_CORE_ONTOLOGY.md`,
  `CVF_RUNTIME_AUTHORITY_MODEL.md`, or `CVF_EXECUTION_STATE_MODEL.md` exists.

---

## Blocking Finding 1 — Problem E Is Mis-scored In The Assessment

Severity: BLOCKING_FOR_ASSESSMENT_HEADLINE

The assessment's executive verdict claims:

- `5 of 8 pain points are CLOSED`
- `3 of 8 are PARTIAL`
- Problem E is treated as CLOSED in the summary narrative.

But the Problem E section states:

- `Verdict: PARTIAL`
- missing metrics: hallucination recovery, human correction count,
  long-horizon stability, rollback success.

The roadmap also includes E1 as a residual candidate, which confirms E is not
closed overall. The correct posture is `Problem E: PARTIAL, schema-first
metric residual`.

Required correction:

- Revise any downstream status language that says E is CLOSED.
- Keep E1 in the roadmap.
- Do not claim `5/8 CLOSED` unless E is explicitly excluded from the residual
  count as "closed for current nine-function surface only," which is too
  narrow for the 17.05 audit ask.

---

## Blocking Finding 2 — C1 Contradicts The Roadmap's Own GC-018 Rule

Severity: BLOCKING_FOR_C1

Candidate C1 says:

- `GC-018 required: No`
- all five verbs are read-only wrappers with no new I/O surface.

The same roadmap later says:

- no candidate proceeds to GC-018 filing until Codex rebuttal returns
  NON_BLOCKING;
- skipping GC-018 for any candidate is forbidden.

This is an internal process contradiction. It is also under-scoped: adding
five canonical CLI verbs changes the public command surface of the governance
CLI. Even if the handlers are read-only, `trace dump`, `receipt show`,
`provider list`, and `skill list|show` still need named source paths, input
shape, error behavior, and tests. Some will necessarily read existing files,
registries, or logs, so "no new I/O surface" is not a safe claim.

Required correction:

- Mark C1 as `GC-018 required: Yes`, or remove C1 from this roadmap.
- The GC-018 must name the exact backing source for each verb.
- `cvf run` may remain an alias to `execute`, but it must not imply a new
  runtime path.
- `receipt`, `trace`, `skill`, and `provider` must be read-only and must not
  add mutation, network provider calls, or new auth paths.

Until revised, C1 is BLOCKED.

---

## Candidate A1 — Non-Blocking

A1 is acceptable because it is framed as a decision candidate rather than a
pre-committed documentation build.

Required downstream guard:

- The GC-018 must cite specific guards and the exact behavior they enforce.
- It must pick one outcome: contract-closure or explicit-rejection.
- It must not author `CVF_KERNEL_LAW.md`, `CVF_CORE_ONTOLOGY.md`,
  `CVF_RUNTIME_AUTHORITY_MODEL.md`, or `CVF_EXECUTION_STATE_MODEL.md` before
  the necessity audit is complete.

Verdict: NON_BLOCKING.

---

## Candidate D1 — Non-Blocking With Gate Update

D1 is correctly framed as a per-method decision for `retry()`, `cost()`, and
`risk()`. Current evidence supports Claude's residual: the eight other method
surfaces exist, while those three do not exist as gateway contract files.

The prerequisite language is stale if it depends on the original CDH rebuttal
returning NON_BLOCKING. The original CDH rebuttal was BLOCKING, while later
delta work closed W1/D2. D1 must cite the completed W1/D2 closure evidence or
remain held.

Required downstream guard:

- Do not touch `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`.
- For each of retry, cost, and risk, choose contract-closure or
  explicit-rejection.
- If rejecting a contract file, name the existing policy, routing, fallback,
  quota, or risk surface that owns the semantic.

Verdict: NON_BLOCKING_WITH_GATE_UPDATE.

---

## Candidate E1 — Non-Blocking After Assessment Fix

E1 addresses the right failure mode: compute-without-data. The schema-first
structure is correct, and hallucination recovery is correctly rejected instead
of claimed through LLM judging.

Required downstream guard:

- Fix the assessment status so Problem E is PARTIAL overall.
- Keep the benchmark offline-only.
- Add upstream event fields before metric functions.
- If the audit asks for "human correction count," the output must preserve
  count semantics even if the metric result also includes a rate.

Verdict: NON_BLOCKING_AFTER_ASSESSMENT_FIX.

---

## Candidate G1 — Non-Blocking

G1 is bounded if it remains an absorption/reference-doc task. Current runtime
evidence supports the allowed-actor role gate; the remaining gap is catalog
formalization.

Required downstream guard:

- Re-author the legacy role catalog; do not copy private-reference text.
- Introduce no new role IDs.
- Do not redesign RBAC.
- Do not replace pack-policy `allowedActorRoles` as the runtime source.
- Runtime code should remain unchanged unless the catalog audit finds a
  concrete mismatch.

Verdict: NON_BLOCKING.

---

## Candidate H1 — Non-Blocking With Gate Update

H1 correctly requires choosing exactly one path: five tier-specific contracts
or one classifier contract. It also correctly avoids runtime wiring.

The prerequisite language is stale if it depends on the original CDH rebuttal
returning NON_BLOCKING. The original CDH rebuttal was BLOCKING, while later H2
work closed audit-memory policy refinement. H1 must cite the completed H2
evidence or remain held.

Required downstream guard:

- Choose exactly one path in GC-018.
- Do not ship both typed-per-tier contracts and a classifier contract.
- Do not claim runtime data flow, provider prompt reinjection, or
  organizational memory runtime.
- Record the rejected path and rationale in the closure review.

Verdict: NON_BLOCKING_WITH_GATE_UPDATE.

---

## Findings / Position

Position: the residual closure roadmap should continue, but only as a revised
or explicitly caveated packet.

Findings:

1. The predecessor assessment mis-scores Problem E in its executive headline.
2. C1 is internally inconsistent because it waives GC-018 while the roadmap
   forbids skipping GC-018 for any candidate.
3. C1 under-describes the source and I/O boundary for five new canonical CLI
   verbs.
4. D1 and H1 are directionally sound, but their prerequisite language should
   cite completed delta closure evidence or remain held.
5. A1, E1, and G1 are appropriately bounded if their downstream GC-018 files
   preserve the decision/absorption/schema-first boundaries.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Assessment overclaims `5/8 CLOSED` and hides the E residual | Mark Problem E PARTIAL overall before using the assessment as a closure baseline |
| C1 proceeds without GC-018 because it is described as read-only | Require GC-018 for C1 or hold it out of the tranche |
| New CLI verbs accidentally become mutation, network, or auth surfaces | Name each verb's backing source, input shape, and forbidden behaviors in GC-018 |
| D1/H1 start from stale CDH prerequisites | Cite completed W1/D2/H2 delta closure evidence, or keep the candidate held |
| A1 freeze docs become governance theatre | Require specific guard-chain comparison before authoring or rejecting named files |

---

## Decision / Disposition

Disposition: MIXED.

The roadmap is not rejected in full. A1, E1, G1, D1, and H1 are usable after
the corrections above. C1 is blocked as drafted and must be revised before any
GC-018 or implementation work.

No GC-018 may be filed from the current roadmap until:

1. The Problem E scoring contradiction is corrected in the assessment or
   explicitly acknowledged in the candidate's GC-018.
2. C1 is revised to require GC-018, or C1 is held out of the tranche.
3. D1/H1 prerequisite language is updated to cite the completed delta closure
   evidence, or those candidates remain held.

---

## Claim Boundary

This rebuttal is static review evidence only. It does not authorize
implementation, live proof, public-sync changes, new governance semantics, new
memory tiers, new provider execution behavior, or public claims of a coherent
governed capability runtime.
