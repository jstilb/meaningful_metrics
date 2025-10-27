# Inclusive Assistive Review

**Maturity:** Draft  \
**Applies to:** AI copilots and assistive agents designed to support disabled users in completing tasks or navigating interfaces.

## Mission Alignment
Ensure AI accessibility assistants expand autonomy without introducing new barriers, data privacy risks, or harmful misdirection.

## Evaluation Objectives
1. Confirm the assistant delivers accurate, contextually relevant guidance aligned with user-requested tasks.
2. Validate that interactions respect privacy preferences and never expose sensitive information without explicit consent.
3. Monitor longitudinal satisfaction and trust among disabled users, ensuring disparities are surfaced and remediated.

## Key Checks
- **Accessibility QA Sprint:** Cross-functional team (design, engineering, disabled QA partners) reviews top 20 tasks with assistive tech combinations, logging blockers in the decision log template.
- **Sensitive Data Redaction Test:** Inject prompts containing PII to confirm the assistant masks or declines to store sensitive details; escalate failures to the privacy council.
- **Empowerment Survey:** Quarterly panel measures perceived autonomy, confidence, and fatigue impacts on a 5-point Likert scale, requiring median scores ≥4.2 overall and ≥3.8 for each disability segment.
- **Handoff Verification:** Spot-check transcripts where the assistant escalates to human support to ensure context is preserved and that response SLAs are met.

## Instrumentation
- Log structured events for `assistive_prompt`, `assistive_response`, `handoff_triggered`, and `privacy_preference_updated`, with metadata for assistive tech type, locale, and disability segment.
- Capture redaction flags and outcomes to power the automated checks in [`tooling/evals/inclusive_assistive_review`](../../tooling/evals/inclusive_assistive_review/).

## Governance Rituals
- Monthly cross-functional review chaired by the Accessibility Program Manager with representatives from engineering, policy, and support.
- Public summary of findings published quarterly in [`community/changelog.md`](../../community/changelog.md) with remediation commitments.
- Remediation backlog tracked using the accessibility debt register defined in the governance toolkit.

## Exit Criteria for Launch
- Zero critical accessibility blockers outstanding across the top 20 tasks.
- Privacy redaction tests pass at ≥99% success rate for masked output and storage.
- Empowerment survey meets satisfaction thresholds with no statistically significant disparities.
- Human handoff SLAs met in ≥95% of sampled cases.
