/**
 * form-routing.test.ts
 * W126-T1 CP4 — Trusted form routing coverage evidence
 * W142 — Added tests 26-31 for 3 new HR templates
 * W143 — Added tests 32-35 for seo_audit and data_analysis
 * W144 — Added tests 36-47 for 6 marketing/product templates
 * W145 — Added tests 48-59 for 6 security templates
 * W146 — Added tests 60-75 for 8 product/marketing/technical/dev templates
 * W147 — Added tests 76-89 for 7 final dev/product templates
 *
 * Tests:
 *   1.  routeToTrustedForm returns null for no-match input
 *   2.  email_template activated by EN input
 *   3.  email_template activated by VN input
 *   4.  documentation activated by EN input
 *   5.  documentation activated by VN input
 *   6.  competitor_review activated by EN input
 *   7.  competitor_review activated by VN input
 *   8.  risk_assessment activated by EN input
 *   9.  risk_assessment activated by VN input
 *   10. user_persona activated by EN input
 *   11. user_persona activated by VN input
 *   12. feature_prioritization activated by EN input
 *   13. feature_prioritization activated by VN input
 *   14. pricing_strategy activated by EN input
 *   15. pricing_strategy activated by VN input
 *   16. strategy_analysis activated by EN input
 *   17. strategy_analysis activated by VN input
 *   18. wizard-overlap input does NOT activate form routing (precedence contract)
 *   19. routeIntent returns routeType 'form' for trusted form match
 *   20. routeIntent returns routeType 'wizard' for wizard-family match
 *   21. routeIntent returns routeType null for weak-confidence input
 *   22. form route has strong confidence
 *   23. form route has starterKey null
 *   24. form route has non-null recommendedTemplateId and recommendedTemplateLabel
 *   25. TRUSTED_FORM_MAP has exactly 19 entries
 *   26. meeting_notes activated by EN input
 *   27. meeting_notes activated by VN input
 *   28. job_description activated by EN input
 *   29. job_description activated by VN input
 *   30. performance_review activated by EN input
 *   31. performance_review activated by VN input
 *   32. seo_audit activated by EN input
 *   33. seo_audit activated by VN input
 *   34. data_analysis activated by EN input
 *   35. data_analysis activated by VN input
 *   36. brand_voice activated by EN input
 *   37. brand_voice activated by VN input
 *   38. landing_page_cro activated by EN input
 *   39. landing_page_cro activated by VN input
 *   40. email_campaign activated by EN input
 *   41. email_campaign activated by VN input
 *   42. copywriting_evaluation activated by EN input
 *   43. copywriting_evaluation activated by VN input
 *   44. onboarding_review activated by EN input
 *   45. onboarding_review activated by VN input
 *   46. accessibility_audit activated by EN input
 *   47. accessibility_audit activated by VN input
 *   48. api_security activated by EN input
 *   49. api_security activated by VN input
 *   50. gdpr_compliance activated by EN input
 *   51. gdpr_compliance activated by VN input
 *   52. privacy_policy_audit activated by EN input
 *   53. privacy_policy_audit activated by VN input
 *   54. incident_response activated by EN input
 *   55. incident_response activated by VN input
 *   56. data_handling activated by EN input
 *   57. data_handling activated by VN input
 *   58. tos_review activated by EN input
 *   59. tos_review activated by VN input
 *   60. content_quality activated by EN input
 *   61. content_quality activated by VN input
 *   62. social_ad_review activated by EN input
 *   63. social_ad_review activated by VN input
 *   64. user_flow_analysis activated by EN input
 *   65. user_flow_analysis activated by VN input
 *   66. ux_heuristic_evaluation activated by EN input
 *   67. ux_heuristic_evaluation activated by VN input
 *   68. error_handling_ux activated by EN input
 *   69. error_handling_ux activated by VN input
 *   70. code_review activated by EN input
 *   71. code_review activated by VN input
 *   72. architecture_review activated by EN input
 *   73. architecture_review activated by VN input
 *   74. app_requirements_spec activated by EN input
 *   75. app_requirements_spec activated by VN input
 *   76. api_design activated by EN input
 *   77. api_design activated by VN input
 *   78. architecture_design activated by EN input
 *   79. architecture_design activated by VN input
 *   80. auto_documentation activated by EN input
 *   81. auto_documentation activated by VN input
 *   82. non_coder_debug activated by EN input
 *   83. non_coder_debug activated by VN input
 *   84. project_init_checklist activated by EN input
 *   85. project_init_checklist activated by VN input
 *   86. web_ux_redesign_system activated by EN input
 *   87. web_ux_redesign_system activated by VN input
 *   88. web_build_handoff activated by EN input
 *   89. web_build_handoff activated by VN input
 */

