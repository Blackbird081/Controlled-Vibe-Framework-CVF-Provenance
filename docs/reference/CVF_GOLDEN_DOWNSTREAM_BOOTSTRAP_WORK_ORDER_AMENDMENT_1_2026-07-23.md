# CVF Golden Downstream Bootstrap — Work Order Amendment 1

Memory class: EVIDENCE_RECORD

Status: IMPORTED_EXECUTION_COMPLETE_PENDING_PROVENANCE_REVIEW

docType: reference

Text Encoding Exception: preserve Unicode punctuation from the imported
historical public amendment; no machine-readable token depends on it.

## Purpose

Preserve the originating amendment that repaired the bounded worker scope.

## Scope / Applies To

Applies only to the historical golden-downstream bootstrap work order. It is
not a current dispatch surface.

- Work order: `CVF-BSL-T1-WO`
- Amendment: `CVF-BSL-T1-WO-A1`
- Date: 2026-07-23
- Status: AUTHORIZED
- Authority: independent REVIEWER finding BSL-R7

## Finding

The new bootstrap and doctor depend on catalog/helper surfaces that must be
part of the public workspace kit. The public-core reconciler owns the
post-clone completeness list, but its path was not in the original changed-set
ceiling. Without that path, the worker cannot close BSL-R7.

## Amendment

## Claim Boundary

This amendment records historical scope repair only and grants no new
implementation, commit, push, or public-export authority.

Add exactly this path to the changed-set ceiling:

```text
scripts/update_cvf_workspace_public_core.ps1
```

Authorized changes in that file are limited to public-kit completeness for
the new golden downstream catalog surfaces and directly related testable error
detail. No reconciliation algorithm, backup behavior, Git history handling or
manifest-update behavior may change.

No other scope, exclusion, role, evidence, provider or commit authority
changes.
