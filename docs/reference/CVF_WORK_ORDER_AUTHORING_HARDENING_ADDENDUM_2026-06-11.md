# CVF Work Order Authoring Hardening Addendum

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

Date: 2026-06-11

Owner: CVF governance control plane

---

## Purpose

This addendum keeps the canonical work-order template compact while preserving
the detailed authoring rules promoted from EX-T1 review findings.

It is binding when referenced by:

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`;
- local governance hook-chain checks.

---

## Scope / Target / Owner Boundary

Target owner surfaces:

- work-order authoring;
- worker return packet structure;
- closure package row and status discipline;
- runtime freshness non-use claim wording;
- parent roadmap versus child closure status wording.

Owner boundary:

- reference-only authoring discipline;
- no runtime implementation authority;
- no provider/API key use;
- no public-sync or release authority;
- no autonomous rule mutation.

---

## Scope / Applies-To

This addendum applies to future governed work orders, worker returns,
completion reviews, and roadmap-derived closure packets when they rely on the
canonical work-order template.

It does not replace the canonical template or closure-quality standard. It
extracts detailed rules from the template so the template can remain below its
governed file-size threshold.

---

## Minimum Worker Return Structural Shell

Worker returns for governed work must include:

- `## Purpose`
- `## Scope / Target / Owner Boundary`
- `## Pre-Flight Evidence`
- `## Changed File List`
- `## Reviewer-Fast Gate` or `## Governance Gates Run`
- `## Findings / Position`
- `## Risk / Corrective Action`
- `## Finding-To-Governance Learning Disposition` when the worker return
  records findings, defects, known issues, risks, quality gaps, or gate
  blockers
- `## Claim Boundary`
- `## Public Export Disposition`

The shell may include additional domain-specific sections, but it must not
drop the reviewer-facing sections above when the packet asks an orchestrator to
review, close, or commit the work.

---

## Pseudo-Path Discipline

Worker returns, work orders, reviews, and completion packets must not use
pseudo-path shorthand such as a top-level extension directory followed by a
generic source directory, or an invented docs glob, unless that exact path or
glob is an intentional manifest pattern.

Use real repo paths inside backticks when citing a source surface. Use prose
such as "runtime source tree" when no concrete path is being cited.

---

## Machine Closure Package Authoring Rules

Machine Closure Package row names are exact machine tokens. Use:

- `Work order status`
- `Completion or reviewer artifact`
- `Roadmap state`
- `Registry JSON`
- `Registry Markdown`
- `External evidence digest`
- `System loop interlock`
- `Session continuity`

Do not rename `Registry JSON` to `Corpus scan registry JSON` or
`Registry Markdown` to `Corpus scan registry MD`.

`Final status` values must be checker-accepted:

- `PASS`
- `BLOCKED`
- `N/A with reason`

Do not use `N/A_WITH_REASON` in the final status cell.

If corpus, search, classification, or readiness state appears in a
closed-equivalent artifact, `Registry JSON` and `Registry Markdown` must be
`PASS` or `BLOCKED with reason`; do not mark them `N/A with reason`.

If `External evidence digest` is `PASS` and references external evidence, the
row or the External Artifact Hash Manifest must include at least one
`sha256:<hex>` digest.

---

## Parent Roadmap Versus Child Closure Status

Parent roadmaps that remain open for later child lanes must not use `CLOSED` in
the top-level `Status` merely because one child lane passed.

Use child-lane wording such as `EX_T1_PASS_BOUNDED` in the parent roadmap.
Reserve `CLOSED_PASS_BOUNDED` for the child work order, completion review, or a
fully closed roadmap.

---

## Runtime Freshness Non-Use Claims

If a work order claims a runtime/source capability is absent, not implemented,
hardcoded, per-role only, stale, missing, or intentionally not used in the
current lane, include a `Current Runtime Freshness Verification` section before
dispatch.

Examples include:

- "no provider/API key use"
- "no provider calls"
- "no runtime/source edits"
- "no registry update" when current runtime/source owners exist

The verification section must show the repo searches or source files checked
and must cite current owner paths for any partial implementation surface found.

---

## Prior Verification Reuse And Unicode Evidence Handling

Work orders that consume a prior manifest, source bundle, external evidence
digest, T11B-style verification result, or Unicode-path extracted text must
include an `Evidence Reuse And Encoding Plan`.

Canonical standard:

`docs/reference/CVF_PRIOR_VERIFICATION_REUSE_AND_UNICODE_EVIDENCE_HANDLING_STANDARD_2026-06-11.md`

The plan must choose exactly one verification mode:

- `REUSE_PRIOR_VERIFICATION`
- `RECOMPUTE_REQUIRED`
- `REVIEWER_RECOMPUTE_ONLY`

If prior verification already proves path existence, hash match, size match,
and lineage/role match for the same source identity, the default mode is
`REUSE_PRIOR_VERIFICATION`. A work order may require fresh recomputation only
when it records the concrete gap or drift reason.

When cited paths contain non-ASCII characters, the plan must require literal
paths and UTF-8-safe readers. Do not rename, normalize, or copy evidence files
merely to make a shell command easier unless a separate governed task
authorizes that mutation.

---

## Negative Search And Collision Discipline

