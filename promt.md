## Mission

Execute the three-lane roadmap — Lane B (Workflow Packaging), Lane C
(Execution Gateway), Lane H (Memory Runtime Wiring) — as specified in:

  docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_B_C_H_2026-05-19.md

Authority: docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md
Session mode: operator_lane_selection_active (CVF_SESSION/ACTIVE_SESSION_STATE.json)
Codex role: IMPLEMENTER. Claude role: REVIEWER (per GC-046).

---

## Mandatory Execution Rules (apply to ALL lanes)

1. GC-018 FIRST: File a GC-018 baseline document BEFORE any implementation
   code for each lane. Path pattern:
     docs/baselines/CVF_GC018_LANE_<B|C|H>_<SHORT_NAME>_2026-05-19.md
   Required sections per template:
     docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md
   Include the mandatory Tranche Closure Checklist section.

2. Inventory questions first: Lane C has 6 inventory questions, Lane H has
   7. Answer every question with a file:line citation in the GC-018 BEFORE
   writing any implementation code. Do not skip this step.

3. Atomic commit per step: GC-018, implementation, tests, and completion
   packet are separate commits. Do not batch two lanes.

4. GC-020 after every commit: Update Current HEAD in
   AGENT_HANDOFF_V9_2026-05-18.md, then commit the handoff update as a
   separate commit immediately after.

5. Hook chain clean: Every commit must pass
   governance/compat/run_local_governance_hook_chain.py without --no-verify.

6. GC-023 pre-flight: Before adding code to any existing file, check its
   current line count and the exception registry. If adding would exceed
   the limit, create a dedicated file instead.
   Exception registry: governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json

7. Anti-duplication: Before writing any new file, grep for existing
   equivalents in EXTENSIONS/. Building from zero when a foundation exists
   is a blocking error.

8. Public catalog update is MANDATORY after each lane closes. Run Test-Path
   on all new catalog paths from the public-sync clone before committing.
   Catalog is in Controlled-Vibe-Framework-CVF-public-sync — edit there only.
   Record git remote -v output in the lane completion packet.

---

## Execution Order

Lane B → Lane C → Lane H

Each lane must be fully closed (GC-018 + implementation + tests + completion
packet + catalog update + GC-020) before the next lane begins.
Do NOT parallelize lanes.

---

## Lane B — Workflow Packaging

### Pre-flight check

```powershell
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates.ts"
# must return True
```

Locate the three templates from templates.ts before filing GC-018:

1. Template with id containing "app_builder" or "app_builder_complete"
2. Highest-value business category template (most inputs, most steps)
3. Highest-value content category template

Record all three exact template IDs in the GC-018.

### What to build

For each of the 3 templates, create 3 files in:
  EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/<template-id>/

File 1 — workflow.spec.md (use text code fence, not markdown, to avoid heading conflicts):
  # Workflow Spec — <Template Name>
  Template ID, Role binding, Governed by: CVF v4.0.0 GA
  Sections: Intake / Workflow Steps / Output / Evidence

File 2 — execution.policy.json:
  templateId, requiredRole, minimumPermission, dlpEnabled, quotaEnabled,
  providerLane, receiptRequired, guardPolicyRef

File 3 — receipt.schema.json (JSON Schema draft 2020-12):
  Properties: templateId, role, stepTraces[], providerLane, dlpResult,
  quotaResult, issuedAt. Required: templateId, role, stepTraces, issuedAt.

GC-018 required: YES. Risk: R0.
Live proof required: NO. No runtime code changes.

### Acceptance criteria

- [ ] 3 templates each have workflow.spec.md, execution.policy.json,
      receipt.schema.json
- [ ] No runtime code added or modified (route.ts untouched)
- [ ] All new file paths exist before citing in GC-018
- [ ] Public catalog updated: add or update row for "Workflow capability
      packs" in Key Extensions table
- [ ] GC-020 handoff updated after commit

### Boundary — do NOT do in Lane B

- Modify execute/route.ts or any runtime file
- Claim governed pack is "live proven" — it is schema-defined only
- Add W-series names or internal governance references to pack files
- Add new public capability claims without evidence

