'use client';

import { useMemo, useState } from 'react';
import { ArrowRight, CheckCircle2, ClipboardCheck, ShieldCheck, TriangleAlert } from 'lucide-react';

import { useLanguage } from '@/lib/i18n';
import { validateHandoff, type HandoffDecision } from '@/lib/agent-handoff-validator';
import type { AgentRole } from '@/lib/multi-agent';

const COPY = {
  en: {
    label: 'Agent Handoff',
    title: 'Pass reviewed work forward with less guesswork',
    intro: 'Check whether a reviewed packet carries enough context for the next person or assistant to continue safely.',
    from: 'From step',
    to: 'Next step',
    status: 'Previous step status',
    output: 'Reviewed summary',
    outputPlaceholder: 'Paste the short review summary that should move forward.',
    check: 'Handoff check',
    carried: 'The reviewed context is present and can move forward.',
    missing: 'The reviewed context is missing and should not move forward yet.',
    summary: 'Carried summary',
    issues: 'Review notes',
    noIssues: 'No handoff issues were found. Keep the source, receipt, and claim boundary visible for review.',
    benefitsTitle: 'Why this helps non-coders',
    boundary: 'This page checks a local handoff shape. It does not claim a live multi-agent transfer by itself.',
    benefits: [
      'The next person can see what was reviewed and what still needs attention.',
      'The visible receipt makes the packet easier to trust, share, and revisit.',
      'New knowledge becomes a clear handoff note instead of hidden background context.',
    ],
  },
  vi: {
    label: 'Bàn giao cho agent',
    title: 'Bàn giao phần đã review với ít phỏng đoán hơn',
    intro: 'Kiểm tra packet đã review có đủ ngữ cảnh để người hoặc assistant tiếp theo tiếp tục an toàn hay không.',
    from: 'Bước trước',
    to: 'Bước tiếp theo',
    status: 'Trạng thái bước trước',
    output: 'Tóm tắt đã review',
    outputPlaceholder: 'Dán tóm tắt ngắn cần chuyển tiếp.',
    check: 'Kiểm tra bàn giao',
    carried: 'Ngữ cảnh đã review có đủ để chuyển tiếp.',
    missing: 'Ngữ cảnh đã review đang thiếu và chưa nên chuyển tiếp.',
    summary: 'Tóm tắt được chuyển tiếp',
    issues: 'Ghi chú review',
    noIssues: 'Không phát hiện vấn đề trong handoff. Vẫn cần giữ nguồn, receipt và ranh giới claim để review.',
    benefitsTitle: 'Vì sao hữu ích cho non-coder',
    boundary: 'Trang này kiểm tra hình dạng handoff cục bộ. Nó không tự claim live multi-agent transfer.',
    benefits: [
      'Người tiếp theo thấy rõ phần nào đã review và phần nào còn cần chú ý.',
      'Receipt nhìn thấy được giúp packet dễ tin, dễ chia sẻ và dễ xem lại.',
      'Kiến thức mới trở thành ghi chú bàn giao rõ ràng thay vì ngữ cảnh ẩn.',
    ],
  },
};

const DECISION_STYLE: Record<HandoffDecision, string> = {
  ALLOW: 'border-emerald-200 bg-emerald-50 text-emerald-800 dark:border-emerald-900/60 dark:bg-emerald-950/30 dark:text-emerald-100',
  WARN: 'border-amber-200 bg-amber-50 text-amber-800 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-100',
  BLOCK: 'border-red-200 bg-red-50 text-red-800 dark:border-red-900/60 dark:bg-red-950/30 dark:text-red-100',
};

