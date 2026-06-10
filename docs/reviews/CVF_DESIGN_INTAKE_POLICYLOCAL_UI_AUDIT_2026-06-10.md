# Design Reference Intake Note — PolicyLocal UI Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: design_intake_note

Date: 2026-06-10

Gate applied: `DESIGN.md` §13 Design Reference Intake Gate

Classification: Production app (PolicyLocal) — useful for workflow hierarchy,
implementation pitfalls, and reusable theming judgment.

## Purpose

Record, per `DESIGN.md` §13 Absorption Output, the absorption of reusable design
lessons from the 2026-06-10 PolicyLocal UI audit into the CVF design contract:
what was absorbed, what was rejected, which CVF surface changed, and why no
duplicate skill was created.

## Scope / Target / Owner Boundary

Target scope:

- the PolicyLocal web UI audit + fixes (landing tonal banding, theme-aware
  landing, accent-system activation, layered elevation);
- the reusable design judgments extractable from it;
- the CVF surfaces those judgments may update (`DESIGN.md`, canonical UX skill).

Owner boundary: this note is an absorption record only. It does not change
PolicyLocal runtime, does not author a new skill, and does not authorize public
claims. Project-specific token values remain in the project, not the contract.

## Target / Source

- **Name:** PolicyLocal (Vietnamese legal document search/Q&A app).
- **Path:** `CVF-Workspace/Policy_Local/apps/web` (sibling workspace, not CVF root).
- **Trigger:** EA-level UI/UX audit + fixes performed 2026-06-10 (landing tonal
  banding, theme-aware landing, accent system activation, layered elevation).

## Scope / Methodology

EA-level review of the PolicyLocal web UI (dark/light themes, landing, settings,
shared component layer), followed by fixes and Playwright screenshot
verification across dark, light, and a non-default accent. Each reusable defect
was classified against `DESIGN.md` §13 intake gate and the §10 promotion rule to
decide whether it belongs in the contract, a skill, a QA check, or the project.

## Findings / Position

### 2. What was absorbed (→ promoted to `DESIGN.md` §14)

Reusable design judgments, generalized away from PolicyLocal specifics:

- **§14.1 Token-first discipline** — raw hex/`rgba()` in a component is a defect;
  every color must exist in both `:root` and `[data-theme="light"]`. Names the
  two real failure modes observed (light mode silently dark; accent dead).
- **§14.2 No pure black + tonal banding** — deep blue-charcoal base, alternating
  base/raised bands with soft hairline boundaries for long/landing surfaces.
- **§14.3 Layered elevation scale** — xs/sm/md/lg/xl as ambient+key+ring,
  re-tuned for light mode; accent-tinted glow for primary/focus.
- **§14.4 Accent as app-wide token set** — `[data-accent]` mechanism; "wire all
  three (CSS block + type + picker) or remove the declaration."
- **§14.5 Implementation pitfalls** — React border shorthand/longhand conflict;
  orphan-route guard; IDE inline-style warnings are not the gate.
- **§14.6 Pre-ship verification** — verify dark + light + a non-default accent.

A short pointer was added to the canonical skill
`product_ux/cvf_web_ux_redesign_system.skill.md` directing theming/accent/
verification rules to `DESIGN.md` §14 (contract stays source of truth).

## 3. What was rejected

- **A project-local skill `policylocal-design`** was initially (incorrectly)
  created under `Policy_Local/.claude/skills/`. It was **deleted**. It violated
  `DESIGN.md` §10/§11: it was a dark/light-audit + palette + style-selection
  skill that duplicates the canonical portfolio, was scoped to one project, and
  was only visible to one agent.
- PolicyLocal-specific token values (`--lp-*`, exact landing hex) were **not**
  promoted — they are project implementation detail, not cross-product contract.

## 4. CVF surface changed

- `DESIGN.md` — added §14 (the reusable rules above). Primary change.
- `product_ux/cvf_web_ux_redesign_system.skill.md` — one-line pointer to §14.
- No QA-checklist or new-skill change.

## 5. Why no duplicate skill was created

