import type { ExecutionRequest } from '@/lib/ai';
import { CVF_WEB_REDESIGN_DNA_APPENDIX, shouldAttachCvfWebRedesignDna } from '@/lib/cvf-web-redesign-dna';
import { getTemplateById } from '@/lib/templates';
import { renderTemplateIntent } from '@/lib/template-intent';

const TRUSTED_NONCODER_DEPTH_TEMPLATE_IDS = new Set([
  'documentation',
  'faq_outline',
  'acceptance_criteria',
  'competitor_review',
  'risk_assessment',
  'user_persona',
  'feature_prioritization',
  'pricing_strategy',
  'strategy_analysis',
  'operator_plan',
  'decision_memo',
]);

type DeliverableShape = 'faq' | 'acceptance_criteria' | 'plan' | 'decision_comparison' | 'prioritization' | 'persona';

const SHAPE_SPECIFIC_TEMPLATE_IDS = new Set([
  'faq_outline',
  'acceptance_criteria',
  'operator_plan',
  'decision_memo',
]);

function collectRequestText(request: ExecutionRequest): string {
  const inputText = Object.entries(request.inputs)
    .filter(([key]) => !key.startsWith('_'))
    .map(([, value]) => value)
    .filter(Boolean)
    .join('\n');

  return [
    request.templateId,
    request.templateName,
    request.intent,
    inputText,
  ].join('\n').toLowerCase();
}

function resolveDeliverableShapes(request: ExecutionRequest): DeliverableShape[] {
  const text = collectRequestText(request);
  const shapes: DeliverableShape[] = [];

  if (/\b(faq|frequently asked|question(?:s)? and answer(?:s)?|q&a)\b/i.test(text)) {
    shapes.push('faq');
  }

  if (/\b(acceptance criteria|given when then|testable criteria)\b/i.test(text)) {
    shapes.push('acceptance_criteria');
  }

  if (/\b(\d+[- ]?day|weekly|monthly|roadmap|plan|launch|retention|operations?)\b/i.test(text)) {
    shapes.push('plan');
  }

  if (/\b(compare|comparison|option|options|versus|vs\.?|channel choice|choose|decision|freemium|paid-only)\b/i.test(text)) {
    shapes.push('decision_comparison');
  }

  if (/\b(prioriti[sz]e|prioritization|priority|backlog|mvp scope|triage|rice|ice|moscow|kano)\b/i.test(text)) {
    shapes.push('prioritization');
  }

  if (/\b(persona|personas|buyer|end-user|user journey|segment)\b/i.test(text)) {
    shapes.push('persona');
  }

  return shapes;
}

function buildTaskShapeGuidance(shapes: DeliverableShape[]): string[] {
  const guidance: string[] = [];

  if (shapes.includes('faq')) {
    guidance.push('FAQ shape: produce 8-12 concrete questions with direct answers; group by user concern; include at least one payment/access/troubleshooting item when relevant; end with acceptance checks for whether the FAQ is ready to publish.');
  }

  if (shapes.includes('acceptance_criteria')) {
    guidance.push('Acceptance-criteria shape: group criteria by feature or workflow; make each criterion observable and testable; include data source, refresh/state expectations, error/empty states, and pass/fail checks instead of generic quality advice.');
  }

  if (shapes.includes('plan')) {
    guidance.push('Plan shape: provide a timeline or phased action table with owner/role, action, concrete artifact, success metric, and acceptance check for each phase; include immediate next actions for the first 24-72 hours when relevant.');
  }

  if (shapes.includes('decision_comparison')) {
    guidance.push('Decision/comparison shape: compare every named or reasonably inferred option using the same criteria; include pros, cons, cost/effort, risk, best-fit scenario, and a final recommendation with a simple decision rule.');
  }

  if (shapes.includes('prioritization')) {
    guidance.push('Prioritization shape: score or rank each item; explain the top tradeoffs; identify quick wins and deferrals; give the operator a next-step checklist and acceptance checks for the chosen scope.');
  }

  if (shapes.includes('persona')) {
    guidance.push('Persona shape: give each persona realistic context, goals, pain points, jobs-to-be-done, triggers, objections, and concrete product/marketing next steps with acceptance checks.');
  }

  return guidance;
}

function resolvePrimaryDeliverableShape(shapes: DeliverableShape[]): DeliverableShape | undefined {
  if (shapes.includes('faq')) return 'faq';
  if (shapes.includes('acceptance_criteria') || shapes.includes('prioritization') || shapes.includes('persona')) {
    return undefined;
  }
  if (shapes.includes('decision_comparison')) return 'decision_comparison';
  if (shapes.includes('plan')) return 'plan';
  return undefined;
}