---

## Lane C — Execution Gateway

### Pre-flight checks

```powershell
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI"
# must return True — this is the base CLI to extend

rg -n "commander|Commander" "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src"
# understand the CLI framework in use
```

### Mandatory inventory — answer ALL 6 in GC-018 before any code

1. Invocation model: does the CLI call a running web server (HTTP POST to
   localhost:3000/api/execute) or import the execute module directly (Node)?
   Recommended: HTTP POST — reuses all existing middleware unchanged.
   Cite the execute route file and port configuration.

2. Auth/session model: the web route uses NextAuth session. For CLI, choose
   between --api-key flag or local .cvf-token file. Document the choice.
   Do NOT store or print secrets in plaintext.

3. Env/key loading: provider keys (DASHSCOPE_API_KEY etc.) must be loaded
   from .env or process.env — never hardcoded. Cite how the web route
   handles this (route.ts line reference).

4. Input schema: CLI accepts --template <id> --role <role> plus optional
   --input <json>. Verify the exact input shape the execute route expects
   (cite route.ts request schema lines).

5. Receipt output: print governance receipt JSON to stdout. Print step traces
   with --verbose flag or to stderr. Define the exact fields.

6. Error/timeout: graceful error messages, non-zero exit on failure, default
   timeout 30s. Document the exact exit codes.

### What to build

Preferred location: add cvf-execute command to
  EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/

If Codex judges the execute surface warrants separation, create:
  EXTENSIONS/CVF_CLI_EXECUTE/
Justify the choice in the GC-018.

Minimum viable implementation:
- cvf execute --template <id> --role <role> [--input <json>] [--endpoint <url>] [--verbose]
- POSTs to <endpoint>/api/execute with auth header
- Prints receipt JSON to stdout
- Prints step traces to stderr if --verbose
- cvf execute --help shows usage

Tests required:
- Unit: mock HTTP returns mock receipt → CLI outputs valid JSON
- Unit: missing --template → exit 1 + usage message
- Integration (live): describe.skip('live — requires running CVF server')
  Do NOT run in CI without provider key gate

GC-018 required: YES. Risk: R1.
Live proof required: YES for acceptance claim.
  Start CVF web server, run:
    cvf execute --template product_brief --role BUILDER
  Confirm receipt JSON returned with stepTraces[].
  Record output in the Lane C completion packet.

### Acceptance criteria

- [ ] cvf execute --template product_brief --role BUILDER returns receipt JSON
      to stdout when CVF web server is running
- [ ] Receipt includes stepTraces[] array with at minimum intake,
      provider_call, receipt_emission steps
- [ ] Auth model documented; no secret printed to stdout
- [ ] Error on missing required flags with usage message (exit 1)
- [ ] Unit tests pass in CI (no live provider call in CI path)
- [ ] cvf execute --help shows correct usage
- [ ] Extension placement justified in GC-018
- [ ] Public catalog updated: governance CLI row updated to include
      cvf execute command
- [ ] GC-020 handoff updated after commit

### Boundary — do NOT do in Lane C

- Modify execute/route.ts governance logic — CLI calls it, does not change it
- Add new governance middleware to the execute path
- Create a new auth system — use existing NextAuth or a simple token
- Implement cvf trace, cvf run, cvf debug in this tranche — one command only
- Add live provider call to CI without provider key gate
- Claim CLI as "runtime entry point" replacing the web route

---

## Lane H — Memory Runtime Wiring

### Pre-flight checks

```powershell
Test-Path "EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts"
Test-Path "EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts"
# both must return True

rg -n "MemoryTierOwner|MemoryReinjectionPolicy" "EXTENSIONS/CVF_GUARD_CONTRACT/src"
# must return results — confirm contracts exist before building

rg -n "audit|receipt|governance" "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts"
# identify the exact lines where audit event is currently emitted
```

### Mandatory inventory — answer ALL 7 in GC-018 before any code

1. Audit event location: find the exact line(s) in route.ts where the
   governance audit event or audit payload is currently emitted. Paste
   the file:line reference in the GC-018.

