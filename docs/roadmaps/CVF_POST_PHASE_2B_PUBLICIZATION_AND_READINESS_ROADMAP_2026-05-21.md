# CVF Post Phase 2.B Publicization And Readiness Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PUBLICIZATION_READINESS_BOUNDED

docType: roadmap

Date: 2026-05-21

---

## Purpose

Define the next publicization and product-readiness sequence after Phase 2.B
static migration, bounded adapter coverage, runtime coherence, and one narrow
live governance proof have closed.

The operating principle is: publicize only what is already proven, and make the
next proof as small as possible before widening any claim.

---

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Phase 2.B static migration plan:
  `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- Runtime coherence completion:
  `docs/reviews/CVF_PHASE_2B_RUNTIME_COHERENCE_COMPLETION_2026-05-21.md`
- Live governance proof completion:
  `docs/reviews/CVF_PHASE_2B_LIVE_GOVERNANCE_PROOF_COMPLETION_2026-05-21.md`
- Governance kernel owner map:
  `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- Governance kernel freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- Public repository boundary:
  `AGENTS.md`

---

## Authorization / Decision

Operator decision on 2026-05-21:

- Public-facing work should proceed only as far as the evidence supports.
- Five next-value areas should receive a roadmap:
  provider stability, public-sync/public catalog, product readiness,
  persistence/database, and Maika proof.
- Kernel-owner replacement and global freeze lift are not current work. They
  should be recorded as deferred condition-gated items only.

This roadmap is closed by
`docs/reviews/CVF_POST_PHASE_2B_PUBLICIZATION_READINESS_COMPLETION_2026-05-21.md`.
The closure authorizes only the bounded evidence and public-safe summary
recorded there. It does not authorize persistence changes, Maika changes,
provider runtime expansion, owner replacement, or freeze release.

---

## Scope

In scope:

- Roadmapping the five operator-selected value areas after Phase 2.B closure.
- Defining the recommended order for bounded publicization.
- Recording the evidence ceiling for current public-facing claims.
- Recording kernel-owner replacement and global freeze lift as deferred
  condition-gated items.
- Updating active session pointers so future agents load this roadmap before
  selecting publicization work.

Out of scope:

- Implementing any provider, product, public-sync, persistence, database, or
  Maika change.
- Filing lane-specific GC-018 packets or work orders.
- Editing the public-sync clone.
- Changing kernel ownership.
- Releasing any frozen governance-kernel surface.

---

## Non-Goals

- Do not claim broad provider stability from the one existing live proof.
- Do not update the public repository from the private provenance workspace.
- Do not introduce a persistence/database default before a concrete
  operational need is proven.
- Do not use Maika child-data/photo/vision proof as an implied consequence of
  text-summary proof.
- Do not replace kernel owners without the freeze-release process.
- Do not lift the global freeze; the current rule rejects global release.

---

## Current Closure Baseline

Closed before this roadmap:

| Surface | Current status | Boundary |
| --- | --- | --- |
| Phase 2.B static plan | `CLOSED_STATIC_MIGRATION_PLAN_LOCKED` | planning/dispatch only |
| Phase 2.B bounded adapter coverage | 46 primary rows covered through bounded slices | no broad bulk migration claim |
| Runtime coherence | `CLOSED_RUNTIME_COHERENCE_INTERNAL_PROOF` | deterministic internal proof only |
| Live governance proof | `CLOSED_LIVE_GOVERNANCE_PROOF` | one Alibaba `/api/execute` proof only |

Current live proof facts:

- Provider lane: `alibaba`.
- Model: `qwen-turbo`.
- Decision/routing decision: `ALLOW`.
- Receipt id: `rcpt-env-mpepcnmc-ier7bt`.
- Trace id: `env-mpepcnmc-ier7bt`.
- Runtime coherence checksum: `fnv1a32:5d3d2dac`.

Current public claim ceiling:

CVF can honestly claim private provenance evidence for a bounded internal
Phase 2.B coherence graph and one live governed `/api/execute` route proof.

It cannot yet claim broad provider stability, all-provider behavior, Maika
child-data/photo/vision proof, persistence/database production readiness,
public product readiness, kernel-owner replacement, or global freeze lift.

---

## Sequencing Principle

The five active roadmap areas are intentionally not equal priority.

Recommended sequence:

1. Provider stability, scoped narrowly.
2. Product readiness assessment.
3. Public-sync/public catalog update with only bounded claims.
4. Persistence/database decision only if readiness identifies an operational
   blocker.
5. Maika proof only if Maika is the chosen demo/customer path.

Items 4 and 5 are demand-gated. They are real product-value areas, but they
should not block a bounded public claim for already-proven Phase 2.B evidence.

---

## PBR-01 - Narrow Provider Stability

Intent: convert the current one-shot live proof into a small repeatability
proof without pretending to prove every provider or workload.