export default function AgentHandoffPage() {
  const { language } = useLanguage();
  const copy = COPY[language === 'vi' ? 'vi' : 'en'];
  const [fromAgent, setFromAgent] = useState<AgentRole>('architect');
  const [toAgent, setToAgent] = useState<AgentRole>('builder');
  const [status, setStatus] = useState<'completed' | 'running' | 'failed'>('completed');
  const [output, setOutput] = useState('The new knowledge is ready for review. Keep the source note, receipt, and claim boundary together.');

  const result = useMemo(() => validateHandoff({
    workflow: { id: 'web-review-demo', name: 'New Knowledge Review', status: status === 'failed' ? 'failed' : 'completed' },
    fromTask: { id: 'source-review', agentId: fromAgent, status, output },
    toAgentId: toAgent,
    toAgentRole: toAgent,
  }), [fromAgent, output, status, toAgent]);

  return (
    <div className="mx-auto max-w-7xl space-y-6 px-4 py-6 text-gray-900 dark:text-gray-100">
      <header className="border-b border-gray-200 pb-5 dark:border-white/[0.08]">
        <div className="mb-2 flex items-center gap-2 text-xs font-bold uppercase tracking-wide text-indigo-600 dark:text-indigo-300">
          <ClipboardCheck className="h-4 w-4" aria-hidden="true" />
          {copy.label}
        </div>
        <h1 className="text-3xl font-bold tracking-normal text-gray-950 dark:text-white">{copy.title}</h1>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-gray-600 dark:text-gray-300">{copy.intro}</p>
      </header>

      <section className="grid gap-5 lg:grid-cols-[minmax(0,0.95fr)_minmax(0,1.05fr)]">
        <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
          <div className="flex items-center gap-2">
            <ShieldCheck className="h-5 w-5 text-indigo-500" aria-hidden="true" />
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">{copy.check}</h2>
          </div>

          <div className="mt-5 grid gap-4 sm:grid-cols-2">
            <SelectField label={copy.from} value={fromAgent} onChange={value => setFromAgent(value as AgentRole)} options={['orchestrator', 'architect', 'builder', 'reviewer']} />
            <SelectField label={copy.to} value={toAgent} onChange={value => setToAgent(value as AgentRole)} options={['orchestrator', 'architect', 'builder', 'reviewer']} />
            <SelectField label={copy.status} value={status} onChange={value => setStatus(value as 'completed' | 'running' | 'failed')} options={['completed', 'running', 'failed']} />
            <div className="hidden items-end justify-center sm:flex">
              <ArrowRight className="mb-3 h-5 w-5 text-gray-400" aria-hidden="true" />
            </div>
            <label className="sm:col-span-2 text-sm font-semibold">
              {copy.output}
              <textarea value={output} onChange={event => setOutput(event.target.value)} placeholder={copy.outputPlaceholder} rows={7} className="mt-1 w-full resize-y rounded-lg border border-gray-200 bg-gray-50 px-3 py-2 text-sm leading-6 dark:border-gray-700 dark:bg-gray-950" />
            </label>
          </div>

          <div className={`mt-4 rounded-lg border p-4 text-sm leading-6 ${DECISION_STYLE[result.decision]}`}>
            <div className="font-semibold">Decision: {result.decision}</div>
            <div className="mt-1">{result.contextCarried ? copy.carried : copy.missing}</div>
          </div>
        </div>

        <div className="space-y-5">
          <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">{copy.summary}</h2>
            <p className="mt-3 rounded-lg border border-gray-200 bg-gray-50 p-4 text-sm leading-6 text-gray-600 dark:border-gray-800 dark:bg-gray-950 dark:text-gray-300">{result.outputSummary}</p>
            <div className="mt-4 rounded-lg border border-amber-200 bg-amber-50 p-4 text-sm leading-6 text-amber-800 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-100">{copy.boundary}</div>
          </div>

          <div className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
            <h2 className="text-lg font-semibold text-gray-950 dark:text-white">{copy.issues}</h2>
            {result.issues.length > 0 ? (
              <div className="mt-4 space-y-3">
                {result.issues.map(issue => (
                  <div key={issue.code} className="flex gap-3 rounded-lg border border-amber-200 bg-amber-50 p-3 text-sm leading-6 text-amber-800 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-100">
                    <TriangleAlert className="mt-1 h-4 w-4 shrink-0" aria-hidden="true" />
                    <span>{language === 'vi' ? issue.friendlyMessageVi : issue.friendlyMessage}</span>
                  </div>
                ))}
              </div>
            ) : (
              <p className="mt-3 text-sm leading-6 text-gray-600 dark:text-gray-300">{copy.noIssues}</p>
            )}
          </div>
        </div>
      </section>

      <section className="rounded-lg border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-gray-900">
        <h2 className="text-lg font-semibold text-gray-950 dark:text-white">{copy.benefitsTitle}</h2>
        <div className="mt-4 grid gap-3 md:grid-cols-3">
          {copy.benefits.map(item => (
            <div key={item} className="flex gap-3 text-sm leading-6 text-gray-600 dark:text-gray-300">
              <CheckCircle2 className="mt-1 h-4 w-4 shrink-0 text-emerald-500" aria-hidden="true" />
              <span>{item}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

function SelectField({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (value: string) => void }) {
  return (
    <label className="text-sm font-semibold">
      {label}
      <select value={value} onChange={event => onChange(event.target.value)} className="mt-1 w-full rounded-lg border border-gray-200 bg-gray-50 px-3 py-2 text-sm dark:border-gray-700 dark:bg-gray-950">
        {options.map(option => <option key={option} value={option}>{option}</option>)}
      </select>
    </label>
  );
}
