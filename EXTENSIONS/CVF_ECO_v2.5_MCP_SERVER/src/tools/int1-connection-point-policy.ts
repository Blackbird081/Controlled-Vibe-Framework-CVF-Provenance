export const INT1_CONTRACT = 'cvf.genericMcpAdapter.int1.v1' as const;

export const INT1_ALLOWED_EVENT_TYPES = new Set([
  'intent.received',
  'plan.created',
  'tool.requested',
  'execution.state',
  'result.produced',
]);

const INT1_FORBIDDEN_PLAN_PATTERNS = [
  'delete_all',
  'drop_database',
  'rm -rf',
  'format_disk',
];

export interface Int1PlanInput {
  planSteps: string[];
  toolsRequired: string[];
  agentRole: string;
  planContext?: string;
}

export interface Int1AgentEventInput {
  eventType: string;
  agentId: string;
  payload: Record<string, unknown>;
}

export function validateInt1Plan(args: Int1PlanInput) {
  const forbiddenStepsDetected = args.planSteps.filter(step =>
    INT1_FORBIDDEN_PLAN_PATTERNS.some(pattern =>
      step.toLowerCase().includes(pattern)
    )
  );
  const riskScore = Math.min(
    args.planSteps.length * 0.1 + args.toolsRequired.length * 0.2,
    3.0
  );
  const advisoryDecision = forbiddenStepsDetected.length > 0
    ? 'REJECT_ADVISORY'
    : riskScore > 2.0
      ? 'REVIEW_RECOMMENDED'
      : 'ALLOW_ADVISORY';

  return {
    contractVersion: INT1_CONTRACT,
    tool: 'cvf_validate_plan',
    advisoryDecision,
    planRisk: riskScore.toFixed(2),
    forbiddenStepsDetected,
    stepCount: args.planSteps.length,
    toolCount: args.toolsRequired.length,
    runtimeExecutionAuthorized: false,
    evaluatedAt: new Date().toISOString(),
  };
}

export function emitInt1AgentEvent(args: Int1AgentEventInput) {
  if (!INT1_ALLOWED_EVENT_TYPES.has(args.eventType)) {
    return {
      contractVersion: INT1_CONTRACT,
      tool: 'cvf_emit_agent_event',
      accepted: false,
      eventType: args.eventType,
      rejectionReason: `unsupported_event_type: "${args.eventType}" not in [${[...INT1_ALLOWED_EVENT_TYPES].join(', ')}]`,
      emittedAt: new Date().toISOString(),
    };
  }

  return {
    contractVersion: INT1_CONTRACT,
    tool: 'cvf_emit_agent_event',
    accepted: true,
    eventType: args.eventType,
    eventId: `int1-evt-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    agentId: args.agentId,
    runtimeExecutionAuthorized: false,
    emittedAt: new Date().toISOString(),
  };
}
