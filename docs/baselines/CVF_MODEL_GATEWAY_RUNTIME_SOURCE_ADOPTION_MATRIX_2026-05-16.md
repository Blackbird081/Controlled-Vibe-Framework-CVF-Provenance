<!-- Memory class: SUMMARY_RECORD -->

# CVF Model Gateway Runtime Source Adoption Matrix - 2026-05-16

Status: roadmap-ready planning artifact; implementation pending approval.

Source bundle:
`.private_reference/legacy/CVF 16.5/freellmapi/`

Target owner:
`EXTENSIONS/CVF_MODEL_GATEWAY/`

## Adoption Rule

The legacy files are adoption candidates, not code to copy unchanged. Each file
must be adapted into CVF naming, Guard Contract integration, receipts, and test
coverage.

## Matrix

| Legacy file | Accepted value | Target module | Required adaptation | Minimum tests |
|---|---|---|---|---|
| `provider.registry.ts` | Provider/model metadata registry with allow checks | `src/provider-registry.ts` | Add CVF risk class mapping, duplicate protection, disabled/experimental denial semantics | register/list/get/duplicate/disabled/model-missing |
| `provider.health.ts` | Provider/model health state tracking | `src/provider-health.ts` | Make health decision deterministic and receipt-friendly | healthy/rate-limited/invalid/error/unknown usability |
| `quota.ledger.ts` | Quota/token/call accounting | `src/quota-ledger.ts` | Separate estimated vs actual token accounting; expose deny reason | allowed budget, exceeded budget, actual usage recording |
| `routing.policy.ts` | Candidate filtering by registry, health, quota, allowed providers | `src/routing-policy.ts` | Require Guard Contract decision input before route selection | selects eligible route, denies no candidates, respects allowed provider |
| `fallback.policy.ts` | Bounded fallback decision | `src/fallback-policy.ts` | Require retry/fallback reason and prevent unbounded retry churn | retryable vs nonretryable, max fallback, reason preservation |
| `sticky.session.ts` | Stable provider/model selection inside a session window | `src/sticky-session.ts` | Preserve policy override and expiry behavior | reuse inside window, expire after window, policy override |
| `credential.vault.ts` | Credential boundary abstraction | `src/credential-boundary.ts` | Never expose raw key in receipt/log; support env resolver without printing | missing key, resolved metadata only, no raw key returned |
| `gateway.receipt.ts` | Gateway routing/audit receipt | `src/gateway-receipt.ts` | Preserve source fields plus CVF policy/risk/validation fields | receipt id, quota/health fields, model substitution fields |

## Guard Contract Integration Points

Every route decision must receive or create a policy decision boundary before
provider selection:

```yaml
gateway_policy_context:
  trace_id: string
  operator_id: string
  workspace_id: string
  request_risk_class: low|medium|high|critical
  data_classification: public|internal|confidential|restricted|secret_risk
  allowed_provider_ids: []
  blocked_provider_ids: []
  policy_result: allow|deny|requires_approval
```

The routing policy must fail closed when policy result is not `allow`.

## File Size Rule

No adopted source or test file may exceed GC-023 thresholds by default. Split by
responsibility before considering any exception:

- types/constants;
- stateful class;
- pure decision helper;
- tests per primitive.

