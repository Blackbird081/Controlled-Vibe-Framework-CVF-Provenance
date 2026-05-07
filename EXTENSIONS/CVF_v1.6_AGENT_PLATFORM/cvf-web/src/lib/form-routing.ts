/**
 * CVF Trusted Form Router
 * =======================
 * W126-T1 CP1 — Explicit intent-to-form mapping for the trusted form subset.
 *
 * Hard contracts:
 *   - Only 8 explicitly audited forms are eligible (see W126_TRUSTED_FORM_SUBSET_AUDIT.md)
 *   - This module is evaluated before wizard routing so audited form intents
 *     are not shadowed by broad wizard keywords.
 *   - Activation is pattern-based; ambiguity boundaries are documented per form
 *   - Any addition to TRUSTED_FORM_MAP requires a new audit entry + commit
 *
 * W126-T1 CP1
 *
 * @module lib/form-routing
 */

export interface TrustedFormEntry {
  id: string;
  label: string;
  /** Patterns that activate this form from plain-language input */
  activationPatterns: RegExp[];
  /** Human-readable note on when the wizard family should win instead */
  wizardWinsWhen: string;
}

export interface TrustedFormMatch {
  formKey: string;
  id: string;
  label: string;
}

/**
 * W126 trusted form subset — 8 explicitly audited forms.
 * Do not add entries without a matching audit row in W126_TRUSTED_FORM_SUBSET_AUDIT.md.
 */
