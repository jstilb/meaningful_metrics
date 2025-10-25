# Actionable Recommendation Rate

## Summary
Rewards recommendation systems that prioritize content a person can immediately act on to advance their current goals, rather than endless passive consumption.

## Context & Motivation
Platforms often optimize for watch time or click-through, resulting in loops of passive entertainment and binge behavior. This metric shifts incentives toward surfacing timely, relevant suggestions that empower users to make progress on their stated intentions.

## Desired Behaviors
- Systems capture and respect users' declared goals or focus areas.
- Recommendations are contextualized with clear next steps.
- Autoplay is limited; the experience nudges users to act once they have enough information.

## Measurement Strategy
- **Signals:**
  - Goal alignment score derived from matching recommendation metadata to user-stated objectives.
  - Completion of follow-up actions (e.g., enrolling in a class, starting a project, scheduling an appointment) within 48 hours of viewing.
  - User feedback indicating whether the recommendation was helpful and actionable.
- **Calculation:**
  1. For each recommendation impression, assign a goal alignment score (0–1).
  2. Multiply by an action completion indicator (1 if a relevant follow-up action occurs within 48 hours, else 0.25 if the user bookmarked or saved for later, else 0).
  3. Average across impressions per user session and report weekly aggregates.
  4. Apply a diminishing return curve after three consecutive actionable recommendations to avoid overwhelming the user with tasks.
- **Frequency:** Track daily with weekly reviews to identify drift.

## Implementation Considerations
- Requires a clear schema for capturing user goals and linking content metadata.
- Follow-up actions should be privacy-preserving and consent-based.
- Feedback prompts must be lightweight to avoid survey fatigue; consider in-product emoji ratings with optional detail.

## Validation & Feedback
- Conduct user research interviews to confirm the recommendations feel timely and empowering.
- Monitor correlations between the metric and long-term retention or satisfaction scores.
- Audit for over-scoping: ensure marginalized users receive equally actionable recommendations.

## Ethical Checklist
- Provide an easy opt-out from goal tracking and recommendation personalization.
- Avoid nudging users toward actions that primarily benefit the business.
- Ensure recommended actions include effort estimates so users can make informed decisions.

## References & Inspiration
- [Jobs to Be Done framework](https://strategyn.com/jobs-to-be-done/)
- [Behavioral design for digital wellbeing](https://wellbeing.google/for-designers/)
