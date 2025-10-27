# Civic Participation Depth — Implementation Kit

## Event Schema
| Event | Description | Required Properties |
|-------|-------------|---------------------|
| `opportunity_viewed` | Resident views an opportunity detail page. | `resident_id`, `opportunity_id`, `neighborhood`, `language`, `access_needs` |
| `action_committed` | Resident commits to an action (RSVP, pledge, reminder). | `resident_id`, `opportunity_id`, `commitment_type`, `scheduled_at`, `channel` |
| `action_completed` | Resident confirms completion of the action. | `resident_id`, `opportunity_id`, `completion_verified` (bool), `verification_source` |
| `action_follow_up_submitted` | Resident completes follow-up survey/interview. | `resident_id`, `opportunity_id`, `satisfaction_score`, `barrier_theme` |
| `access_issue_reported` | Resident flags accessibility or logistical blockers. | `resident_id`, `opportunity_id`, `issue_type`, `severity` |

## Derived Metrics Query

```sql
WITH commitments AS (
  SELECT DISTINCT
    resident_id,
    opportunity_id,
    MIN(CASE WHEN event_name = 'opportunity_viewed' THEN event_timestamp END) AS viewed_at,
    MIN(CASE WHEN event_name = 'action_committed' THEN event_timestamp END) AS committed_at,
    MIN(CASE WHEN event_name = 'action_completed' THEN event_timestamp END) AS completed_at,
    MAX(CASE WHEN event_name = 'action_follow_up_submitted' THEN satisfaction_score END) AS satisfaction_score
  FROM civic_events
  WHERE event_timestamp BETWEEN :start_date AND :end_date
  GROUP BY resident_id, opportunity_id
)
SELECT
  neighborhood,
  language,
  COUNT(*) FILTER (WHERE committed_at IS NOT NULL AND completed_at IS NOT NULL) * 1.0 /
    NULLIF(COUNT(*) FILTER (WHERE committed_at IS NOT NULL), 0) AS completion_after_commit_rate,
  COUNT(*) FILTER (WHERE completed_at IS NOT NULL AND satisfaction_score >= 4) * 1.0 /
    NULLIF(COUNT(*) FILTER (WHERE completed_at IS NOT NULL), 0) AS satisfied_completion_rate
FROM commitments
GROUP BY neighborhood, language;
```

## Outreach Checklist
- Share monthly summaries with community partners including satisfaction trends and accessibility issue rates.
- Trigger outreach to organizers when completion-after-commit rate falls below 60% or when accessibility issue severity averages above 2.5.
- Log remediation actions and responsible owners in the decision log template for transparency.
