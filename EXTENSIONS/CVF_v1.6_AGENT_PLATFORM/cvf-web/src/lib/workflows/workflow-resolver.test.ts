import { describe, expect, it } from 'vitest';

import {
  buildWorkflowExecutionProjection,
  resolveWorkflowBindingForExecution,
} from './workflow-resolver';

describe('workflow-resolver', () => {
  it('resolves the Phase E Product Brief workflow binding', () => {
    const binding = resolveWorkflowBindingForExecution('app_builder_complete');

    expect(binding?.workflowId).toBe('workflow.product.create_product_brief.v1');
    expect(binding?.steps).toHaveLength(5);
  });

  it('replays workflow state and does not complete steps past the deferred reviewer gate', () => {
    const binding = resolveWorkflowBindingForExecution('app_builder_complete');
    expect(binding).toBeDefined();

    const projection = buildWorkflowExecutionProjection(binding!, 'receipt-123');

    expect(projection.stepTraces.map((trace) => trace.stepId)).toEqual([
      'step-1-intake-validation',
      'step-2-knowledge-retrieval',
      'step-3-provider-call',
      'step-4-review-gate',
      'step-5-receipt-emit',
    ]);
    expect(projection.stateMachine).toMatchObject({
      contractVersion: 'cvf.workflowStateMachineProjection.v1',
      workflowId: 'workflow.product.create_product_brief.v1',
      initialState: 'intake_pending',
      finalState: 'review_pending',
      completedStepIds: [
        'step-1-intake-validation',
        'step-2-knowledge-retrieval',
        'step-3-provider-call',
      ],
      deferredStepIds: [
        'step-4-review-gate',
        'step-5-receipt-emit',
      ],
      waitingStepIds: ['step-5-receipt-emit'],
    });
    expect(projection.stepTraces).toContainEqual(expect.objectContaining({
      stepId: 'step-4-review-gate',
      decision: 'deferred',
      receiptId: null,
    }));
    expect(projection.stepTraces).toContainEqual(expect.objectContaining({
      stepId: 'step-5-receipt-emit',
      decision: 'deferred',
      receiptId: null,
    }));
    expect(projection.receipts).toEqual(projection.receiptBinding.emissions.map((emission) => ({
      stepId: emission.stepId,
      receiptId: 'receipt-123',
      source: 'governance_evidence_receipt',
      obligationId: emission.obligationId,
    })));
    expect(projection.receipts.map((receipt) => receipt.stepId)).toEqual([
      'step-1-intake-validation',
      'step-2-knowledge-retrieval',
      'step-3-provider-call',
    ]);
    expect(projection.receiptObligations).toHaveLength(4);
    expect(projection.receiptBinding.fullMatrixDisposition).toBe('deferred_with_reason');
    expect(projection.deferredStepIds).toEqual([
      'step-4-review-gate',
      'step-5-receipt-emit',
    ]);
    expect(projection.recovery).toMatchObject({
      contractVersion: 'cvf.workflowRecoveryReadout.wr1.v1',
      workflowId: 'workflow.product.create_product_brief.v1',
      currentState: 'review_pending',
      lastRestorableCheckpoint: {
        checkpointType: 'POST_EXECUTION',
        stepId: 'step-3-provider-call',
        state: 'review_pending',
        receiptId: 'receipt-123',
        traceSource: 'state_machine_projection',
      },
      blockedStepIds: [
        'step-4-review-gate',
        'step-5-receipt-emit',
      ],
      validationGate: 'blocked',
      recoveryAction: 'hold_for_reviewer_gate',
      requestedTransition: {
        requestedTrigger: null,
        requestedFromState: null,
        requestedToState: null,
        disposition: 'no_requested_transition',
        matchedStepId: null,
      },
    });
  });

  it('classifies direct freeze requests from review pending as invalid', () => {
    const binding = resolveWorkflowBindingForExecution('app_builder_complete');
    expect(binding).toBeDefined();

    const projection = buildWorkflowExecutionProjection(binding!, 'receipt-123', {
      trigger: 'freeze_requested',
      fromState: 'review_pending',
      toState: 'completed',
    });

    expect(projection.recovery.requestedTransition).toMatchObject({
      requestedTrigger: 'freeze_requested',
      requestedFromState: 'review_pending',
      requestedToState: 'completed',
      disposition: 'invalid_from_current_state',
      matchedStepId: 'step-5-receipt-emit',
    });
    expect(projection.recovery.recoveryAction).toBe('escalate_to_governance');
    expect(projection.recovery.recommendedNextAction).toContain('Block forward progress');
  });

  it('holds configured reviewer gate transitions instead of auto-advancing', () => {
    const binding = resolveWorkflowBindingForExecution('app_builder_complete');
    expect(binding).toBeDefined();

    const projection = buildWorkflowExecutionProjection(binding!, 'receipt-123', {
      trigger: 'approval_granted',
      fromState: 'review_pending',
      toState: 'freeze_ready',
    });

    expect(projection.recovery.requestedTransition).toMatchObject({
      requestedTrigger: 'approval_granted',
      requestedFromState: 'review_pending',
      requestedToState: 'freeze_ready',
      disposition: 'configured_deferred_gate',
      matchedStepId: 'step-4-review-gate',
    });
    expect(projection.recovery.recoveryAction).toBe('hold_for_reviewer_gate');
    expect(projection.recovery.boundaries).toContain('no_broad_workflow_engine');
  });

  it('leaves unbound templates untouched', () => {
    expect(resolveWorkflowBindingForExecution('documentation')).toBeUndefined();
    expect(resolveWorkflowBindingForExecution(undefined)).toBeUndefined();
  });
});
