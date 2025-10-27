-- Run quarterly to monitor outreach fairness across demographics
WITH base AS (
  SELECT
    demographic_group,
    event_name,
    event_timestamp
  FROM civic_outreach_events
  WHERE event_timestamp BETWEEN :start_date AND :end_date
)
SELECT
  demographic_group,
  COUNT(*) FILTER (WHERE event_name = 'outreach_sent') AS outreach_sent,
  COUNT(*) FILTER (WHERE event_name = 'outreach_engaged') AS outreach_engaged,
  COUNT(*) FILTER (WHERE event_name = 'service_accessed') AS service_accessed,
  ROUND(COUNT(*) FILTER (WHERE event_name = 'outreach_engaged') * 1.0 /
        NULLIF(COUNT(*) FILTER (WHERE event_name = 'outreach_sent'), 0), 4) AS engagement_rate,
  ROUND(COUNT(*) FILTER (WHERE event_name = 'service_accessed') * 1.0 /
        NULLIF(COUNT(*) FILTER (WHERE event_name = 'outreach_sent'), 0), 4) AS service_access_rate
FROM base
GROUP BY demographic_group
ORDER BY demographic_group;
