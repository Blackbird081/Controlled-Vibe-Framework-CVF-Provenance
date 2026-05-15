# CVF Legacy 16.5 External Knowledge Absorption Map - 2026-05-16

Memory class: POINTER_RECORD

Document type: CANONICAL-CANDIDATE - CVF-NATIVE ABSORPTION MAP

Source bundle: `.private_reference/legacy/CVF 16.5`

Review packet:
`docs/reviews/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_2026-05-16.md`

## Purpose

This document records how the CVF 16.5 legacy knowledge bundle should be
absorbed without creating parallel runtimes.

It reuses the already-written source summaries and detail drafts, then normalizes
them into the existing CVF rule:

`external knowledge can inform CVF; it cannot become CVF authority`

## Owner Surface Map

| Knowledge pattern | Primary owner | Accepted use | Blocked use |
|---|---|---|---|
| Markdown vault intake | Knowledge Layer / Context Builder | Register candidate knowledge with metadata, sensitivity, provenance, and intake receipt | Raw vault consumption by agents |
| Knowledge graph/frontmatter | Knowledge Layer | Navigation and context packaging hints | Policy authority or hidden routing |
| Provenance receipt | Evidence / Audit | Record source path, version, classification, and output usage | Invent proof or imply live enforcement |
| Drift signal | Learning Plane | Flag stale, conflicting, duplicated, or low-confidence knowledge | Auto-rewrite canon |
| Governed reinjection | Control Plane / Context Builder | Reintroduce approved summaries or pointers into context | Dump raw memory/vault content into prompts |
| OpenSpec change packet | Control Plane | Map proposal/design/tasks into CVF phase review | Direct apply/sync/archive without CVF review |
| Delta grammar | Docs governance / Review | Mark ADDED/MODIFIED/REMOVED/RENAMED plus risk/policy/evidence impact | Treat spec delta as approval |

## Required Intake Shape

Future runtime work should preserve this record shape when external knowledge is
registered:

```yaml
external_knowledge_intake:
  intake_id: string
  source_path: string
  source_class: private_reference|external_reference|generated_draft|canon|example
  candidate_title: string
  candidate_type: doctrine|policy|adapter_pattern|runtime_pattern|example|rejected
  sensitivity: public|internal|confidential|restricted
  owner_surface: string
  provenance_summary: string
  freshness: current|stale|unknown
  accepted_value: []
  blocked_value: []
  evidence_requirement: none|doc_review|unit|e2e|live_governance
  evaluation_status: accepted|deferred|rejected|retired
```

The shape is a docs-level contract until a future roadmap implements it.

## Knowledge Intake Rules

Rule 1: source files are source inputs, not source authority.

Rule 2: agents may not consume raw external vault, memory, or generated legacy
files as final context without CVF packaging.

Rule 3: metadata must be explicit enough to show source class, sensitivity,
freshness, and owner surface.

Rule 4: knowledge reinjection must preserve provenance and token budget.

Rule 5: stale or conflicting material creates a review signal, not an automatic
canonical rewrite.

## OpenSpec Mapping

OpenSpec-like material can be useful as a change-packet adapter:

| OpenSpec material | CVF interpretation |
|---|---|
| `proposal.md` | INTAKE/DESIGN review input |
| `design.md` | DESIGN/BUILD boundary input |
| `tasks.md` | BUILD task packet candidate |
| `apply` | Execution only after CVF approval |
| `verify` | REVIEW evidence input |
| `archive/sync` | Archive candidate only; FREEZE decides canonical update |

CVF additions required for every delta:

- risk impact;
- policy impact;
- approval impact;
- DLP impact;
- rollback note;
- evidence required.

## Absorption Boundary

This map does not authorize:

- a new note app;
- a new memory server;
- a new graph authority;
- automatic knowledge rewrite;
- OpenSpec direct apply;
- public publication of private reference material.

It authorizes only docs-level intake semantics and future roadmap candidates.

