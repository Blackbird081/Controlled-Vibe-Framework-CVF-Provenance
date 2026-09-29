# CVF RSE-T4 Tool Classifier Block Recovery Addendum

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

## Scope / Applies To

Applies to dispatch packets and worker returns that encounter or must classify
a tool/platform edit block. Dispatcher owns applicability; worker records only
observed events and bounded recovery evidence. No classifier bypass is authorized.

## Purpose

Keep tool/classifier edit recovery inside the technical agent lane while
recording platform-forced operator UI honestly.

## Dispatch Contract

`toolClassifierBlockRecoveryApplicability` is exactly `APPLICABLE` or
`NOT_APPLICABLE_WITH_REASON - <reason>`. For `APPLICABLE`, require:

- `workerAuthoredOperatorQuestionAllowed: NO`
- `platformForcedPromptBoundary: RECORD_NOT_SUPPRESS`
- `atomicEditPreparationRequired: YES`
- `workerControlledEditRetryCeiling: 1`
- `retryScope: SAME_SEMANTIC_EDIT_NO_SCOPE_CHANGE`
- `exhaustedRecoveryRoute: BLOCKED_WITH_REASON_TO_LOCAL`
- `classifierEventCaptureRequired: YES`

## Return Event Contract

Event, forced-prompt, worker-question and retry counts are nonnegative
integers. Forced-prompt and worker-question counts cannot exceed event count.
`NO_EVENT` requires all counts zero and reasoned non-event evidence. A nonzero
event count requires a non-`NO_EVENT` disposition and bounded secret-safe
evidence. Repository controls record, but do not suppress, platform UI.

## Claim Boundary

Local packet/checker semantics only; no classifier bypass, UI interception or
external runtime guarantee.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
