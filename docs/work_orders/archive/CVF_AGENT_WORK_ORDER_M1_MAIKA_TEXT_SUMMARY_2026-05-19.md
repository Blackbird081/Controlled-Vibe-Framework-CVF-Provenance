# CVF Agent Work Order — M1: Maika Text Summary Through CVF Execute

Memory class: SUMMARY_RECORD

Status: CLOSED_WITH_DEPLOYMENT_VERIFICATION_PENDING

GC-018 required: No — Maika product feature; no new CVF enforcement surface.

## Purpose

Add `supabase/functions/generate-daily-summary/index.ts` to the Nha tre Maika
workspace. The function calls CVF `/api/execute` (governed path only; no direct
provider fallback) with a minimized, privacy-bounded payload derived from the
existing rule-based button in `DailyReports.jsx`. Replaces the synchronous
string-concat with an async AI-generated summary while preserving the rule-based
string as a network/auth fallback only.

## Authority Chain

`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` — M1 section.
Codex rebuttal `CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
accepted; M1 corrected scope applied.

## Agent Roles

- **Orchestrator** — dispatches work order; accepts completion packet.
- **Worker** — implements all tasks in Maika workspace only; runs pre-flight
  checks before writing any code; returns evidence to Orchestrator/Codex for
  the completion review.

## Scope

**Allowed scope:** Maika workspace (`CVF-Workspace/Nha tre Maika`) only.

- New file: `supabase/functions/generate-daily-summary/index.ts`
- Modified file: `src/pages/admin/DailyReports.jsx` — button handler,
  loading state, and local helper only
- Modified file: `.env.example` — document Supabase server env placeholders
  `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN`

**Forbidden scope:**

- Direct provider call (no Anthropic/OpenAI SDK import in edge function)
- Photo description or image handling
- Modifying CVF governance repo or public-sync repo
- Adding new env vars beyond `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN`
  (Supabase secrets)
- Changing any Maika auth, DB schema, or push notification code

## Required First Reads

1. `src/pages/admin/DailyReports.jsx` lines 654–696 — current onClick handler
2. `supabase/functions/send-push/index.ts` — Deno edge function pattern
3. `supabase/functions/_shared/cors.ts` — CORS helpers
4. `.env.example` (if exists) — existing env vars
5. Roadmap M1 section — data minimization payload spec

## Write Ownership

Worker owns: `generate-daily-summary/index.ts`, `DailyReports.jsx` onClick
block, `.env.example` additions. No other files.

## Pre-Flight Checks

Worker must verify before writing any code:

```text
1. Confirm supabase/functions/send-push/index.ts exists and read pattern
2. Confirm supabase/functions/generate-daily-summary/ does NOT exist yet
3. Confirm DailyReports.jsx lines 654–683 contain the rule-based string concat
4. Confirm no direct AI provider SDK (anthropic, openai) in any existing function
5. Confirm .env.example does NOT already declare CVF_EXECUTE_URL / CVF_SERVICE_TOKEN
```

## Execution Plan

Task 1 → Task 2 → Task 3 in sequence.

### Task 1 — Edge function `generate-daily-summary/index.ts`

Create `supabase/functions/generate-daily-summary/index.ts`.

Pattern: follow `send-push/index.ts` (Deno.env, corsHeadersFor, jsonResponse,
requireSender for auth).

Payload sent to CVF `/api/execute`:

```json
{
  "templateId": "documentation",
  "templateName": "documentation",
  "intent": "Generate a concise Vietnamese daily report summary for a kindergarten child.",
  "inputs": {
    "subject": "Tóm tắt nhật ký hằng ngày cho phụ huynh",
    "currentNotes": "<string — joined mood, meals, sleep, activities, health; no child name>",
    "readerGoal": "Phụ huynh hiểu ngắn gọn ngày hôm nay của bé, không có dữ liệu định danh."
  },
  "requestedRole": "SERVICE_AGENT"
}
```

Privacy boundary (document in file header comment):

- No child name, parent name, or contact data in payload
- No photo or image data
- Meals joined as summary string, not raw meal names with student identifiers
- `requestedRole: "SERVICE_AGENT"` — not OPERATOR or BUILDER

Auth: read `CVF_SERVICE_TOKEN` from `Deno.env.get('CVF_SERVICE_TOKEN')`.
Build HMAC signature compatible with `computeServiceRequestSignature()` in
`service-token-auth.ts`: SHA-256 HMAC over `${timestamp}.${body}`. Use
Deno/WebCrypto APIs in the Edge Function; do not import Node `crypto`.

Endpoint: read `CVF_EXECUTE_URL` from `Deno.env.get('CVF_EXECUTE_URL')`.

Response: return `{ summary: string }` on success; return
`{ error: string }` on CVF failure.

No direct AI provider call. No fallback to string concat inside the function.

### Task 2 — Wire `DailyReports.jsx` button

In `DailyReports.jsx`, replace the synchronous onClick block at lines 654–683
with an async handler:

1. Call the Supabase Edge Function using the existing Maika fetch pattern:
   `fetch(${VITE_SUPABASE_URL}/functions/v1/generate-daily-summary, ...)`
   with `Authorization: Bearer <session.access_token>` and `apikey:
   VITE_SUPABASE_ANON_KEY`.
2. `payload` = minimized fields only (mood, meals, sleep, activities, health);
   do not send `student`, `studentId`, child name, photo paths, or parent data.
3. On success: `setForm(f => ({ ...f, note: data.summary }))`.
4. On error (network / auth / CVF failure): fall back to existing rule-based
   string concat (copy the current lines 655–681 as fallback).
5. Show a loading state on the button while awaiting (disable + text change).

Do not remove the rule-based string. It is the fallback only.

### Task 3 — Document env vars

In `.env.example` (create if missing), add:

```text
# CVF governed execution endpoint (for Maika AI features)
CVF_EXECUTE_URL=https://your-cvf-deploy.netlify.app
CVF_SERVICE_TOKEN=your-service-token-here
```

## Acceptance Criteria

- [ ] `generate-daily-summary/index.ts` exists; no direct AI provider SDK import
- [ ] Payload contains no child name, photo, or parent contact data
- [ ] `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN` read from `Deno.env`, not hardcoded
- [ ] `DailyReports.jsx` button calls edge function asynchronously using the
  existing fetch + Authorization/apikey pattern
- [ ] Rule-based string concat is fallback on network/auth/CVF error only
- [ ] `.env.example` documents both env vars with placeholder values

## Evidence Requirements

Completion review must include:

1. Edge function file path and line count.
2. `DailyReports.jsx` diff: old onClick (string concat) → new async handler.
3. Confirmation: no direct AI provider SDK import in edge function.
4. Confirmation: no child name or photo data in payload.
5. Confirmation: `CVF_SERVICE_TOKEN` is read from `Deno.env`, not hardcoded.
6. Manual test description, mock fetch test, or supabase CLI local test showing
   summary returned from CVF execute path.

## Review Gate

Orchestrator reviews completion packet. No closure without privacy boundary
evidence (items 3 + 4 above).

## Closure Checklist

- [ ] All acceptance criteria verified with evidence
- [ ] Completion review filed by Orchestrator/Codex in CVF `docs/reviews/`
  after Maika implementation is complete
- [ ] GC-020 handoff HEAD SHA updated by Orchestrator/Codex after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- `send-push/index.ts` pattern cannot be followed (e.g., Deno version mismatch)
- CVF `/api/execute` requires auth method not supportable from Deno edge
- Supabase functions directory structure has changed from expected layout

## Target repo

`CVF-Workspace/Nha tre Maika` only.

## Claim Boundary

M1 covers text-only daily summary via CVF governed path. Does not authorize
photo description, direct provider call, new Maika routes, DB schema changes,
or CVF repo modifications.
