import {
  getActiveWorkflowSteps,
  validateWorkflowBinding,
  type WorkflowBinding,
  type WorkflowStepExecutionTrace,
} from 'cvf-guard-contract';

import createProductBriefWorkflow from './workflow.product.create_product_brief.v1.json';

export interface WorkflowStepReceipt {
  readonly stepId: string;
  readonly receiptId: string;
  readonly source: 'governance_evidence_receipt';
}

export interface WorkflowExecutionProjection {
  readonly workflowId: string;
  readonly workflowVersion: string;
  readonly capabilityId: string;
  readonly templateId: string;
  readonly stepTraces: readonly WorkflowStepExecutionTrace[];
  readonly receipts: readonly WorkflowStepReceipt[];
  readonly deferredStepIds: readonly string[];
}

const WORKFLOW_BINDINGS: readonly WorkflowBinding[] = [
  createProductBriefWorkflow as WorkflowBinding,
];

export function resolveWorkflowBindingForExecution(templateId?: string): WorkflowBinding | undefined {
  if (!templateId) {
    return undefined;
  }

  const binding = WORKFLOW_BINDINGS.find((candidate) => candidate.templateId === templateId);
  if (!binding) {
    return undefined;
  }

  const validation = validateWorkflowBinding(binding);
  if (!validation.valid) {
    throw new Error(`Invalid workflow binding for ${templateId}: ${validation.errors.join('; ')}`);
  }

  return binding;
}

export function buildWorkflowExecutionProjection(
  binding: WorkflowBinding,
  receiptId: string,
): WorkflowExecutionProjection {
  const activeSteps = getActiveWorkflowSteps(binding);
  const stepTraces: WorkflowStepExecutionTrace[] = activeSteps.map((step) => ({
    stepId: step.stepId,
    preconditionChecked: true,
    decision: 'completed',
    receiptId,
    source: 'route_dispatch',
  }));

  return {
    workflowId: binding.workflowId,
    workflowVersion: binding.version,
    capabilityId: binding.capabilityId,
    templateId: binding.templateId,
    stepTraces,
    receipts: stepTraces.map((trace) => ({
      stepId: trace.stepId,
      receiptId,
      source: 'governance_evidence_receipt',
    })),
    deferredStepIds: binding.steps
      .filter((step) => step.status === 'deferred_until_reviewer_surface')
      .map((step) => step.stepId),
  };
}
