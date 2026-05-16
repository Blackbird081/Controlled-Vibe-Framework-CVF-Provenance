'use client';

import { ArrowRight, FileCheck2, ShieldCheck, Sparkles } from 'lucide-react';

import ArtifactExportPanel, { type ArtifactExportRequest } from '@/components/ArtifactExportPanel';
import { useLanguage } from '@/lib/i18n';

const COPY = {
  en: {
    label: 'Artifact Export',
    title: 'Turn approved work into an HTML review packet',
    intro: 'This page is for people who need a clean, reviewable version of AI-assisted work. It keeps the source, receipt anchor, status, and claim boundary visible so the next reviewer does not have to guess what happened.',
    boundary: 'HTML presentation candidate only. PDF, image export, and governed-artifact generation claims are out of scope for this surface.',
    newKnowledgeTitle: 'What new knowledge should become',
    newKnowledgeBody: 'When CVF absorbs useful knowledge, the web surface should turn it into clearer choices, review packets, receipts, and handoff notes. The user benefit is better review and safer reuse, not more hidden complexity.',
    flow: ['Source', 'Review', 'Handoff'],
    cards: [
      ['Bring knowledge into the review', 'Approved source text can become a clean review page without changing the meaning of the original material.'],
      ['Keep the receipt visible', 'The output keeps the receipt anchor and review boundary close to the work, so a non-coder can see what is safe to rely on.'],
      ['Hand off with less guessing', 'The HTML candidate is meant for review, sharing, and handoff. It does not replace human judgment or live proof.'],
    ],
  },
  vi: {
    label: 'Xuất artifact',
    title: 'Biến phần đã duyệt thành packet HTML để review',
    intro: 'Trang này dành cho người cần một bản dễ đọc của công việc có AI hỗ trợ. Nguồn, receipt, trạng thái và ranh giới claim được giữ rõ để người review tiếp theo không phải đoán.',
    boundary: 'Chỉ là HTML presentation candidate. PDF, xuất ảnh và claim tạo artifact có proof riêng không nằm trong surface này.',
    newKnowledgeTitle: 'Kiến thức mới nên trở thành gì',
    newKnowledgeBody: 'Khi CVF hấp thu kiến thức hữu ích, web surface nên biến nó thành lựa chọn rõ hơn, packet review, receipt và ghi chú bàn giao. Lợi ích là review tốt hơn và tái sử dụng an toàn hơn, không phải thêm độ phức tạp ẩn.',
    flow: ['Nguồn', 'Review', 'Bàn giao'],
    cards: [
      ['Đưa kiến thức vào review', 'Nội dung nguồn đã duyệt có thể trở thành trang review sạch mà không đổi ý nghĩa gốc.'],
      ['Giữ receipt dễ thấy', 'Kết quả giữ receipt và ranh giới review gần với nội dung để non-coder biết phần nào có thể tin cậy.'],
      ['Bàn giao ít phỏng đoán hơn', 'Bản HTML dùng để review, chia sẻ và bàn giao. Nó không thay thế phán đoán của người review hoặc live proof.'],
    ],
  },
};

const starterRequest: ArtifactExportRequest = {
  title: 'Customer Onboarding Review Packet',
  sourcePath: 'workspace/reviews/customer-onboarding.md',
  sourceContent: [
    '# Customer Onboarding Review Packet',
    '',
    'Memory class: FULL_RECORD',
    '',
    'Status: READY_FOR_REVIEW',
    '',
    '## Summary',
    '',
    'This packet captures the current onboarding plan, the checks already made, and the open decisions that still need a human review.',
    '',
    '## Claim Boundary',
    '',
    'This is an HTML presentation candidate. It helps review and handoff. It is not a live governance proof by itself.',
  ].join('\n'),
  memoryClass: 'FULL_RECORD',
  status: 'READY_FOR_REVIEW',
  claimBoundary: 'HTML presentation candidate only. It helps review and handoff, but it is not governed artifact generation proof.',
  receiptAnchor: 'receipt-customer-onboarding-demo',
};

const cardIcons = [Sparkles, ShieldCheck, FileCheck2];

export default function ArtifactsPage() {
  const { language } = useLanguage();
  const copy = COPY[language === 'vi' ? 'vi' : 'en'];

  return (
    <div className="mx-auto max-w-7xl space-y-6 px-4 py-6">
      <header className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm dark:border-gray-800 dark:bg-gray-900">
        <div className="flex flex-col gap-5 lg:flex-row lg:items-start lg:justify-between">
          <div className="max-w-3xl">
            <div className="mb-2 flex items-center gap-2 text-xs font-bold uppercase tracking-wide text-indigo-600 dark:text-indigo-300">
              <FileCheck2 className="h-4 w-4" aria-hidden="true" />
              {copy.label}
            </div>
            <h1 className="text-2xl font-bold text-gray-950 dark:text-white">{copy.title}</h1>
            <p className="mt-3 text-sm leading-6 text-gray-600 dark:text-gray-300">{copy.intro}</p>
          </div>
          <div className="rounded-xl border border-amber-200 bg-amber-50 px-4 py-3 text-xs leading-5 text-amber-800 dark:border-amber-900/70 dark:bg-amber-950/30 dark:text-amber-200">{copy.boundary}</div>
        </div>
      </header>

      <section className="grid gap-4 md:grid-cols-3" aria-label="Artifact export value">
        {copy.cards.map(([title, body], index) => {
          const Icon = cardIcons[index];
          return (
            <article key={title} className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm dark:border-gray-800 dark:bg-gray-900">
              <div className="mb-4 inline-flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600 dark:bg-indigo-950/40 dark:text-indigo-300">
                <Icon className="h-4 w-4" aria-hidden="true" />
              </div>
              <h2 className="text-sm font-semibold text-gray-950 dark:text-white">{title}</h2>
              <p className="mt-2 text-sm leading-6 text-gray-600 dark:text-gray-300">{body}</p>
            </article>
          );
        })}
      </section>

      <section className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm dark:border-gray-800 dark:bg-gray-900">
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="text-sm font-semibold text-gray-950 dark:text-white">{copy.newKnowledgeTitle}</h2>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-gray-600 dark:text-gray-300">{copy.newKnowledgeBody}</p>
          </div>
          <div className="flex items-center gap-2 rounded-lg border border-gray-200 px-3 py-2 text-xs font-semibold text-gray-600 dark:border-gray-800 dark:text-gray-300">
            {copy.flow.map((item, index) => (
              <span key={item} className="inline-flex items-center gap-2">
                {index > 0 && <ArrowRight className="h-3.5 w-3.5" aria-hidden="true" />}
                {item}
              </span>
            ))}
          </div>
        </div>
      </section>

      <ArtifactExportPanel initialRequest={starterRequest} />
    </div>
  );
}