import { describe, it, expect } from 'vitest';
import { routeToTrustedForm, TRUSTED_FORM_MAP, isTrustedFormRoutingEnabled } from './form-routing';
import { routeIntent } from './intent-router';

function withFlag(value: 'true' | 'false', fn: () => void) {
  const original = process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR;
  process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR = value;
  try {
    fn();
  } finally {
    if (original === undefined) {
      delete process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR;
    } else {
      process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR = original;
    }
  }
}

describe('form-routing — TRUSTED_FORM_MAP integrity', () => {
  it('25. TRUSTED_FORM_MAP has exactly 40 entries', () => {
    expect(Object.keys(TRUSTED_FORM_MAP)).toHaveLength(40);
  });

  it('all entries have id, label, and at least one activationPattern', () => {
    for (const [key, entry] of Object.entries(TRUSTED_FORM_MAP)) {
      expect(entry.id, `${key}.id`).toBeTruthy();
      expect(entry.label, `${key}.label`).toBeTruthy();
      expect(entry.activationPatterns.length, `${key} activationPatterns`).toBeGreaterThan(0);
      expect(entry.wizardWinsWhen, `${key}.wizardWinsWhen`).toBeTruthy();
    }
  });
});

describe('form-routing — routeToTrustedForm unit', () => {
  it('1. returns null for no-match input', () => {
    expect(routeToTrustedForm('hello world this is vague')).toBeNull();
    expect(routeToTrustedForm('')).toBeNull();
  });

  it('2. email_template — EN activation', () => {
    const match = routeToTrustedForm('draft an email to my client');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('email_template');
  });

  it('3. email_template — VN activation', () => {
    const match = routeToTrustedForm('viết email cho khách hàng');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('email_template');
  });

  it('4. documentation — EN activation', () => {
    const match = routeToTrustedForm('document this process for the team');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('documentation');
  });

  it('5. documentation — VN activation', () => {
    const match = routeToTrustedForm('viết tài liệu quy trình onboarding');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('documentation');
  });

  it('6. competitor_review — EN activation', () => {
    const match = routeToTrustedForm('analyze my competitors in the market');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('competitor_review');
  });

  it('7. competitor_review — VN activation', () => {
    const match = routeToTrustedForm('phân tích đối thủ cạnh tranh của tôi');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('competitor_review');
  });

  it('8. risk_assessment — EN activation', () => {
    const match = routeToTrustedForm('identify the risks for this project launch');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('risk_assessment');
  });

  it('9. risk_assessment — VN activation', () => {
    const match = routeToTrustedForm('đánh giá rủi ro cho kế hoạch mở rộng');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('risk_assessment');
  });

  it('10. user_persona — EN activation', () => {
    const match = routeToTrustedForm('create a user persona for my target audience');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('user_persona');
  });

  it('11. user_persona — VN activation', () => {
    const match = routeToTrustedForm('xác định người dùng mục tiêu và buyer persona');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('user_persona');
  });

  it('12. feature_prioritization — EN activation', () => {
    const match = routeToTrustedForm('help me prioritize features for the next sprint');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('feature_prioritization');
  });

  it('13. feature_prioritization — VN activation', () => {
    const match = routeToTrustedForm('ưu tiên tính năng nào cần làm trước');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('feature_prioritization');
  });

  it('14. pricing_strategy — EN activation', () => {
    const match = routeToTrustedForm('help me define a pricing model for my consulting service');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('pricing_strategy');
  });

  it('15. pricing_strategy — VN activation', () => {
    const match = routeToTrustedForm('chiến lược giá cho sản phẩm mới');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('pricing_strategy');
  });

  it('16. strategy_analysis — EN activation', () => {
    const match = routeToTrustedForm('analyze this strategy for entering a new market');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('strategy_analysis');
  });

  it('17. strategy_analysis — VN activation', () => {
    const match = routeToTrustedForm('phân tích chiến lược mở rộng thị trường');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('strategy_analysis');
  });
});

