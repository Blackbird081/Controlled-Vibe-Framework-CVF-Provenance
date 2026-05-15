import { describe, expect, it } from 'vitest';
import { buildExecutionPrompt } from './execute-prompt-contract';
import type { ExecutionRequest } from '@/lib/ai';

const baseRequest: ExecutionRequest = {
  templateId: 'web_build_handoff',
  templateName: 'Bàn giao Web cho Agent',
  inputs: {
    websiteGoal: 'Build an internal operations portal',
    audience: 'Non-technical supervisors',
  },
  intent: 'Tôi là non-coder và muốn dựng web mới',
};

describe('buildExecutionPrompt', () => {
  it('attaches CVF Web Redesign DNA for non-coder web handoff requests', () => {
    const prompt = buildExecutionPrompt(baseRequest);

    expect(prompt).toContain('Bound UX Skill Context');
    expect(prompt).toContain('Template Output Contract');
    expect(prompt).toContain('Do not return the raw skeleton');
    expect(prompt).toContain('Acceptance Checklist');
    expect(prompt).toContain('CVF Web Redesign DNA');
    expect(prompt).toContain('professional command workspace');
    expect(prompt).toContain('preserve existing routes, auth, API payloads');
  });

  it('injects exact template headings into the live prompt for guarded UX packets', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'web_ux_redesign_system',
      templateName: 'CVF Web UX Redesign System',
      intent: 'Create a governed UX redesign packet',
    });

    expect(prompt).toContain('Use these headings and labels exactly where applicable');
    expect(prompt).toContain('## 7. Review Gate & Acceptance Checklist');
    expect(prompt).toContain('What requires explicit builder approval');
  });

  it('treats trusted form output templates as minimum outlines, not compression targets', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'strategy_analysis',
      templateName: 'Strategy Analysis',
      intent: 'Compare launch options with assumptions, concrete next steps, and acceptance checks.',
      inputs: {
        topic: 'Launch options',
        context: 'Compare three go-to-market options for a simple booking app.',
        options: 'SaaS marketplace, direct sales, local partnership',
        constraints: 'Small salon buyers, limited budget',
        priority: 'Growth',
      },
    });

    expect(prompt).toContain('minimum outline, not a compression target');
    expect(prompt).toContain('assumptions, rationale, concrete next actions, and acceptance checks');
    expect(prompt).toContain('aim for 700-1100 output tokens');
    expect(prompt).toContain('compare each named or reasonably inferred option');
    expect(prompt).toContain('Task-shape requirements override generic template headings when they conflict');
    expect(prompt).toContain('Do not let SWOT, risk, overview, or documentation-wrapper sections replace the requested plan, comparison, FAQ, prioritization, persona, or criteria deliverable');
    expect(prompt).toContain('Decision Comparison Memo');
    expect(prompt).toContain('It replaces generic template headings when they conflict');
    expect(prompt).not.toContain('Operational Documentation Packet');
  });

  it('uses a plan-first contract for operations and retention plan tasks', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'strategy_analysis',
      templateName: 'Strategy Analysis',
      intent: 'Create a 30-day operations plan for launching a neighborhood tutoring marketplace.',
      inputs: {
        topic: 'Ops plan',
        context: 'Create a 30-day operations plan for launch.',
        options: 'Tutor onboarding, parent signup, matching workflow',
        constraints: 'Small team, limited budget',
        priority: 'Growth',
      },
    });

    expect(prompt).toContain('Task-shape requirements');
    expect(prompt).toContain('Operator Action Plan');
    expect(prompt).toContain('Timeline And Owners');
    expect(prompt).toContain('First 24-72 Hours');
    expect(prompt).toContain('Plan shape');
    expect(prompt).toContain('timeline or phased action table with owner/role, action, concrete artifact, success metric, and acceptance check');
    expect(prompt).not.toContain('SWOT Analysis');
  });

  it('uses an FAQ-first contract for FAQ outline tasks', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'documentation',
      templateName: 'Documentation',
      intent: 'Create an FAQ outline for a small online course checkout flow.',
      inputs: {
        subject: 'FAQ plan',
        currentNotes: 'Small online course checkout flow.',
        readerGoal: 'Operators can publish a useful FAQ.',
        audience: 'Customers and support operators',
        mustPreserve: 'Payment and enrollment terms',
      },
    });

    expect(prompt).toContain('FAQ shape');
    expect(prompt).toContain('FAQ Outline');
    expect(prompt).toContain('FAQ Entries');
    expect(prompt).toContain('Publish Readiness Checks');
    expect(prompt).toContain('8-12 concrete questions with direct answers');
    expect(prompt).toContain('payment/access/troubleshooting');
    expect(prompt).not.toContain('Operational Documentation Packet');
  });

  it('keeps the documentation skeleton plus shape guidance for dashboard criteria tasks', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'documentation',
      templateName: 'Documentation',
      intent: 'Write acceptance criteria for a dashboard that shows weekly sales, conversion, and open tasks.',
      inputs: {
        subject: 'Acceptance criteria',
        currentNotes: 'Dashboard shows weekly sales, conversion, and open tasks.',
        readerGoal: 'Operator can verify the dashboard before handoff.',
        audience: 'Non-technical operator',
        mustPreserve: 'Weekly sales, conversion, open tasks',
      },
    });

    expect(prompt).toContain('Acceptance-criteria shape');
    expect(prompt).toContain('Operational Documentation Packet');
    expect(prompt).not.toContain('Acceptance Criteria Packet');
    expect(prompt).toContain('observable and testable');
    expect(prompt).toContain('data source, refresh/state expectations, error/empty states, and pass/fail checks');
  });

  it('keeps the feature-prioritization skeleton plus shape guidance for backlog triage tasks', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'feature_prioritization',
      templateName: 'Feature Prioritization',
      intent: 'Triage a backlog for a volunteer event signup app with limited engineering time.',
      inputs: {
        features: 'Check-in QR codes, waitlist, volunteer roles, reminder emails',
        goal: 'Choose MVP scope',
        constraints: 'Limited engineering time',
        framework: 'RICE',
      },
    });

    expect(prompt).toContain('Prioritization shape');
    expect(prompt).toContain('Feature Prioritization Output');
    expect(prompt).toContain('Scoring Matrix');
    expect(prompt).not.toContain('Prioritization Decision');
    expect(prompt).toContain('score or rank each item');
    expect(prompt).toContain('next-step checklist and acceptance checks');
  });

  it('keeps generic template skeletons when no shape-specific contract matches', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'strategy_analysis',
      templateName: 'Strategy Analysis',
      intent: 'Review business strategy and summarize the major considerations.',
      inputs: {
        topic: 'Market entry',
        context: 'A small business is considering a new service line.',
        options: '',
        constraints: 'Limited budget',
        priority: 'Stability',
      },
    });

    expect(prompt).toContain('Strategy Analysis Output');
    expect(prompt).toContain('SWOT Analysis');
    expect(prompt).not.toContain('shape-specific deliverable contract');
  });

  it('renders the operator-plan template family without falling back to SWOT sections', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'operator_plan',
      templateName: 'Operator Plan',
      intent: 'Create a 30-day operations plan for launching a tutoring marketplace.',
      inputs: {
        goal: 'Launch tutoring marketplace',
        context: 'Need tutor onboarding, parent signup, and matching workflow.',
        timeline: '30 days',
        owners: 'Founder, ops lead',
        constraints: 'Small team, limited budget',
      },
    });

    expect(prompt).toContain('Operator Action Plan');
    expect(prompt).toContain('Use these headings and labels exactly where applicable');
    expect(prompt).toContain('Detailed Timeline');
    expect(prompt).toContain('Operating Checklist');
    expect(prompt).not.toContain('SWOT Analysis');
    expect(prompt).not.toContain('shape-specific deliverable contract');
  });

  it('renders the acceptance-criteria template family as the primary skeleton', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'acceptance_criteria',
      templateName: 'Acceptance Criteria',
      intent: 'Write acceptance criteria for a sales dashboard.',
      inputs: {
        feature: 'Weekly sales dashboard',
        context: 'Shows weekly sales, conversion, and open tasks.',
        users: 'Operator and manager',
        states: 'Empty, stale data, permission denied',
      },
    });

    expect(prompt).toContain('Acceptance Criteria Packet');
    expect(prompt).toContain('Criteria By Workflow');
    expect(prompt).toContain('Data/State Requirement');
    expect(prompt).not.toContain('Operational Documentation Packet');
    expect(prompt).not.toContain('shape-specific deliverable contract');
  });

  it('does not attach CVF Web Redesign DNA for unrelated templates', () => {
    const prompt = buildExecutionPrompt({
      ...baseRequest,
      templateId: 'strategy_analysis',
      templateName: 'Strategy Analysis',
      intent: 'Review business strategy',
    });

    expect(prompt).not.toContain('CVF Web Redesign DNA');
  });
});