Scope:

- Multi-journey live governance proof on the existing governed `/api/execute`
  path.
- At minimum, replay Alibaba and DeepSeek lanes if live keys are available.
- Verify repeated receipt creation, non-mock evidence mode, no direct provider
  bypass, no raw secret output, and clean timeout diagnostics.
- Include the mandatory live release gate or an explicitly stricter successor.

Non-goals:

- No broad provider benchmark.
- No all-model parity claim.
- No provider method expansion.
- No Maika proof.
- No public claim until PBR-03.

Acceptance criteria:

- A GC-018/work order defines exact providers, journey count, timeout budget,
  and stop conditions.
- Live keys are loaded only from approved operator secret sources.
- Each successful journey records provider, model, decision, receipt id, trace
  id, and evidence mode.
- Failure cases are classified honestly as provider/runtime stability defects,
  not converted into passing public evidence.

Suggested disposition after completion:

- If stable: allow product-readiness assessment to cite bounded two-lane or
  one-lane stability, depending on actual results.
- If unstable: file a provider/runtime stability remediation roadmap before
  any public stability claim.

---

## PBR-02 - Product Readiness Assessment

Intent: decide what CVF can safely present as a product now, before updating
public-facing material.

Scope:

- Review private provenance evidence against public-product claims.
- Classify claims as `public_ready`, `private_evidence_only`,
  `demo_only`, `blocked`, or `deferred`.
- Identify the smallest public front door language that is true today.
- Identify release blockers for hosted/product operation.

Non-goals:

- No code implementation.
- No public-sync edits.
- No new live proof unless PBR-01 has not produced enough evidence.
- No freeze release.

Acceptance criteria:

- A readiness packet lists allowed claims and forbidden claims.
- The packet cites exact evidence for each allowed claim.
- The packet names any live proof or catalog update that must happen before a
  broader claim.
- The packet explicitly decides whether PBR-04 or PBR-05 is needed before a
  public update.

Suggested disposition after completion:

- If public-ready claim language exists, proceed to PBR-03.
- If not, return to the smallest blocking proof rather than widening public
  claims.

---

## PBR-03 - Public-Sync / Public Catalog Update

Intent: update the public repository only with claims that PBR-02 authorizes.

Scope:

- Work only from the public-sync clone:
  `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`.
- Run `git remote -v` before any public push.
- Update public catalog, README, or evidence summary only if the claim is
  supported by private provenance evidence and PBR-02.
- Use narrow language such as bounded Phase 2.B coherence and one live governed
  route proof unless PBR-01 proves more.

Non-goals:

- Do not push the private provenance tree.
- Do not expose private evidence packets, raw traces, secrets, or operator
  environment details.
- Do not claim broad provider stability unless PBR-01 proves it.
- Do not claim production readiness unless PBR-02 approves it.

Acceptance criteria:

- Public-sync remote points to
  `Controlled-Vibe-Framework-CVF.git`, not the provenance repository.
- Public-facing claim text maps one-to-one to closed evidence.
- A public commit SHA is recorded in the provenance completion packet.
- Any public catalog advisory is resolved or explicitly marked N/A with
  rationale.

---

## PBR-04 - Persistence / Database Decision

Intent: avoid accidental database work while preserving a path to real
operator-grade audit retention when needed.

Scope:

- Start with an ADR or readiness-linked decision, not a schema migration.
- Decide whether current file/browser-local persistence is enough for the
  public claim selected in PBR-02.
- If not enough, choose the smallest persistence layer for the identified
  need, with retention, redaction, recovery, and operator access boundaries.

Non-goals:

- No default Supabase/Postgres posture without a separate decision.
- No database schema migration in the roadmap-only step.
- No persistent memory tier expansion.
- No reinjection behavior.
- No storage of raw secrets or unredacted child/sensitive data.

Acceptance criteria:

- A concrete operational need exists: audit retention, multi-user review,
  cross-session recovery, hosted ops, or compliance evidence.
- The ADR names what data is persisted, what is redacted before persistence,
  retention policy, failure mode, and migration/rollback path.
- Any implementation requires a separate GC-018/work order and tests.

Suggested disposition after completion:

- If no operational need is proven, keep persistence/database deferred.
- If a need is proven, implement only the selected persistence slice.

---

## PBR-05 - Maika Proof Demand Gate

Intent: use Maika as product proof only when it is truly the selected product
path, and keep child-data/privacy risk ahead of demo pressure.

Scope:

- Start with a demand gate: confirm whether Maika is the current public demo,
  customer proof, or operator priority.
- If yes, split proof types:
  - text-summary proof;
  - child-data minimization proof;
  - photo/vision proof only if explicitly required.
- Require authenticated Supabase/admin/teacher invocation where applicable.
- Require minimized payload evidence, redaction evidence, CVF receipt/audit
  evidence, and no direct provider fallback.