export const TRUSTED_FORM_MAP: Record<string, TrustedFormEntry> = {
  'email_template': {
    id: 'email_template',
    label: '📧 Email Template',
    activationPatterns: [
      /\b(draft|write|compose|send|follow.?up)\s+(an?\s+)?email\b/i,
      /\bemail\s+(to|template|draft)\b/i,
      /\bmẫu email\b/i,
      /viết email|soạn email|thư điện tử/i,
    ],
    wizardWinsWhen: 'user describes a full content or marketing strategy, not a specific email task',
  },
  'documentation': {
    id: 'documentation',
    label: '📄 Documentation',
    activationPatterns: [
      /\bdocument(ation)?\s+(this|a|my|the|for)\b/i,
      /\b(SOP|how.?to guide|process doc|handoff doc)\b/i,
      /viết tài liệu|tạo tài liệu|tài liệu kỹ thuật|tài liệu quy trình|bàn giao tài liệu/i,
      /quy trình\s+(làm việc|tiếp nhận|onboard)/i,
    ],
    wizardWinsWhen: 'user asks for content strategy, research report, or a marketing campaign',
  },
  'competitor_review': {
    id: 'competitor_review',
    label: '🔍 Competitor Review',
    activationPatterns: [
      /\bcompetitors?\b/i,
      /\b(competitive analysis|competitive landscape|compare competitors?)\b/i,
      /\brival(s)?\b/i,
      /đối thủ/i,
      /phân tích đối thủ/i,
    ],
    wizardWinsWhen: 'user says "business strategy" broadly without specific competitor focus',
  },
  'risk_assessment': {
    id: 'risk_assessment',
    label: '⚠️ Risk Assessment',
    activationPatterns: [
      /\brisk assessment\b/i,
      /\bassess\s+(the\s+)?risks?\b/i,
      /\bidentify\s+(the\s+)?risks?\b/i,
      /\brisk analysis\b/i,
      /rủi ro/i,
      /phân tích rủi ro/i,
      /đánh giá rủi ro/i,
    ],
    wizardWinsWhen: 'user says "security assessment" or "penetration test" (security-assessment wizard wins)',
  },
  'user_persona': {
    id: 'user_persona',
    label: '👤 User Persona',
    activationPatterns: [
      /\buser persona\b/i,
      /\bbuyer persona\b/i,
      /\btarget audience\b/i,
      /\bcustomer profile\b/i,
      /\bideal customer\b/i,
      /người dùng mục tiêu/i,
      /hồ sơ khách hàng/i,
      /khách hàng mục tiêu/i,
    ],
    wizardWinsWhen: 'user says "product design" broadly or "design my app"',
  },
  'feature_prioritization': {
    id: 'feature_prioritization',
    label: '📋 Feature Prioritization',
    activationPatterns: [
      /\bprioritize\s+features?\b/i,
      /\bfeature prioritization\b/i,
      /\bwhich features?\b/i,
      /\bfeature list\b/i,
      /\bwhat to build first\b/i,
      /ưu tiên tính năng/i,
      /\broadmap priorit/i,
    ],
    wizardWinsWhen: 'user says "build my app" or "design my product" (wizard wins)',
  },
  'pricing_strategy': {
    id: 'pricing_strategy',
    label: '💰 Pricing Strategy',
    activationPatterns: [
      /\bpricing model\b/i,
      /\bhow to price\b/i,
      /\bprice\s+(my|a|the)\s+(product|service|app|saas)\b/i,
      /giá bán/i,
      /chiến lược giá/i,
      /định giá/i,
    ],
    wizardWinsWhen: 'user says "business strategy" broadly without pricing-specific focus',
  },
  'strategy_analysis': {
    id: 'strategy_analysis',
    label: '📊 Strategy Analysis',
    activationPatterns: [
      /\banalyze\s+(this|a|my|the)\s+strategy\b/i,
      /\bstrategy (evaluation|analysis)\b/i,
      /\bevaluate\s+(a|this|my)?\s*(decision|strategy)\b/i,
      /phân tích chiến lược/i,
      /đánh giá chiến lược/i,
      /đánh giá\s+(cơ hội|thách thức|cơ hội và thách thức)/i,
      /\banalyze a decision\b/i,
    ],
    wizardWinsWhen: 'user says "help me build a business strategy" (business-strategy wizard wins)',
  },
  'meeting_notes': {
    id: 'meeting_notes',
    label: '📝 Meeting Notes',
    activationPatterns: [
      /\bmeeting notes?\b/i,
      /\bminutes? of (the )?meeting\b/i,
      /\btake (the )?minutes\b/i,
      /\bsummarize (the )?meeting\b/i,
      /biên bản họp/i,
      /ghi chú họp/i,
      /kết quả buổi họp/i,
      /tóm tắt cuộc họp/i,
    ],
    wizardWinsWhen: 'user asks for a full project plan or workshop design (wizard wins)',
  },
  'job_description': {
    id: 'job_description',
    label: '💼 Job Description',
    activationPatterns: [
      /\bjob description\b/i,
      /\bjob posting\b/i,
      /\bwrite (a )?JD\b/i,
      /\brecruit(ing)? for\b/i,
      /\bhiring (a |an )?\w/i,
      /mô tả công việc/i,
      /tuyển dụng/i,
      /đăng tuyển/i,
      /viết JD/i,
    ],
    wizardWinsWhen: 'user asks for a full HR strategy or org design (wizard wins)',
  },
  'performance_review': {
    id: 'performance_review',
    label: '⭐ Performance Review',
    activationPatterns: [
      /\bperformance review\b/i,
      /\bperformance evaluation\b/i,
      /\bstaff review\b/i,
      /\bemployee assessment\b/i,
      /đánh giá hiệu suất/i,
      /đánh giá nhân viên/i,
      /nhận xét nhân viên/i,
      /đánh giá kết quả công việc/i,
    ],
    wizardWinsWhen: 'user asks for full people management or 360 feedback design (wizard wins)',
  },
  'seo_audit': {
    id: 'seo_audit',
    label: '🔎 SEO Audit',
    activationPatterns: [
      /\bseo audit\b/i,
      /\baudit\s+(my\s+)?seo\b/i,
      /\bcheck\s+(my\s+)?seo\b/i,
      /\bseo (check|review|analysis)\b/i,
      /\bwebsite seo\b/i,
      /kiểm tra seo/i,
      /audit seo/i,
      /phân tích seo/i,
      /tối ưu seo/i,
    ],
    wizardWinsWhen: 'user asks for full marketing strategy or content strategy broadly (wizard wins)',
  },
  'data_analysis': {
    id: 'data_analysis',
    label: '📈 Data Analysis',
    activationPatterns: [
      /\bdata analysis\b/i,
      /\banalyze\b.{0,25}\b(data|dataset|report|metrics|numbers)\b/i,
      /\binsights? from\b.{0,20}\b(data|report)\b/i,
      /\banalyze (my |this )?(analytics|dashboard|spreadsheet)\b/i,
      /phân tích dữ liệu/i,
      /phân tích (số liệu|báo cáo|kết quả)/i,
      /đọc dữ liệu/i,
      /giải thích (số liệu|dữ liệu|kết quả)/i,
    ],
    wizardWinsWhen: 'user asks for a full research project design or scientific methodology (research wizard wins)',
  },
  'brand_voice': {
    id: 'brand_voice',
    label: '🎙️ Brand Voice',
    activationPatterns: [
      /\bbrand voice\b/i,
      /\bbrand tone\b/i,
      /\btone of voice\b/i,
      /\bvoice (and|&) tone\b/i,
      /\bbrand style guide\b/i,
      /\bbrand consistency\b/i,
      /giọng điệu thương hiệu/i,
      /phong cách viết.*thương hiệu/i,
      /đồng bộ giọng điệu/i,
    ],
    wizardWinsWhen: 'user says "build my brand" or "brand strategy" broadly (branding wizard wins)',
  },
  'landing_page_cro': {
    id: 'landing_page_cro',
    label: '🎯 Landing Page CRO',
    activationPatterns: [
      /\blanding page\s+(cro|optimization|optimiz|review|audit)\b/i,
      /\boptimiz\w+\s+(my\s+|the\s+)?landing page\b/i,
      /\bconversion rate optimization\b/i,
      /\bcro\s+(for|of|analysis|audit)\b/i,
      /\bimprove\s+(my\s+|the\s+)?(landing page|conversion rate)\b/i,
      /tối ưu landing page/i,
      /tăng conversion rate/i,
      /tối ưu tỷ lệ chuyển đổi/i,
    ],
    wizardWinsWhen: 'user says "build a landing page" or "design my landing page" (product wizard wins)',
  },
  'email_campaign': {
    id: 'email_campaign',
    label: '📨 Email Campaign',
    activationPatterns: [
      /\breview\s+(my\s+)?(email|newsletter)\s+campaign\b/i,
      /\bemail (campaign|newsletter)\s+(review|evaluation|check|audit)\b/i,
      /\bemail marketing\s+(review|audit|analysis|check)\b/i,
      /\bcheck\s+(my\s+)?email\s+(campaign|newsletter|marketing)\b/i,
      /đánh giá email campaign/i,
      /kiểm tra email marketing/i,
      /review chiến dịch email/i,
    ],
    wizardWinsWhen: 'user asks to write or compose a new email (email_template form wins instead)',
  },
  'copywriting_evaluation': {
    id: 'copywriting_evaluation',
    label: '✏️ Copywriting Evaluation',
    activationPatterns: [
      /\bcopywriting (evaluation|review|audit|check|analysis)\b/i,
      /\bevaluate\s+(my\s+)?(copy|copywriting|headline|ad copy)\b/i,
      /\breview\s+(my\s+)?(marketing copy|ad copy|copywriting)\b/i,
      /\brate\s+(my\s+)?(copy|headline|ad)\b/i,
      /\bcheck\s+(my\s+)?(copy|headline|marketing copy)\b/i,
      /đánh giá copywriting/i,
      /kiểm tra marketing copy/i,
      /đánh giá nội dung quảng cáo/i,
    ],
    wizardWinsWhen: 'user asks for full content strategy or content planning (content-strategy wizard wins)',
  },
  'onboarding_review': {
    id: 'onboarding_review',
    label: '🎓 Onboarding Review',
    activationPatterns: [
      /\breview\s+(my\s+|the\s+|user\s+)?onboarding\b/i,
      /\bonboarding (review|audit|analysis|flow analysis)\b/i,
      /\bimprove\s+(my\s+|the\s+|user\s+)?onboarding\b/i,
      /\boptimiz\w+\s+(my\s+|the\s+)?onboarding\b/i,
      /review onboarding/i,
      /đánh giá onboarding/i,
      /tối ưu onboarding/i,
      /cải thiện trải nghiệm người dùng mới/i,
    ],
    wizardWinsWhen: 'user says "design my onboarding" or "build user onboarding from scratch" (product wizard wins)',
  },
  'accessibility_audit': {
    id: 'accessibility_audit',
    label: '♿ Accessibility Audit',
    activationPatterns: [
      /\baccessibility audit\b/i,
      /\baudit\s+(my\s+|the\s+|page\s+)?accessibility\b/i,
      /\bWCAG\s+(compliance|check|audit|review)\b/i,
      /\bcheck\s+(my\s+|the\s+)?accessibility\b/i,
      /\baccessibility (check|review|compliance|testing)\b/i,
      /kiểm tra accessibility/i,
      /audit accessibility/i,
      /kiểm tra khả năng tiếp cận/i,
    ],
    wizardWinsWhen: 'user says "design an accessible app" broadly (product wizard wins); security assessment wizard wins for broad compliance',
  },
  'api_security': {
    id: 'api_security',
    label: '🔒 API Security',
    activationPatterns: [
      /\bAPI security\b/i,
      /\bsecure\s+(my\s+|the\s+|our\s+)?API\b/i,
      /\bAPI security (review|audit|checklist|check|assessment)\b/i,
      /\bsecurity (review|audit|check)\s+(of|for)\s+(my\s+|the\s+)?API\b/i,
      /bảo mật API/i,
      /kiểm tra bảo mật API/i,
      /review bảo mật API/i,
    ],
    wizardWinsWhen: 'user says "security assessment" broadly without API-specific focus (security-assessment wizard wins)',
  },
  'gdpr_compliance': {
    id: 'gdpr_compliance',
    label: '🇪🇺 GDPR Compliance',
    activationPatterns: [
      /\bGDPR\s+(compliance|check|audit|review|assessment)\b/i,
      /\b(check|review|audit|comply\s+with)\s+GDPR\b/i,
      /\bGDPR\s+(ready|compliant)\b/i,
      /kiểm tra tuân thủ GDPR/i,
      /tuân thủ GDPR/i,
      /GDPR compliance/i,
    ],
    wizardWinsWhen: 'user asks for full data protection strategy or privacy program design broadly (security-assessment wizard wins)',
  },
  'privacy_policy_audit': {
    id: 'privacy_policy_audit',
    label: '🔏 Privacy Policy Audit',
    activationPatterns: [
      /\bprivacy policy\s+(audit|review|check|analysis)\b/i,
      /\b(audit|review|check)\s+(my\s+|the\s+)?privacy policy\b/i,
      /\bprivacy policy\b.{0,20}\b(compliant|coverage|gaps)\b/i,
      /kiểm tra chính sách bảo mật/i,
      /audit chính sách quyền riêng tư/i,
      /review chính sách bảo mật/i,
    ],
    wizardWinsWhen: 'user asks for full privacy program design (security-assessment wizard wins)',
  },
  'incident_response': {
    id: 'incident_response',
    label: '🚨 Incident Response',
    activationPatterns: [
      /\bincident response\b/i,
      /\bIR plan\b/i,
      /\bsecurity incident\s+(plan|response|playbook)\b/i,
      /\bdata breach\s+(response|plan|playbook)\b/i,
      /\bcreate\s+(an?\s+)?incident response plan\b/i,
      /ứng phó sự cố/i,
      /kế hoạch ứng phó bảo mật/i,
      /phản ứng sự cố bảo mật/i,
    ],
    wizardWinsWhen: 'user says "security strategy" or "full security program" (security-assessment wizard wins)',
  },
  'data_handling': {
    id: 'data_handling',
    label: '🗃️ Data Handling',
    activationPatterns: [
      /\bdata handling\s+(review|audit|policy|check)\b/i,
      /\bdata lifecycle\b/i,
      /\bdata governance\s+(review|audit|check|policy)\b/i,
      /\breview\s+(my\s+|our\s+)?data handling\b/i,
      /\bdata retention\s+(policy|review|audit)\b/i,
      /xử lý dữ liệu.{0,10}(review|kiểm tra)/i,
      /review cách xử lý dữ liệu/i,
      /quản trị dữ liệu/i,
    ],
    wizardWinsWhen: 'user asks for full data privacy program or GDPR implementation (gdpr_compliance form or security wizard wins)',
  },
  'tos_review': {
    id: 'tos_review',
    label: '📃 ToS Review',
    activationPatterns: [
      /\bterms of service\s+(review|audit|check|analysis)\b/i,
      /\bToS\s+(review|audit|check|analysis)\b/i,
      /\b(review|audit|check)\s+(my\s+|the\s+)?terms (of service|and conditions)\b/i,
      /\bterms (and conditions|of use)\s+(review|audit|check)\b/i,
      /review điều khoản dịch vụ/i,
      /kiểm tra điều khoản sử dụng/i,
      /đánh giá điều khoản dịch vụ/i,
    ],
    wizardWinsWhen: 'user asks for legal contract review broadly (outside security domain)',
  },
  'content_quality': {
    id: 'content_quality',
    label: '✅ Content Quality',
    activationPatterns: [
      /\bcontent quality\s+(check|audit|review|analysis)\b/i,
      /\b(check|audit|review)\s+(my\s+|the\s+)?content quality\b/i,
      /\bcontent (evaluation|assessment|scoring)\b/i,
      /kiểm tra chất lượng nội dung/i,
      /đánh giá chất lượng nội dung/i,
      /kiểm tra chất lượng bài viết/i,
    ],
    wizardWinsWhen: 'user asks for full content strategy or content planning (content-strategy wizard wins)',
  },
  'social_ad_review': {
    id: 'social_ad_review',
    label: '📱 Social Ad Review',
    activationPatterns: [
      /\bsocial (media\s+)?ad\s+(review|audit|check|evaluation)\b/i,
      /\b(Facebook|Instagram|TikTok|LinkedIn|YouTube)\s+ad\s+(review|audit|check|evaluation)\b/i,
      /\breview\s+(my\s+)?(social|Facebook|Instagram|TikTok|LinkedIn)\s+ad\b/i,
      /review quảng cáo (mạng xã hội|MXH|Facebook|TikTok)/i,
      /đánh giá quảng cáo (mạng xã hội|MXH|Facebook)/i,
      /kiểm tra quảng cáo (MXH|mạng xã hội)/i,
    ],
    wizardWinsWhen: 'user asks for full marketing campaign strategy (marketing-campaign wizard wins)',
  },
  'user_flow_analysis': {
    id: 'user_flow_analysis',
    label: '🔄 User Flow Analysis',
    activationPatterns: [
      /\buser flow\s+(analysis|review|audit|optimization)\b/i,
      /\banalyze\s+(my\s+|the\s+)?user (flow|journey)\b/i,
      /\buser journey\s+(analysis|review|mapping|audit)\b/i,
      /phân tích user flow/i,
      /phân tích hành trình người dùng/i,
      /tối ưu user flow/i,
    ],
    wizardWinsWhen: 'user asks to design a new user flow from scratch (product-design wizard wins)',
  },
  'ux_heuristic_evaluation': {
    id: 'ux_heuristic_evaluation',
    label: '📋 UX Heuristic Evaluation',
    activationPatterns: [
      /\bUX heuristic\b/i,
      /\bheuristic evaluation\b/i,
      /\bNielsen.{0,20}heuristic\b/i,
      /\bevaluate\s+(my\s+|the\s+)?UX\s+(using|with|against)?\s*heuristic/i,
      /đánh giá UX heuristic/i,
      /kiểm tra heuristic/i,
      /heuristic evaluation/i,
    ],
    wizardWinsWhen: 'user asks to design a new UX system (product-design wizard wins)',
  },
  'error_handling_ux': {
    id: 'error_handling_ux',
    label: '🛑 Error Handling UX',
    activationPatterns: [
      /\berror (handling|messages?)\s+(UX|review|audit|check|improvement)\b/i,
      /\b(review|improve|rewrite)\s+(my\s+|the\s+)?error messages?\b/i,
      /\bUX\s+(of|for)\s+(my\s+|the\s+)?error\b/i,
      /cải thiện thông báo lỗi/i,
      /review error messages/i,
      /viết lại thông báo lỗi/i,
    ],
    wizardWinsWhen: 'user asks for full UX redesign (product-design wizard wins)',
  },
  'code_review': {
    id: 'code_review',
    label: '💻 Code Review',
    activationPatterns: [
      /\bcode review\b/i,
      /\breview\s+(my\s+|this\s+|the\s+)?code\b/i,
      /\bcode (quality|evaluation|audit|check)\b/i,
      /\bcheck\s+(my\s+|this\s+)?code\b/i,
      /review code/i,
      /kiểm tra chất lượng code/i,
      /đánh giá code/i,
    ],
    wizardWinsWhen: 'user asks to build or generate code (app-builder wizard wins)',
  },
  'architecture_review': {
    id: 'architecture_review',
    label: '🏗️ Architecture Review',
    activationPatterns: [
      /\barchitecture review\b/i,
      /\breview\s+(my\s+|the\s+|our\s+)?architecture\b/i,
      /\bsystem architecture\s+(review|audit|check|analysis)\b/i,
      /\barchitecture (audit|analysis|check|evaluation)\b/i,
      /review kiến trúc/i,
      /đánh giá kiến trúc hệ thống/i,
      /kiểm tra thiết kế kiến trúc/i,
    ],
    wizardWinsWhen: 'user asks to design a new architecture (architecture-design form wins) or build a system (system-design wizard wins)',
  },
  'app_requirements_spec': {
    id: 'app_requirements_spec',
    label: '📝 App Requirements Spec',
    activationPatterns: [
      /\bapp requirements?\s+(spec|document|template|write)\b/i,
      /\bwrite\s+(my\s+)?(app|application) requirements?\b/i,
      /\bspec\s+(for\s+)?(my\s+|an?\s+)?(app|application)\b/i,
      /\bfunctional requirements?\s+(doc|document|template|spec)\b/i,
      /\brequirements?\s+(specification|document|spec)\s+(for|of)\b/i,
      /viết spec yêu cầu ứng dụng/i,
      /tài liệu yêu cầu ứng dụng/i,
      /viết yêu cầu phần mềm/i,
    ],
    wizardWinsWhen: 'user says "build my app" or "create my app" (app-builder wizard wins)',
  },
};

/**
 * Attempt to match a plain-language input to a trusted form target.
 *
 * Returns the first matching TrustedFormMatch, or null if no trusted form
 * matches. The intent router calls this before wizard routing because form
 * patterns are narrower than wizard-family keywords.
 */
export function routeToTrustedForm(userInput: string): TrustedFormMatch | null {
  for (const [key, entry] of Object.entries(TRUSTED_FORM_MAP)) {
    for (const pattern of entry.activationPatterns) {
      if (pattern.test(userInput)) {
        return { formKey: key, id: entry.id, label: entry.label };
      }
    }
  }
  return null;
}

/**
 * Returns true when the trusted form front door flag is enabled.
 * W126 uses the same INTENT_FIRST flag — form routing is part of the same surface.
 */
export function isTrustedFormRoutingEnabled(): boolean {
  return process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR === 'true';
}
