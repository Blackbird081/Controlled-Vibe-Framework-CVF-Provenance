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
  });

  it('leaves unbound templates untouched', () => {
    expect(resolveWorkflowBindingForExecution('documentation')).toBeUndefined();
    expect(resolveWorkflowBindingForExecution(undefined)).toBeUndefined();
  });
});
