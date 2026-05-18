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

  it('builds active step traces and receipt pointers without firing the deferred reviewer step', () => {
    const binding = resolveWorkflowBindingForExecution('app_builder_complete');
    expect(binding).toBeDefined();

    const projection = buildWorkflowExecutionProjection(binding!, 'receipt-123');

    expect(projection.stepTraces.map((trace) => trace.stepId)).toEqual([
      'step-1-intake-validation',
      'step-2-knowledge-retrieval',
      'step-3-provider-call',
      'step-5-receipt-emit',
    ]);
    expect(projection.stepTraces).not.toContainEqual(
      expect.objectContaining({ stepId: 'step-4-review-gate' }),
    );
    expect(projection.receipts).toEqual(projection.receiptBinding.emissions.map((emission) => ({
      stepId: emission.stepId,
      receiptId: 'receipt-123',
      source: 'governance_evidence_receipt',
      obligationId: emission.obligationId,
    })));
    expect(projection.receiptObligations).toHaveLength(4);
    expect(projection.receiptBinding.fullMatrixDisposition).toBe('deferred_with_reason');
    expect(projection.deferredStepIds).toEqual(['step-4-review-gate']);
  });

  it('leaves unbound templates untouched', () => {
    expect(resolveWorkflowBindingForExecution('documentation')).toBeUndefined();
    expect(resolveWorkflowBindingForExecution(undefined)).toBeUndefined();
  });
});