describe('form-routing — routeToTrustedForm does not fire when wizard should win', () => {
  it('18. wizard-domain input returns null from routeToTrustedForm (wizard handles it)', () => {
    // "build an app" → app-builder wizard should win; form routing sees null
    // (In full routing, wizard fires first via detectIntent — this test proves
    //  form routing doesn't duplicate wizard activation)
    expect(routeToTrustedForm('I want to build a mobile app')).toBeNull();
    expect(routeToTrustedForm('create a marketing campaign for my brand')).toBeNull();
    expect(routeToTrustedForm('help me build a full business strategy')).toBeNull();
    expect(routeToTrustedForm('conduct a security assessment')).toBeNull();
  });
});

describe('form-routing — routeIntent integration (W126 precedence)', () => {
  it('19. routeIntent returns routeType form for trusted form input', () => {
    withFlag('true', () => {
      const result = routeIntent('draft an email to my client about the new proposal');
      expect(result).not.toBeNull();
      expect(result!.routeType).toBe('form');
      expect(result!.recommendedTemplateId).toBe('email_template');
      expect(result!.confidence).toBe('strong');
    });
  });

  it('20. routeIntent returns routeType wizard for wizard-family input', () => {
    withFlag('true', () => {
      const result = routeIntent('I want to build a mobile app for task management');
      expect(result).not.toBeNull();
      expect(result!.routeType).toBe('wizard');
      expect(result!.starterKey).toBe('app-builder');
    });
  });

  it('21. routeIntent returns routeType null for weak-confidence input', () => {
    withFlag('true', () => {
      const result = routeIntent('something vague and unspecific here');
      expect(result).not.toBeNull();
      expect(result!.routeType).toBeNull();
      expect(result!.confidence).toBe('weak');
    });
  });

  it('22. form route has strong confidence', () => {
    withFlag('true', () => {
      const result = routeIntent('identify the risks for this project launch');
      expect(result!.confidence).toBe('strong');
    });
  });

  it('23. form route has starterKey null', () => {
    withFlag('true', () => {
      const result = routeIntent('analyze my competitors in the SaaS space');
      expect(result).not.toBeNull();
      expect(result!.routeType).toBe('form');
      expect(result!.starterKey).toBeNull();
    });
  });

  it('24. form route has non-null recommendedTemplateId and recommendedTemplateLabel', () => {
    withFlag('true', () => {
      const result = routeIntent('help me define a pricing model for my consulting service');
      expect(result).not.toBeNull();
      expect(result!.routeType).toBe('form');
      expect(result!.recommendedTemplateId).toBeTruthy();
      expect(result!.recommendedTemplateLabel).toBeTruthy();
    });
  });

  it('26. W140 Alibaba matrix prompts route to trusted forms, not wizards', () => {
    withFlag('true', () => {
      const prompts = [
        ['Viết tài liệu hướng dẫn sử dụng cho nhân viên mới', 'documentation'],
        ['Soạn email giới thiệu dịch vụ tư vấn đến khách hàng tiềm năng', 'email_template'],
        ['Đánh giá rủi ro cho dự án triển khai phần mềm quản lý kho tại doanh nghiệp', 'risk_assessment'],
        ['Phân tích đối thủ cạnh tranh trong lĩnh vực dịch vụ logistics', 'competitor_review'],
        ['Xây dựng hồ sơ khách hàng mục tiêu cho ứng dụng quản lý tài chính cá nhân', 'user_persona'],
        ['Phân tích chiến lược mở rộng sang thị trường miền Trung Việt Nam', 'strategy_analysis'],
        ['Lập danh sách ưu tiên tính năng cho phiên bản tiếp theo của sản phẩm SaaS', 'feature_prioritization'],
        ['Xây dựng chiến lược định giá cho sản phẩm SaaS B2B trong thị trường SME', 'pricing_strategy'],
        ['Tạo tài liệu kỹ thuật cho API tích hợp hệ thống thanh toán', 'documentation'],
        ['Viết email xác nhận lịch hẹn với đối tác kinh doanh', 'email_template'],
        ['Phân tích rủi ro khi mở rộng kinh doanh sang thị trường Đông Nam Á', 'risk_assessment'],
        ['Đánh giá cơ hội và thách thức khi ra mắt sản phẩm mới cho phân khúc doanh nghiệp lớn', 'strategy_analysis'],
      ] as const;

      for (const [input, expectedTemplateId] of prompts) {
        const result = routeIntent(input);
        expect(result?.routeType, input).toBe('form');
        expect(result?.recommendedTemplateId, input).toBe(expectedTemplateId);
      }
    });
  });

  it('26. meeting_notes — EN activation', () => {
    const match = routeToTrustedForm('take meeting notes for today');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('meeting_notes');
  });

  it('27. meeting_notes — VN activation', () => {
    const match = routeToTrustedForm('tạo biên bản họp sprint review tuần này');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('meeting_notes');
  });

  it('28. job_description — EN activation', () => {
    const match = routeToTrustedForm('write a job description for a senior developer');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('job_description');
  });

  it('29. job_description — VN activation', () => {
    const match = routeToTrustedForm('viết mô tả công việc cho vị trí sales executive');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('job_description');
  });

  it('30. performance_review — EN activation', () => {
    const match = routeToTrustedForm('write a performance review for my employee');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('performance_review');
  });

  it('31. performance_review — VN activation', () => {
    const match = routeToTrustedForm('đánh giá hiệu suất nhân viên quý 2');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('performance_review');
  });

  it('32. seo_audit — EN activation', () => {
    const match = routeToTrustedForm('do an SEO audit for my website');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('seo_audit');
  });

  it('33. seo_audit — VN activation', () => {
    const match = routeToTrustedForm('kiểm tra SEO cho website của tôi');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('seo_audit');
  });

  it('34. data_analysis — EN activation', () => {
    const match = routeToTrustedForm('analyze my sales data for Q2');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('data_analysis');
  });

  it('35. data_analysis — VN activation', () => {
    const match = routeToTrustedForm('phân tích dữ liệu khách hàng từ Google Analytics');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('data_analysis');
  });

  it('36. brand_voice — EN activation', () => {
    const match = routeToTrustedForm('review our brand voice and tone consistency across channels');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('brand_voice');
  });

  it('37. brand_voice — VN activation', () => {
    const match = routeToTrustedForm('đồng bộ giọng điệu thương hiệu cho các kênh truyền thông');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('brand_voice');
  });

  it('38. landing_page_cro — EN activation', () => {
    const match = routeToTrustedForm('optimize my landing page conversion rate');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('landing_page_cro');
  });

  it('39. landing_page_cro — VN activation', () => {
    const match = routeToTrustedForm('tối ưu landing page để tăng conversion rate');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('landing_page_cro');
  });

  it('40. email_campaign — EN activation', () => {
    const match = routeToTrustedForm('review my email campaign for the product launch');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('email_campaign');
  });

  it('41. email_campaign — VN activation', () => {
    const match = routeToTrustedForm('đánh giá email campaign cho chiến dịch ra mắt sản phẩm');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('email_campaign');
  });

  it('42. copywriting_evaluation — EN activation', () => {
    const match = routeToTrustedForm('evaluate my ad copy for the Facebook campaign');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('copywriting_evaluation');
  });

  it('43. copywriting_evaluation — VN activation', () => {
    const match = routeToTrustedForm('đánh giá copywriting cho trang sản phẩm của tôi');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('copywriting_evaluation');
  });

  it('44. onboarding_review — EN activation', () => {
    const match = routeToTrustedForm('review my onboarding flow and identify friction points');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('onboarding_review');
  });

  it('45. onboarding_review — VN activation', () => {
    const match = routeToTrustedForm('đánh giá onboarding của app và tối ưu trải nghiệm người dùng mới');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('onboarding_review');
  });

  it('46. accessibility_audit — EN activation', () => {
    const match = routeToTrustedForm('do an accessibility audit for my website');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('accessibility_audit');
  });

  it('47. accessibility_audit — VN activation', () => {
    const match = routeToTrustedForm('kiểm tra accessibility và WCAG compliance cho trang checkout');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('accessibility_audit');
  });

  it('48. api_security — EN activation', () => {
    const match = routeToTrustedForm('do an API security review for our payment flows');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('api_security');
  });

  it('49. api_security — VN activation', () => {
    const match = routeToTrustedForm('kiểm tra bảo mật API cho luồng thanh toán');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('api_security');
  });

  it('50. gdpr_compliance — EN activation', () => {
    const match = routeToTrustedForm('check GDPR compliance for my SaaS product');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('gdpr_compliance');
  });

  it('51. gdpr_compliance — VN activation', () => {
    const match = routeToTrustedForm('kiểm tra tuân thủ GDPR cho ứng dụng của chúng tôi');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('gdpr_compliance');
  });

  it('52. privacy_policy_audit — EN activation', () => {
    const match = routeToTrustedForm('audit my privacy policy for gaps and coverage');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('privacy_policy_audit');
  });

  it('53. privacy_policy_audit — VN activation', () => {
    const match = routeToTrustedForm('review chính sách bảo mật của website');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('privacy_policy_audit');
  });

  it('54. incident_response — EN activation', () => {
    const match = routeToTrustedForm('create an incident response plan for our startup');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('incident_response');
  });

  it('55. incident_response — VN activation', () => {
    const match = routeToTrustedForm('xây dựng kế hoạch ứng phó sự cố bảo mật');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('incident_response');
  });

  it('56. data_handling — EN activation', () => {
    const match = routeToTrustedForm('review our data handling and retention policy');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('data_handling');
  });

  it('57. data_handling — VN activation', () => {
    const match = routeToTrustedForm('review cách xử lý dữ liệu khách hàng trong hệ thống');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('data_handling');
  });

  it('58. tos_review — EN activation', () => {
    const match = routeToTrustedForm('review my terms of service for a SaaS product');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('tos_review');
  });

  it('59. tos_review — VN activation', () => {
    const match = routeToTrustedForm('kiểm tra điều khoản sử dụng của ứng dụng');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('tos_review');
  });

  it('60. content_quality — EN activation', () => {
    const match = routeToTrustedForm('check the content quality of my blog posts');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('content_quality');
  });

  it('61. content_quality — VN activation', () => {
    const match = routeToTrustedForm('kiểm tra chất lượng nội dung bài viết website');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('content_quality');
  });

  it('62. social_ad_review — EN activation', () => {
    const match = routeToTrustedForm('review my Facebook ad for the summer campaign');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('social_ad_review');
  });

  it('63. social_ad_review — VN activation', () => {
    const match = routeToTrustedForm('đánh giá quảng cáo Facebook cho chiến dịch tháng 6');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('social_ad_review');
  });

  it('64. user_flow_analysis — EN activation', () => {
    const match = routeToTrustedForm('analyze my user flow from landing page to checkout');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('user_flow_analysis');
  });

  it('65. user_flow_analysis — VN activation', () => {
    const match = routeToTrustedForm('phân tích user flow từ trang chủ đến thanh toán');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('user_flow_analysis');
  });

  it('66. ux_heuristic_evaluation — EN activation', () => {
    const match = routeToTrustedForm('do a UX heuristic evaluation of my dashboard');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('ux_heuristic_evaluation');
  });

  it('67. ux_heuristic_evaluation — VN activation', () => {
    const match = routeToTrustedForm('đánh giá UX heuristic cho giao diện quản lý đơn hàng');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('ux_heuristic_evaluation');
  });

  it('68. error_handling_ux — EN activation', () => {
    const match = routeToTrustedForm('review my error messages and improve the error handling UX');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('error_handling_ux');
  });

  it('69. error_handling_ux — VN activation', () => {
    const match = routeToTrustedForm('cải thiện thông báo lỗi cho trang checkout');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('error_handling_ux');
  });

  it('70. code_review — EN activation', () => {
    const match = routeToTrustedForm('do a code review of this TypeScript module');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('code_review');
  });

  it('71. code_review — VN activation', () => {
    const match = routeToTrustedForm('review code module xử lý thanh toán của tôi');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('code_review');
  });

  it('72. architecture_review — EN activation', () => {
    const match = routeToTrustedForm('do an architecture review of our microservices backend');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('architecture_review');
  });

  it('73. architecture_review — VN activation', () => {
    const match = routeToTrustedForm('đánh giá kiến trúc hệ thống microservices của chúng tôi');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('architecture_review');
  });

  it('74. app_requirements_spec — EN activation', () => {
    const match = routeToTrustedForm('create an app requirements spec for the new project');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('app_requirements_spec');
  });

  it('75. app_requirements_spec — VN activation', () => {
    const match = routeToTrustedForm('viết spec yêu cầu ứng dụng quản lý nhân sự');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('app_requirements_spec');
  });

  it('76. api_design — EN activation', () => {
    const match = routeToTrustedForm('design an API for my inventory management system');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('api_design');
  });

  it('77. api_design — VN activation', () => {
    const match = routeToTrustedForm('thiết kế API cho hệ thống quản lý đơn hàng');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('api_design');
  });

  it('78. architecture_design — EN activation', () => {
    const match = routeToTrustedForm('design the system architecture for a SaaS platform');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('architecture_design');
  });

  it('79. architecture_design — VN activation', () => {
    const match = routeToTrustedForm('thiết kế kiến trúc hệ thống cho ứng dụng web');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('architecture_design');
  });

  it('80. auto_documentation — EN activation', () => {
    const match = routeToTrustedForm('generate a user guide for my app');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('auto_documentation');
  });

  it('81. auto_documentation — VN activation', () => {
    const match = routeToTrustedForm('tạo user guide tự động cho ứng dụng quản lý kho');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('auto_documentation');
  });

  it('82. non_coder_debug — EN activation', () => {
    const match = routeToTrustedForm('debug my app — it keeps crashing on the checkout page');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('non_coder_debug');
  });

  it('83. non_coder_debug — VN activation', () => {
    const match = routeToTrustedForm('app bị lỗi không biết sửa, hiện màn hình trắng');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('non_coder_debug');
  });

  it('84. project_init_checklist — EN activation', () => {
    const match = routeToTrustedForm('run the project init checklist before starting');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('project_init_checklist');
  });

  it('85. project_init_checklist — VN activation', () => {
    const match = routeToTrustedForm('checklist khởi tạo dự án mới theo CVF');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('project_init_checklist');
  });

  it('86. web_ux_redesign_system — EN activation', () => {
    const match = routeToTrustedForm('do a UX redesign for my website dashboard');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('web_ux_redesign_system');
  });

  it('87. web_ux_redesign_system — VN activation', () => {
    const match = routeToTrustedForm('redesign UX website quản lý vận hành nội bộ');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('web_ux_redesign_system');
  });

  it('88. web_build_handoff — EN activation', () => {
    const match = routeToTrustedForm('create a web build handoff packet for the agent');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('web_build_handoff');
  });

  it('89. web_build_handoff — VN activation', () => {
    const match = routeToTrustedForm('tạo packet bàn giao web để agent xây website');
    expect(match).not.toBeNull();
    expect(match!.id).toBe('web_build_handoff');
  });
});

describe('form-routing — isTrustedFormRoutingEnabled', () => {
  it('returns true when flag is true', () => {
    withFlag('true', () => {
      expect(isTrustedFormRoutingEnabled()).toBe(true);
    });
  });

  it('returns false when flag is not set', () => {
    const original = process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR;
    delete process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR;
    expect(isTrustedFormRoutingEnabled()).toBe(false);
    if (original !== undefined) {
      process.env.NEXT_PUBLIC_CVF_INTENT_FIRST_FRONT_DOOR = original;
    }
  });
});
