import {
  bindStepReceipts,
  validateWorkflowBinding,
  type StepReceiptBindingResult,
  type StepReceiptObligation,
  type WorkflowBinding,
  type WorkflowStepDecision,
  type WorkflowStepExecutionTrace,
} from 'cvf-guard-contract';

import createProductBriefWorkflow from './workflow.product.create_product_brief.v1.json';

export interface WorkflowStepReceipt {
  readonly stepId: string;
  readonly receiptId: string;
  readonly source: 'governance_evidence_receipt';
  readonly obligationId: string;
}

export interface WorkflowStateMachineStepDecision {
  readonly stepId: string;
  readonly sequence: number;
  readonly fromState: string;
  readonly trigger: string;
  readonly expectedToState: string;
  readonly enteredState: string;
  readonly decision: WorkflowStepDecision;
  readonly reason:
    | 'transition_completed'
    | 'configured_deferred'
    | 'from_state_unreachable';
  readonly receiptRequired: boolean;
  readonly receiptEmitted: boolean;
}

export interface WorkflowStateMachineProjection {
  readonly contractVersion: 'cvf.workflowStateMachineProjection.v1';
  readonly workflowId: string;
  readonly initialState: string;
  readonly finalState: string;
  readonly completedStepIds: readonly string[];
  readonly deferredStepIds: readonly string[];
  readonly waitingStepIds: readonly string[];
  readonly decisions: readonly WorkflowStateMachineStepDecision[];
}

export interface WorkflowExecutionProjection {
  readonly workflowId: string;
  readonly workflowVersion: string;
  readonly capabilityId: string;
  readonly templateId: string;
  readonly stepTraces: readonly WorkflowStepExecutionTrace[];
  readonly receipts: readonly WorkflowStepReceipt[];
  readonly receiptObligations: readonly StepReceiptObligation[];
  readonly receiptBinding: StepReceiptBindingResult;
  readonly deferredStepIds: readonly string[];
  readonly stateMachine: WorkflowStateMachineProjection;
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
  const orderedSteps = [...binding.steps].sort((a, b) => a.sequence - b.sequence);
  const initialState = orderedSteps[0]?.transition.fromState ?? 'intake_pending';
  let currentState = initialState;
  let blockedByDeferredStep = false;

  const decisions: WorkflowStateMachineStepDecision[] = orderedSteps.map((step) => {
    const canEnter = !blockedByDeferredStep && step.transition.fromState === currentState;
    const isConfiguredDeferred = step.status === 'deferred_until_reviewer_surface';
    let decision: WorkflowStepDecision;
    let reason: WorkflowStateMachineStepDecision['reason'];
    let receiptEmitted = false;

    if (!canEnter) {
      decision = 'deferred';
      reason = 'from_state_unreachable';
      blockedByDeferredStep = true;
    } else if (isConfiguredDeferred) {
      decision = 'deferred';
      reason = 'configured_deferred';
      blockedByDeferredStep = true;
    } else {
      decision = 'completed';
      reason = 'transition_completed';
      receiptEmitted = step.receiptRequired;
      currentState = step.transition.toState;
    }

    return {
      stepId: step.stepId,
      sequence: step.sequence,
      fromState: step.transition.fromState,
      trigger: step.transition.trigger,
      expectedToState: step.transition.toState,
      enteredState: currentState,
      decision,
      reason,
      receiptRequired: step.receiptRequired,
      receiptEmitted,
    };
  });

  const stepTraces: WorkflowStepExecutionTrace[] = decisions.map((decision) => ({
    stepId: decision.stepId,
    preconditionChecked: true,
    decision: decision.decision,
    receiptId: decision.receiptEmitted ? receiptId : null,
    source: 'route_dispatch',
  }));
  const receiptBinding = bindStepReceipts(binding, stepTraces);
  const deferredStepIds = decisions
    .filter((decision) => decision.decision === 'deferred')
    .map((decision) => decision.stepId);
  const completedStepIds = decisions
    .filter((decision) => decision.decision === 'completed')
    .map((decision) => decision.stepId);

  return {
    workflowId: binding.workflowId,
    workflowVersion: binding.version,
    capabilityId: binding.capabilityId,
    templateId: binding.templateId,
    stepTraces,
    receipts: receiptBinding.emissions.map((emission) => ({
      stepId: emission.stepId,
      receiptId: emission.receiptId,
      source: 'governance_evidence_receipt',
      obligationId: emission.obligationId,
    })),
    receiptObligations: receiptBinding.obligations,
    receiptBinding,
    deferredStepIds,
    stateMachine: {
      contractVersion: 'cvf.workflowStateMachineProjection.v1',
      workflowId: binding.workflowId,
      initialState,
      finalState: currentState,
      completedStepIds,
      deferredStepIds,
      waitingStepIds: decisions
        .filter((decision) => decision.reason === 'from_state_unreachable')
        .map((decision) => decision.stepId),
      decisions,
    },
  };
}