function buildDeliverableContract(shape: DeliverableShape | undefined): string | undefined {
  switch (shape) {
    case 'faq':
      return `# FAQ Outline

## 1. Audience And Scope
- Who this FAQ is for:
- What workflow or product area it covers:

## 2. FAQ Entries
| Question | Direct Answer | When It Applies | Owner/Source To Confirm |
| --- | --- | --- | --- |
| 1. | | | |
| 2. | | | |

## 3. Must-Include Edge Cases
- Payment/access/troubleshooting questions:
- Policy or wording that must stay unchanged:

## 4. Publish Readiness Checks
- [ ] Answers are direct and understandable by the target audience
- [ ] Missing facts are marked as assumptions or confirmation items
- [ ] Support/operator escalation path is clear`;
    case 'acceptance_criteria':
      return `# Acceptance Criteria Packet

## 1. Scope Under Test
- Feature/workflow:
- User or operator outcome:

## 2. Criteria By Workflow
| Workflow Area | Given | When | Then | Data/State Requirement | Pass/Fail Check |
| --- | --- | --- | --- | --- | --- |
| 1. | | | | | |
| 2. | | | | | |

## 3. Empty, Error, And Edge States
- Empty state:
- Error state:
- Permission/access state:
- Refresh or data-latency state:

## 4. Handoff Checks
- [ ] Each criterion is observable
- [ ] Each criterion can be verified by a non-technical operator or tester
- [ ] Open assumptions are listed`;
    case 'prioritization':
      return `# Prioritization Decision

## 1. Goal And Constraints
- Product/operator goal:
- Constraints:
- Framework used:

## 2. Scoring Matrix
| Item | User/Business Value | Effort | Risk | Confidence | Score/Rank | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | | | | | | |
| 2. | | | | | | |

## 3. Recommended Scope
- Do now:
- Do next:
- Defer:

## 4. Next-Step Checklist And Acceptance Checks
- [ ] Owner can explain why each top item was chosen
- [ ] Deferred items have a reason
- [ ] First implementation or validation step is clear`;
    case 'persona':
      return `# Persona Packet

## 1. Segments And Assumptions
- Source data used:
- Assumptions:

## 2. Persona Profiles
| Persona | Context | Goals | Pain Points | Jobs To Be Done | Objections | Trigger |
| --- | --- | --- | --- | --- | --- | --- |
| 1. | | | | | | |
| 2. | | | | | | |

## 3. Journey And Decision Moments
- Discovery:
- Evaluation:
- First successful use:
- Retention or repeat-use trigger:

## 4. Product Or Marketing Actions
- Message or offer:
- Product change or support action:
- Acceptance checks:`;
    case 'decision_comparison':
      return `# Decision Comparison Memo

## 1. Decision To Make
- Decision:
- Constraints:
- Assumptions:

## 2. Option-By-Option Comparison
| Option | Best Fit Scenario | Pros | Cons | Cost/Effort | Risks | Activation Steps |
| --- | --- | --- | --- | --- | --- | --- |
| Option A | | | | | | |
| Option B | | | | | | |

## 3. Recommendation
- Recommended option:
- Why it wins:
- When to choose a different option:

## 4. Decision Rule And Acceptance Checks
- Decision rule:
- [ ] Every named option was compared
- [ ] Operator knows the first activation step
- [ ] Risks and assumptions are explicit`;
    case 'plan':
      return `# Operator Action Plan

## 1. Goal, Constraints, And Assumptions
- Goal:
- Constraints:
- Assumptions:

## 2. Timeline And Owners
| Phase/Date | Owner/Role | Action | Concrete Artifact | Success Metric | Acceptance Check |
| --- | --- | --- | --- | --- | --- |
| 1. | | | | | |
| 2. | | | | | |

## 3. First 24-72 Hours
- Step 1:
- Step 2:
- Step 3:

## 4. Risks, Dependencies, And Checkpoints
- Key risks:
- Dependencies:
- Review checkpoints:

## 5. Final Handoff Checklist
- [ ] Owner is clear for every action
- [ ] Metrics are measurable
- [ ] Acceptance checks are specific enough to verify`;
    default:
      return undefined;
  }
}