Non-goals:

- No child-data/photo/vision proof by implication.
- No direct provider fallback.
- No raw abnormal health or sensitive child payload in docs.
- No vision runtime claim from contract-only evidence.
- No public Maika claim until the exact Maika proof is closed.

Acceptance criteria:

- A Maika work order identifies the consuming surface and the exact data class.
- The proof path records CVF governance receipt/audit evidence.
- Redaction/minimization is proven before provider call and before persistence
  or public display.
- Photo/vision proof is separated from text-summary proof and needs its own
  live provider evidence.

Suggested disposition after completion:

- If Maika is not the current product path, keep this deferred.
- If Maika is current, begin with text-summary continuity before any
  photo/vision expansion.

---

## Deferred Condition Register

### D-06 - Kernel-Owner Replacement

Current decision: do not proceed.

Reason:

- The HN2.b owner map is authoritative.
- No current blocked work order proves owner replacement is necessary.
- Owner replacement touches frozen governance-kernel surfaces and carries high
  semantic drift risk.

May proceed only when all conditions hold:

- A concrete blocked work order or external pain point proves the current owner
  map causes harm.
- The proposed change targets exactly one owner-map surface.
- A replacement design maps every affected alias.
- A fresh GC-018 and work order cite the owner-map row.
- A different-role reviewer returns a non-blocking rebuttal.
- The operator explicitly approves the per-surface release.

### D-07 - Global Freeze Lift

Current decision: do not proceed.

Reason:

- The binding freeze-release rule explicitly rejects global release.
- Global lift would weaken the governance boundary created by HN2.b/HN2.c.
- Useful future work can proceed through normal GC-018 or per-surface release
  without lifting the whole freeze.

May proceed only if a later doctrine-compatible rule supersedes the current
freeze-release rule. Until then, only one-surface release packets are allowed.

---

## Required Future Work Orders

This roadmap does not itself open implementation. Future work should be split
as follows:

| id | future artifact | required before implementation |
| --- | --- | --- |
| PBR-01 | Provider stability GC-018/work order | exact providers, journeys, live-key requirements, stop conditions |
| PBR-02 | Product readiness review work order | evidence map and public-claim rubric |
| PBR-03 | Public-sync GC-024/work order | public-sync remote verification and approved claim text |
| PBR-04 | Persistence/database ADR | operational need and data-retention boundary |
| PBR-05 | Maika proof GC-018/work order | consuming surface, data class, privacy controls, live proof path |
| D-06 | One-surface release packet | all freeze-release conditions |
| D-07 | Not allowed under current rule | doctrine-compatible supersession required |

---

## Work Plan

1. File this roadmap and queue it as `READY_FOR_REBUTTAL`.
2. Ask a reviewer or later Codex pass to accept, narrow, or reorder the five
   active lanes.
3. If accepted, execute PBR-01 first through a dedicated GC-018/work order.
4. Use PBR-01 results to drive PBR-02 product readiness assessment.
5. Use PBR-02 allowed-claim language to decide whether PBR-03 public-sync work
   should proceed.
6. Start PBR-04 only if PBR-02 identifies persistence/database as a real
   public/product blocker.
7. Start PBR-05 only if the operator selects Maika as the current demo or
   customer proof path.
8. Keep D-06 and D-07 deferred unless their listed conditions are met.

---

## Acceptance Criteria

This roadmap is accepted only if:

- It preserves the current evidence ceiling for Phase 2.B.
- It keeps public-sync work in the public-sync clone.
- It orders public-facing claims after readiness assessment or equivalent
  evidence review.
- It treats persistence/database and Maika proof as demand-gated, not mandatory
  blockers.
- It records kernel-owner replacement as one-surface release work only.
- It records global freeze lift as rejected under the current binding rule.
- It does not authorize implementation without later lane-specific artifacts.

---

## Verification / Evidence Expectations

Common verification:

- `python governance/compat/check_active_session_state.py --enforce`
- `python governance/compat/check_docs_governance_compat.py`
- `python governance/compat/check_markdown_structural_completeness.py`

Live governance or public claim verification:

- `python scripts/run_cvf_release_gate_bundle.py --json`
- focused live proof wrappers as needed, with no raw secret output.

Public-sync verification:

- `git remote -v` in the public-sync clone before push.
- public commit SHA recorded back in provenance.

---

## Exit Condition

This roadmap is complete when an independent rebuttal or operator follow-up
selects the first active lane and confirms the deferred posture for D-06 and
D-07.

Implementation completion belongs to the future lane-specific completion
reviews, not this roadmap.

---

## Claim Boundary

This roadmap authorizes planning only.

It does not close or claim broad provider stability, public product readiness,
public catalog update, persistence/database production readiness, Maika proof,
kernel-owner replacement, or freeze release.