2. Storage owner: which MemoryTierOwner tier owns audit events?
   Expected: 'audit' tier from the 5-tier model (Phase 1.M).
   Cite the tier definition file:line.

3. Persistence boundary: where does the current audit event go — JSONL,
   in-memory, response only? Document the current behavior before touching it.

4. Retention policy: what retention policy applies to audit events?
   Cite the existing policy contract or note a default must be defined.

5. Contamination boundary: audit events must NEVER be reinjected into
   subsequent provider calls. Confirm reinjection is not triggered for this
   event type by reading the MemoryReinjectionPolicy contract.

6. Receipt shape: define AuditMemoryReceipt before wiring. Required fields:
   eventType: 'governance_audit', sessionId, templateId, role,
   tier: 'audit', retentionPolicy, reinjectionAllowed: false,
   persistedAt, storageRef (optional).

7. Live proof requirement: does wiring the audit memory path change provider
   output? If NO (audit is post-response) → unit + integration test sufficient.
   If YES → live Alibaba proof required. Determine this from reading route.ts.

### What to build

Step 1 — Define AuditMemoryReceipt type:
  Add to CVF_GUARD_CONTRACT/src/contracts/ or CVF_LEARNING_PLANE_FOUNDATION/src/
  Justify placement in GC-018.

Step 2 — Wire into execute route (post-response only):
  After governance receipt is built and BEFORE response is returned in route.ts:
  - MemoryTierOwner.classify('governance_audit') → 'audit'
  - MemoryReinjectionPolicy.check('audit', context) → { allowed: false }
  - emitAuditMemoryReceipt({ sessionId, templateId, role, tier, retentionPolicy,
      reinjectionAllowed: false, persistedAt })
  Audit receipt must NOT appear in the provider prompt.

Step 3 — Tests (4 required):
  Unit: MemoryTierOwner.classify('governance_audit') returns 'audit'
  Unit: MemoryReinjectionPolicy.check('audit', ctx) returns { allowed: false }
  Unit: emitAuditMemoryReceipt(...) returns valid AuditMemoryReceipt
  Integration: full execute flow emits auditMemoryReceipt — verify field presence

GC-018 required: YES. Risk: R1.
Live proof required: per inventory question 7. If audit is post-response,
unit + integration tests are sufficient. Record the determination in GC-018.

### Acceptance criteria

- [ ] MemoryTierOwner.classify('governance_audit') returns 'audit'
- [ ] MemoryReinjectionPolicy.check('audit', ...) returns { allowed: false }
- [ ] Execute route emits AuditMemoryReceipt after each governed execution
- [ ] AuditMemoryReceipt does NOT appear in provider prompt
- [ ] All 4 unit/integration tests pass
- [ ] route.ts diff is additive only — no existing governance logic removed
- [ ] Public catalog updated: "Memory and continuity contracts" row status
      upgraded from partially absorbed to partially proven with evidence path
- [ ] GC-020 handoff updated after commit

### Boundary — do NOT do in Lane H

- Wire memory reinjection into the provider prompt — audit is post-response only
- Implement multi-flow memory in this tranche — one flow (audit event) only
- Change MemoryTierOwner or MemoryReinjectionPolicy contract signatures
  if existing tests rely on them — additive only
- Claim "full memory governance" — claim is bounded to audit event persistence
- Delete or replace the existing audit log mechanism — extend it

---

## After All Three Lanes Complete

File a full completion report:
  docs/reviews/CVF_LANE_BCH_FULL_CLOSURE_2026-05-19.md

The report must contain:

- Evidence Trace Block with one row per lane (GC-046 format):
  Command / Result / Key path / Verdict
- Acceptance criteria checklist result per lane (all checkboxes ticked)
- Public catalog update record: paths and Test-Path results per lane
- GC-020 final HEAD recorded

Do NOT:
- Add contracts or types beyond what the lane scopes define
- Claim live proven status without a recorded live proof
- Globally lift system_reconvergence_stop (lifted per-lane only)
- Implement Lane D, E, F, or G — none are authorized
- Use --no-verify on any commit
- Edit the public catalog from the private governance repo
  (run git remote -v first; edits go in the public-sync clone only)
