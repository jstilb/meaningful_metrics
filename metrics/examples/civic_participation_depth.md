# Civic Participation Depth

**Maturity:** Draft  \
**Domain:** Civic technology platforms that connect residents with local opportunities

## Intent
Measure whether civic engagement tools move residents beyond awareness toward concrete, repeatable participation in their communities. The metric rewards platforms that help people discover, commit to, and follow through on civic actions such as attending meetings, providing feedback, or volunteering.

## Signals
- Percentage of users who open an opportunity detail page and subsequently RSVP, provide feedback, or sign up for reminders.
- Completion rate for follow-up surveys that confirm the action occurred and capture qualitative reflections.
- Frequency of returning participation (e.g., users who take more than one action in a quarter).
- Guardrail events such as last-minute cancellations or reports of inaccessible opportunities.

## Incentives
- Encourages product teams to prioritize clear pathways from discovery to action rather than surface-level content views.
- Highlights the importance of accessibility and logistical support for civic events.
- Motivates partnerships with community organizations that can host inclusive opportunities and validate attendance.

## Guardrails
- Flag segments where cancellation or inaccessibility reports exceed 10% to trigger outreach with organizers.
- Require that at least 30% of actions have a verified completion survey response before declaring success.
- Monitor disparities in participation depth across neighborhoods, income brackets, and language preferences; initiate remediation plans when any gap exceeds 15 percentage points.

## Validation
- Conduct quarterly participant interviews to confirm that reported actions translated into meaningful outcomes.
- Run A/B tests on opportunity presentation flows to ensure improvements in the metric correspond with self-reported empowerment.
- Publish a civic equity dashboard using the assets in [`tooling/metrics/civic_participation_depth`](../../tooling/metrics/civic_participation_depth/) to monitor fairness slices and follow-up tasks.

## Implementation Notes
- Instrument event logs for `opportunity_viewed`, `action_committed`, `action_completed`, and `action_follow_up_submitted` with timestamp, neighborhood, and access needs metadata.
- Leverage the SQL queries and outreach checklist provided in the tooling package to create recurring reports for community partners.
