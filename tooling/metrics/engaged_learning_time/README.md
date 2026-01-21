# Engaged Learning Time — Instrumentation Guide

## Required Events
| Event Name | Description | Key Properties |
|------------|-------------|----------------|
| `lesson_start` | Learner begins a structured lesson or module. | `learner_id`, `lesson_id`, `content_difficulty`, `assistive_mode` |
| `reflection_logged` | Learner completes a reflective checkpoint. | `reflection_type`, `duration_seconds`, `sentiment_score` |
| `skill_assessment_completed` | Learner completes an assessment tied to the lesson. | `assessment_id`, `score`, `mastery_delta` |
| `session_end` | Learning session ends. | `duration_seconds`, `focus_mode`, `interruptions_count` |

## Reference Query
Use the SQL snippet below to compute the metric with guardrails that taper excessive session lengths and reward skill gains.

```sql
WITH session_data AS (
  SELECT
    learner_id,
    session_id,
    SUM(CASE WHEN event_name = 'lesson_start' THEN 1 ELSE 0 END) AS lessons_started,
    SUM(CASE WHEN event_name = 'reflection_logged' THEN duration_seconds END) AS reflection_seconds,
    SUM(CASE WHEN event_name = 'session_end' THEN duration_seconds END) AS session_seconds,
    AVG(CASE WHEN event_name = 'skill_assessment_completed' THEN mastery_delta END) AS avg_mastery_delta
  FROM learning_events
  WHERE event_name IN ('lesson_start','reflection_logged','session_end','skill_assessment_completed')
    AND event_timestamp BETWEEN :start_date AND :end_date
  GROUP BY learner_id, session_id
)
SELECT
  learner_id,
  AVG(
    LEAST(session_seconds, 45 * 60) * 0.6 +
    COALESCE(reflection_seconds, 0) * 0.2 +
    GREATEST(avg_mastery_delta, 0) * 0.2
  ) AS engaged_learning_time_score
FROM session_data
GROUP BY learner_id;
```

## Operational Checklist
- Review fairness slices monthly across disability status, locale, and device type.
- Pair quantitative results with the qualitative reflection sampling protocol in the governance toolkit.
- Document any metric definition changes in the community changelog within 7 days.
