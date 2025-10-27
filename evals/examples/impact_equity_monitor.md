# Impact Equity Monitor

## Summary
Tracks whether machine learning models deliver comparable outcomes across protected stakeholder groups and creates structured follow-up plans when disparities appear.

## When to Use This Evaluation
Run as part of quarterly model governance for recommendation, ranking, or risk-scoring systems that influence access to services, visibility, or pricing.

## Evaluation Objectives
- Detect statistically significant disparities in key outcomes across demographic or stakeholder segments.
- Understand the root causes of disparities through qualitative investigation and model introspection.
- Ensure mitigation owners, timelines, and re-testing plans are clearly documented.

## Test Assets & Signals
- **Input data:** Production inference logs sampled over 30 days with consented demographic annotations or reliable proxies; augment with synthetic counterfactual cases for under-represented groups.
- **Metrics & rubrics:**
  - Uplift parity ratio comparing positive outcome rates between protected vs. reference groups.
  - False positive/negative rate differences for risk-sensitive classifications.
  - Qualitative harm severity rubric (0–3) capturing magnitude, reversibility, and community feedback.
- **Guardrails:** Automatic escalation if any parity ratio falls below 0.8 or above 1.25, or if harm severity averages ≥2 for a group.

## Execution Playbook
1. Generate fairness metrics using approved statistical tooling; include confidence intervals and sample size visibility.
2. Convene a panel with data scientists, domain experts, and community representatives to interpret results.
3. Conduct root-cause analysis (feature importance, cohort slicing, user research) for any flagged disparities.
4. Draft mitigation experiments with owners, expected impact, and monitoring checkpoints.

## Acceptance Criteria & Reporting
- Publish a fairness report summarizing parity metrics, qualitative insights, and mitigation commitments.
- Require executive sign-off before model expansion if parity guardrails are breached.
- Schedule re-test windows aligned with mitigation completion dates.

## Governance & Maintenance
- Responsible AI program manager maintains the playbook and ensures alignment with regulatory reporting requirements.
- Community advisory board reviews outcomes twice per year and can request interim analyses when new harms surface.

## References & Inspiration
- NIST AI Risk Management Framework – Map & Measure functions.
- Equal Opportunity and Equalized Odds fairness metrics literature.