§11 mandates a small portfolio: one canonical system skill, one prototype-ingest
skill, one QA checklist. Theming, elevation, accent discipline, and dark/light
audit are **rules that belong in the design contract**, not a standalone skill
(§10 "A new UI/UX skill is allowed only when the capability is recurring,
non-overlapping, and cannot be expressed as a rule in the canonical system skill
or QA checklist"). They are fully expressible as `DESIGN.md` rules, so they were
promoted there. This corrects the earlier mistaken skill creation.

## Quality Score (§13, all five required)

| Check | Verdict |
| --- | --- |
| Product fit | PASS — fixes real workflow/usability defects, not only taste |
| Reusability | PASS — applies to every CVF web surface, multiple page types |
| Governability | PASS — written as enforceable rules, no source assets copied |
| Accessibility | PASS — strengthens contrast + dark/light + focus verification |
| Skill hygiene | PASS — enriches the contract; the duplicate skill was removed |

## Finding-To-Governance Learning Disposition

Per `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD_2026-05-29.md`.
Each material finding from the audit is routed below; all handled in this batch.

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch |
| --- | --- | --- | --- | --- | --- |
| Hard-coded hex breaks light mode + kills accent switching | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Added `DESIGN.md` §14.1 token-first rule | Handled |
| Pure-black flat surfaces; no tonal-banding guidance | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Added `DESIGN.md` §14.2 | Handled |
| §6 lacks a concrete elevation scale | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Added `DESIGN.md` §14.3 | Handled |
| Multi-accent declared in code but no CSS/UI (dead feature) | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Added `DESIGN.md` §14.4 "wire all three or remove" | Handled |
| React border shorthand/longhand conflict; orphan routes | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Added `DESIGN.md` §14.5 implementation pitfalls | Handled |
| No pre-ship verify across dark+light+non-default accent | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Added `DESIGN.md` §14.6 | Handled |
| Internal-upgrade lessons had no promotion path (only external refs) | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Extended `DESIGN.md` §10 to cover internal lessons + link this standard | Handled |
| Agent created a duplicate dark/light-audit skill | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Deleted skill; §10/§11 + `SKILL_PORTFOLIO_CANONICALIZATION_POLICY` already prohibit it | Handled |

No machine-check added: a `[data-accent]`-completeness or no-raw-hex linter is a
plausible future guard (`MACHINE_CHECK_CANDIDATE`) but lives per-project in the
web app's lint config, not the CVF control plane; not promoted here to avoid
scope creep. Recorded for a future project-level lint rule.

Runtime / provider / cost learning lanes: `N/A_WITH_REASON`. Every finding in
this audit is a presentation-layer design-rule promotion (`GOVERNANCE_CONTROL_PLANE`).
None originate from runtime behavior, provider output, token, latency, or cost
evidence; the words "runtime" above describe a dead UI feature, not a
runtime-learning signal. No `RUNTIME_BEHAVIOR_LEARNING`, `PROVIDER_OUTPUT_LEARNING`,
or `COST_ECONOMICS_LEARNING` candidate is raised.

## Risk / Corrective Action

- **Risk that recurred:** an agent promoting a lesson into a new standalone skill
  instead of the contract, duplicating the canonical UI/UX portfolio.
- **Corrective action taken:** the mistaken `policylocal-design` skill was
  deleted; lessons were promoted into `DESIGN.md` §14 and §10 was extended to
  route future internal lessons through the existing promotion rule +
  `SKILL_PORTFOLIO_CANONICALIZATION_POLICY` §7, not a parallel standard.
- **Residual risk:** none for this batch. A future project-level lint
  (`no-raw-hex`, `[data-accent]` completeness) is recorded as a candidate only,
  not opened, to avoid scope creep into the CVF control plane.

## Claim Boundary

This is an absorption + promotion record, not a runtime or product claim. Verified:
`check_finding_to_governance_learning.py` (worktree/index validation at time of authoring) → COMPLIANT;
`DESIGN.md` and the canonical skill updated and under GC-023 thresholds. It does
not claim PolicyLocal runtime behavior changed, nor that any new machine guard
was added. PolicyLocal code fixes are tracked in that project's own repository.
## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A -- design intake note; no separate work order | N/A | N/A with reason: design intake note; no governed work order required |
| Completion or reviewer artifact | this file | (path of this file) | PASS |
| Roadmap state | N/A | N/A | N/A with reason: no roadmap associated with design intake |
| Registry JSON | docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json | No registry JSON update required for design intake | BLOCKED: design intake -- no corpus scan performed; Registry JSON not applicable |
| Registry Markdown | docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md | No registry markdown update required for design intake | BLOCKED: design intake -- no corpus scan performed; Registry Markdown not applicable |
| External evidence digest | N/A -- all evidence is repo-local | N/A | N/A with reason: no external evidence in this artifact |
| System loop interlock | N/A | N/A | N/A with reason: no system loop trigger |
| Session continuity | AGENT_HANDOFF_V17_2026-06-07.md | active handoff updated | PASS |