If a source-verification row, baseline, roadmap, work order, or completion
packet claims a token, field, enum, schema key, failure token, or config key is
`NOT FOUND`, the artifact must include:

- exact search roots;
- exact search command or structured query;
- whether the search covered source, tests, docs, JSON, and external evidence;
- same-token collision results, if any;
- a disposition that separates "same token exists with different meaning" from
  "token absent".

Do not write `NOT FOUND` when a same-token occurrence exists in a test fixture,
generic metadata surface, archived contract, or docs proposal. Record it as a
collision or non-authoritative occurrence, then state why it is or is not
binding for the current work.

This rule is promoted from the EC-T1 closure finding where
`documentStatus` existed in a DSCP-T10 company-docs test fixture but was first
claimed as absent from EXTENSIONS. Future EC-T2 work must carry forward that
collision instead of rediscovering it during implementation.

---

## Export Surface Decision

Work orders and completion packets that create, modify, or rely on foundation
helpers, adapters, contracts, barrels, registries, or reusable source surfaces
for later tranche consumption must include an `Export Surface Decision`.

Allowed decisions:

- `Export Surface Decision: EXPORTED`
- `Export Surface Decision: INTERNAL_ONLY with reason`
- `Export Surface Decision: BLOCKED`

`EXPORTED` requires:

- owner barrel, index, or documented import path;
- focused test or import proof when runtime/source is in scope;
- explicit downstream consumer boundary.

`INTERNAL_ONLY with reason` requires:

- reason the helper is intentionally not exported;
- statement that downstream work orders must not import or rely on it.

`BLOCKED` stops dispatch or closure until the export decision is resolved. Do
not leave export intent implicit for a later worker to infer.

---

## Next-Tranche Audit Mini-Package

Audits that select the next tranche, next roadmap, or next work order must carry
enough structure for a later orchestrator or worker to trust the decision.

Minimum sections:

- `## Owner / Source`
- `## Protocol / Contract / Requirements`
- `## Enforcement / Verification`
- `## Machine Closure Package`
- `## Related Artifacts`

If the audit mentions corpus, search, classification, readiness, registry, or
runtime/source absence, the Machine Closure Package must use `PASS` or
`BLOCKED with reason` for the affected registry/source rows. Do not use `N/A
with reason` when an owner surface exists and the audit intentionally deferred
or excluded it.

---

## Near-Threshold Template Owner Discipline

Do not move new template obligations into an adjacent addendum merely to avoid
touching a near-threshold canonical template or front-door file.

When a canonical template, handoff, front door, or owner entrypoint is within
the GC-023 near-hard margin and a new adjacent rule belongs to that owner
family, the same batch must:

- include the owner entrypoint in Allowed scope;
- split, rotate, archive, or materially shrink the owner;
- update `proactiveOwnerSurfaces` when future adjacent changes should be
  machine-guarded;
- run `python governance/compat/check_governed_file_size.py --enforce`.

Using an addendum is valid only as part of owner extraction, not as an avoidance
pattern.

---

## Required Proof Manifest Atomic Literal Discipline

Required Proof Manifest rows must be review-fast, machine-readable, and
unambiguous.

Rules:

- Put exactly one required literal in each `Required literal` cell.
- Do not write compound cells such as `` `A` and `B` `` or `` `A`, `B` ``.
- If one proof file must contain several sentinels, write one row per sentinel.
- If a proof is intentionally not literal-based, use `N/A with reason` instead
  of a fake placeholder literal.
- When prior verification evidence already proves a binary/hash invariant,
  prefer the existing verification receipt and cite that receipt instead of
  forcing redundant recomputation.

Machine enforcement:

- `governance/compat/check_work_order_dispatch_quality.py` rejects
  dispatch/ready work orders with compound Required Proof Manifest literal
  cells.
- This is a pre-dispatch authoring control. It prevents reviewers and workers
  from discovering malformed proof requirements only after a long hook chain.

---

## Dispatch Packet Authoring Learning Promotion

If Codex or another reviewer fixes a dispatch packet before committing it, the
reviewer must classify whether the finding is a reusable CVF control-plane
pattern.

Reusable dispatch findings include:

- missing authority shell sections such as `## Purpose`;
- placeholder `dispatchBaseHead` instead of a real git commit hash;
- Source Verification rows that mix symbols with value assignments or type
  annotations;
- missing `Current Runtime Freshness Verification` for runtime absence or
  non-use claims;
- missing `Work-Order Fulfillment Manifest` for delegated implementation
  artifacts;
- parent roadmap status residue that conflicts with a newly dispatched child
  lane.
- missing `Export Surface Decision` for reusable helper/foundation surfaces;
- missing `Next-Tranche Audit Mini-Package` for audits that select later work;
- moving template obligations into adjacent addenda while leaving a
  near-threshold canonical template untouched.

If reusable, the same batch must update the template, addendum, standard, or a
machine check. If not reusable, record `N/A with reason` in the reviewer
artifact. This is the authoring-side application of CVF's learning rule: fix
once, reuse many times.

---

## Claim Boundary

This addendum hardens authoring and closure discipline only. It does not prove
runtime behavior, provider behavior, parser behavior, extraction quality,
retrieval quality, production fitness, public claim expansion, or autonomous
mutation.
