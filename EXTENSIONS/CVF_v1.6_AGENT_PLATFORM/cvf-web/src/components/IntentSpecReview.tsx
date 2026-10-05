// Text Encoding Exception: Vietnamese user-facing copy and matching localization fixtures.
'use client';

import { useState } from 'react';
import { IntentSpecConfirmation } from './IntentSpecConfirmation';
import {
    acknowledgeIntentSpecReview, buildReviewedDraftPacket, createIntentSpecReview,
    decisionNeedsReview, getDecisionLabel, getPendingReviewDecisions, INTENT_REVIEW_QUESTIONS,
    isCurrentReviewAcknowledged, synchronizeIntentSpecReview, updateReviewDecision,
    type DecisionDisposition, type IntentSpecReviewState, type ReviewLanguage, type ReviewQuestionId,
} from '@/lib/intent-spec-review';

export function useIntentSpecReview(
    templateId: string, values: Record<string, string>, packetSource: string, language: ReviewLanguage,
) {
    const [stored, setStored] = useState(() => createIntentSpecReview(values, packetSource));
    const review = synchronizeIntentSpecReview(stored, values, packetSource);
    // Render-time reconciliation prevents exporting a stale revision before an effect runs.
    if (review !== stored) setStored(review);
    const enabled = templateId === 'app_builder_complete';
    const update = (id: ReviewQuestionId, change: Parameters<typeof updateReviewDecision>[2]) => {
        setStored(previous => updateReviewDecision(
            synchronizeIntentSpecReview(previous, values, packetSource), id, change,
        ));
    };
    const acknowledge = () => setStored(previous => acknowledgeIntentSpecReview(
        synchronizeIntentSpecReview(previous, values, packetSource),
    ));
    return {
        review: enabled ? review : null, update, acknowledge,
        spec: enabled ? buildReviewedDraftPacket(review, language) : packetSource,
        canContinue: !enabled || (isCurrentReviewAcknowledged(review) && getPendingReviewDecisions(review).length === 0),
    };
}

interface Props {
    review: IntentSpecReviewState;
    language: ReviewLanguage;
    onUpdate: (id: ReviewQuestionId, change: Parameters<typeof updateReviewDecision>[2]) => void;
    onAcknowledge: () => void;
}

