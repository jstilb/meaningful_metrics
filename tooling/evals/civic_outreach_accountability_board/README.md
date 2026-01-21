# Civic Outreach Accountability Board — Oversight Toolkit

## Data Workbook
The notebook `civic_outreach_bias_audit.sql` calculates parity ratios for impressions and conversions across demographics.

```sql
SELECT
  demographic_group,
  COUNT(*) FILTER (WHERE event_name = 'outreach_sent') AS outreach_sent,
  COUNT(*) FILTER (WHERE event_name = 'outreach_engaged') AS outreach_engaged,
  ROUND(
    COUNT(*) FILTER (WHERE event_name = 'outreach_engaged') * 1.0 /
    NULLIF(COUNT(*) FILTER (WHERE event_name = 'outreach_sent'), 0),
  4) AS engagement_rate,
  ROUND(
    COUNT(*) FILTER (WHERE event_name = 'service_accessed') * 1.0 /
    NULLIF(COUNT(*) FILTER (WHERE event_name = 'outreach_sent'), 0),
  4) AS service_access_rate
FROM civic_outreach_events
WHERE event_timestamp BETWEEN :start_date AND :end_date
GROUP BY demographic_group;
```

Flag segments whose engagement or service access rate is <0.9× the best-performing group.

## Meeting Agenda Template
1. Review outstanding remediation actions and confirm owners.
2. Walk through disparity analysis and determine if new mitigations are needed.
3. Evaluate transparency artifacts (message templates, translation QA, accessibility formats).
4. Log public commitments and timelines in `community/changelog.md`.

## Public Reporting Checklist
- Publish quarterly summary PDF and open data extract.
- Provide contact information for submitting feedback or appeals.
- Translate reports into top community languages and post to accessible channels (screen-reader friendly HTML, SMS summary).
