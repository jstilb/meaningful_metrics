# Actionable Recommendation Rate — Instrumentation Guide

## Required Events
| Event Name | Description | Key Properties |
|------------|-------------|----------------|
| `recommendation_rendered` | Recommendation module displayed to the user. | `user_id`, `recommendation_id`, `goal_context`, `rank_position` |
| `recommendation_saved` | User saves or bookmarks the recommendation for later action. | `action_type`, `goal_context`, `time_to_action_seconds` |
| `recommendation_completed` | User completes the recommended action (e.g., enrolls, purchases, RSVPs). | `conversion_value`, `effort_estimate`, `success_confidence` |
| `recommendation_feedback_submitted` | User provides qualitative feedback about usefulness. | `feedback_score`, `feedback_theme` |

## Reference Query

```sql
WITH impressions AS (
  SELECT
    recommendation_id,
    user_id,
    goal_context,
    MIN(event_timestamp) AS rendered_at
  FROM recommendation_events
  WHERE event_name = 'recommendation_rendered'
    AND event_timestamp BETWEEN :start_date AND :end_date
  GROUP BY 1,2,3
),
completions AS (
  SELECT
    recommendation_id,
    user_id,
    MIN(event_timestamp) AS completed_at
  FROM recommendation_events
  WHERE event_name = 'recommendation_completed'
    AND event_timestamp BETWEEN :start_date AND :end_date
  GROUP BY 1,2
)
SELECT
  i.goal_context,
  COUNT(DISTINCT CASE WHEN c.completed_at IS NOT NULL AND EXTRACT(EPOCH FROM (c.completed_at - i.rendered_at)) <= 604800 THEN i.recommendation_id END) * 1.0 /
  NULLIF(COUNT(DISTINCT i.recommendation_id), 0) AS actionable_recommendation_rate
FROM impressions i
LEFT JOIN completions c USING (recommendation_id, user_id)
GROUP BY 1;
```

## Operational Checklist
- Ensure the goal context taxonomy is co-designed with user research and localized teams.
- Run the fairness audit notebook monthly to confirm no protected segment has an actionable rate <80% of the top-performing group.
- Review qualitative feedback for the top negative themes and log remediation actions in the decision log template.
