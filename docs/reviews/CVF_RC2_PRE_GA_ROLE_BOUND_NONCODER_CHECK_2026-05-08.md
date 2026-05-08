<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Role-Bound Non-Coder Check

**Date:** 2026-05-08
**Status:** PASS

| Scenario | Status | Role | Auth mode | Detail |
|---|---|---|---|---|
| R2a_positive_observer_receipt | PASS | viewer | authenticated | Lowest-authorized viewer role received governanceEvidenceReceipt through live execution. |
| R2b_negative_blocked_operation | PASS | anonymous_local | anonymous_local | Anonymous provider_check returned HTTP 403; expected 403 policy block. |

## Boundary

- This repairs the RC2 Claim N admin-role weakness with a lowest-authorized viewer execution receipt and a blocked anonymous operation.
- This is not full managed multi-tenant RBAC proof.