export function buildExecutionPrompt(request: ExecutionRequest): string {
  const { templateName, inputs, intent } = request;
  const previousOutput = inputs._previousOutput;
  const template = request.templateId ? getTemplateById(request.templateId) : undefined;
  const isTrustedNoncoderTemplate = Boolean(template?.id && TRUSTED_NONCODER_DEPTH_TEMPLATE_IDS.has(template.id));
  const deliverableShapes = isTrustedNoncoderTemplate ? resolveDeliverableShapes(request) : [];
  const usesShapeSpecificTemplate = Boolean(template?.id && SHAPE_SPECIFIC_TEMPLATE_IDS.has(template.id));
  const primaryDeliverableShape = usesShapeSpecificTemplate ? undefined : resolvePrimaryDeliverableShape(deliverableShapes);
  const primaryDeliverableContract = buildDeliverableContract(primaryDeliverableShape);
  const taskShapeGuidance = buildTaskShapeGuidance(deliverableShapes);

  let prompt = `## Task: ${templateName}\n\n`;
  prompt += `### User Intent\n${intent}\n\n`;
  prompt += `### Input Data\n`;

  for (const [key, value] of Object.entries(inputs)) {
    if (key.startsWith('_')) continue;
    if (value && value.trim()) {
      const label = key
        .replace(/([A-Z])/g, ' $1')
        .replace(/_/g, ' ')
        .replace(/^\s/, '')
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(' ');

      prompt += `\n**${label}:**\n${value}\n`;
    }
  }

  prompt += `\n---\n\n`;

  if (request.cvfPhase || request.cvfRiskLevel) {
    prompt += `### Governance Context\n`;
    if (request.cvfPhase) prompt += `- Phase target: ${request.cvfPhase}\n`;
    if (request.cvfRiskLevel) prompt += `- Risk level: ${request.cvfRiskLevel}\n`;
    prompt += `\n`;
  }

  if (request.skillPreflightDeclaration || request.skillIds?.length) {
    prompt += `### Skill Context\n`;
    if (request.skillPreflightDeclaration) {
      prompt += `- Skill preflight: ${request.skillPreflightDeclaration}\n`;
    }
    if (request.skillIds?.length) {
      prompt += `- Declared skills: ${request.skillIds.join(', ')}\n`;
    }
    prompt += `\n`;
  }

  if (shouldAttachCvfWebRedesignDna({
    templateId: request.templateId,
    templateName: request.templateName,
    skillIds: request.skillIds,
  })) {
    prompt += `### Bound UX Skill Context\n`;
    prompt += `${CVF_WEB_REDESIGN_DNA_APPENDIX}\n\n`;
  }

  if (template?.outputTemplate || template?.outputExpected?.length) {
    prompt += `### Template Output Contract\n`;
    prompt += `Follow this template contract for structure, but treat it as a minimum outline, not a compression target.\n`;
    prompt += `Do not return the raw skeleton or a fenced code block. Fill the headings with the supplied user input values, names, constraints, and concrete decisions.\n`;
    prompt += `Expand each major heading with task-specific depth: assumptions, rationale, concrete next actions, and acceptance checks when the user asks for an actionable non-coder output.\n`;
    prompt += `If a required detail does not fit a heading cleanly, add a concise subheading under the closest matching section instead of omitting it.\n`;
    if (isTrustedNoncoderTemplate) {
      prompt += `For this trusted non-coder template, produce an operator-ready deliverable rather than a compact summary. Unless the user explicitly asks for brevity, aim for 700-1100 output tokens and make every major option, persona, feature, risk, pricing tier, or step concrete enough to act on.\n`;
      prompt += `For comparison tasks, compare each named or reasonably inferred option before giving a recommendation.\n`;
    }
    if (primaryDeliverableContract) {
      prompt += `Use this shape-specific deliverable contract as the primary output contract. It replaces generic template headings when they conflict with the user's requested deliverable:\n`;
      prompt += `\`\`\`markdown\n${primaryDeliverableContract}\n\`\`\`\n\n`;
    } else if (template.outputExpected?.length) {
      prompt += `Expected sections:\n`;
      for (const section of template.outputExpected) {
        prompt += `- ${section}\n`;
      }
      prompt += `\n`;
    }
    if (!primaryDeliverableContract && template.outputTemplate) {
      const renderedOutputTemplate = renderTemplateIntent(template.outputTemplate, inputs);
      prompt += `Use these headings and labels exactly where applicable:\n`;
      prompt += `\`\`\`markdown\n${renderedOutputTemplate}\n\`\`\`\n\n`;
    }
    if (taskShapeGuidance.length) {
      prompt += `Task-shape requirements override generic template headings when they conflict:\n`;
      for (const item of taskShapeGuidance) {
        prompt += `- ${item}\n`;
      }
      prompt += `Do not let SWOT, risk, overview, or documentation-wrapper sections replace the requested plan, comparison, FAQ, prioritization, persona, or criteria deliverable.\n\n`;
    }
  }

  if (request.fileScope?.length) {
    prompt += `### File Scope\n- Allowed scope: ${request.fileScope.join(', ')}\n\n`;
  }

  if (previousOutput && previousOutput.trim()) {
    prompt += `### Previous Output (for context)\n${previousOutput}\n`;
    prompt += `\n*(The user is requesting a follow-up or refinement of the above.)*\n\n---\n\n`;
  }

  prompt += `### Output Contract\n`;
  prompt += `- Return a final answer directly in Markdown.\n`;
  prompt += `- Use short, explicit section headers only when they add clarity.\n`;
  prompt += `- Keep the result implementation-ready and grounded in the supplied inputs.\n`;
  prompt += `- Do not describe your internal process or governance workflow.\n\n`;
  prompt += `Please analyze the above information and provide a comprehensive, structured response following CVF guidelines.`;

  return prompt;
}