export function IntentSpecReview({ review, language, onUpdate, onAcknowledge }: Props) {
    const [showAll, setShowAll] = useState(false);
    const vi = language === 'vi';
    const pending = getPendingReviewDecisions(review);
    const acknowledged = isCurrentReviewAcknowledged(review);
    const shown = showAll ? review.decisions : review.decisions.slice(0, 3);
    const control = 'min-h-11 rounded-lg border border-gray-300 bg-white p-2 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:border-gray-600 dark:bg-gray-900 dark:text-gray-100';
    return (
        <section aria-label={vi ? 'Review yêu cầu' : 'Requirements review'}
            className="mb-4 rounded-xl border border-gray-200 p-4 dark:border-gray-700">
            <h4 className="text-sm font-semibold text-gray-900 dark:text-gray-100">
                {vi ? 'Làm rõ trước khi bàn giao' : 'Clarify before handoff'}
            </h4>
            <p className="mt-2 text-sm text-gray-600 dark:text-gray-300">
                {vi ? 'Bạn quyết định các quy tắc nghiệp vụ. Builder sẽ chọn cách triển khai trong phạm vi đó.' : 'You decide the business rules. The builder chooses how to implement within those boundaries.'}
            </p>
            <p className="mt-2 text-xs text-gray-600 dark:text-gray-400">
                {vi ? 'Các câu hỏi là gợi ý, không tự phát hiện mọi thiếu sót. Bản review chỉ nằm trong phiên này; tải bản nháp để giữ nội dung.' : 'These prompts do not detect every gap. Review stays in this session only; download the draft to keep its content.'}
            </p>
            <div role="status" className="my-3 text-sm text-gray-800 dark:text-gray-200">
                {vi ? 'Phiên bản' : 'Revision'} {review.revision} · {pending.length} {vi ? 'mục còn cần quyết định' : 'items need a decision'}
                {' · '}{acknowledged ? (vi ? 'Đã xem bản này' : 'Viewed this revision') : (vi ? 'Chưa xem bản này' : 'Not viewed yet')}
            </div>
            <div className="space-y-4">
                {shown.map(decision => {
                    const question = INTENT_REVIEW_QUESTIONS.find(item => item.id === decision.id)!;
                    const textId = `intent-review-${decision.id}`;
                    return (
                        <div key={decision.id} className="rounded-lg border border-gray-200 p-3 dark:border-gray-700">
                            <label htmlFor={textId} className="block text-sm font-medium text-gray-900 dark:text-gray-100">
                                {question[language]}
                            </label>
                            <details className="my-2 text-xs text-gray-600 dark:text-gray-400">
                                <summary className="cursor-pointer">{vi ? 'Thông tin đang có trong brief' : 'Current brief information'}</summary>
                                {question.fields.map(field => (
                                    <p key={field} className="mt-1 whitespace-pre-wrap">{review.values[field] || (vi ? 'Chưa có thông tin.' : 'No information yet.')}</p>
                                ))}
                            </details>
                            <textarea id={textId} rows={2} value={decision.answer}
                                className={`${control} w-full`}
                                placeholder={vi ? 'Trả lời, nêu mâu thuẫn hoặc lý do không áp dụng…' : 'Answer, describe a conflict or explain why it does not apply…'}
                                onChange={event => onUpdate(decision.id, { answer: event.target.value })} />
                            <label className="mt-2 flex flex-col gap-1 text-xs text-gray-600 dark:text-gray-400">
                                {vi ? 'Trạng thái câu trả lời' : 'Answer status'}
                                <select value={decision.disposition} className={control}
                                    onChange={event => onUpdate(decision.id, { disposition: event.target.value as DecisionDisposition })}>
                                    {(['OPEN', 'ANSWERED', 'NOT_APPLICABLE', 'CONFLICT'] as const).map(value => (
                                        <option key={value} value={value}>{getDecisionLabel(value, language)}</option>
                                    ))}
                                </select>
                            </label>
                            {decision.disposition === 'NOT_APPLICABLE' && !decision.answer.trim() && (
                                <p className="mt-2 text-xs text-amber-700 dark:text-amber-300">
                                    {vi ? 'Hãy ghi lý do không áp dụng.' : 'Please give a reason why this does not apply.'}
                                </p>
                            )}
                            {decision.needsReconfirmation && (
                                <div className="mt-2 text-xs text-amber-700 dark:text-amber-300">
                                    <p>{vi ? 'Brief liên quan đã thay đổi. Câu trả lời cũ được giữ để bạn kiểm lại.' : 'Related brief information changed. The old answer is kept for you to review.'}</p>
                                    <button type="button" className={`${control} mt-2`}
                                        onClick={() => onUpdate(decision.id, { reconfirm: true })}>
                                        {vi ? 'Giữ câu trả lời cho bản mới' : 'Keep answer for new revision'}
                                    </button>
                                </div>
                            )}
                            {decisionNeedsReview(decision) && !decision.needsReconfirmation && (
                                <p className="mt-2 text-xs text-amber-700 dark:text-amber-300">
                                    {vi ? 'Mục này vẫn còn mở trong bản nháp.' : 'This item remains open in the draft.'}
                                </p>
                            )}
                        </div>
                    );
                })}
            </div>
            <button type="button" className={`${control} mt-3`} onClick={() => setShowAll(value => !value)}>
                {showAll ? (vi ? 'Thu gọn' : 'Show fewer') : (vi ? `Xem đủ ${review.decisions.length} câu hỏi` : `Show all ${review.decisions.length} questions`)}
            </button>
            <p className="my-3 text-xs text-gray-600 dark:text-gray-400">
                {vi ? 'Bạn vẫn có thể xuất bản nháp với các mục chưa quyết. Đã xem không đồng nghĩa duyệt build hoặc spec đã đầy đủ.' : 'You can export a draft with unresolved items. Viewing it does not approve a build or prove specification completeness.'}
            </p>
            <button type="button" disabled={acknowledged} onClick={onAcknowledge}
                className="min-h-11 rounded-lg bg-indigo-600 px-3 text-sm text-white focus:ring-2 focus:ring-indigo-400 disabled:opacity-50">
                {vi ? 'Tôi đã xem bản nháp này' : 'I have viewed this draft'}
            </button>
            <IntentSpecConfirmation review={review} language={language} />
        </section>
    );
}
