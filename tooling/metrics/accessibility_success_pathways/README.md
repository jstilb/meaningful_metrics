# Accessibility Success Pathways — Instrumentation Workbook

## Event Logging
| Event | Description | Key Properties |
|-------|-------------|----------------|
| `accessibility_mode_enabled` | User enables an accessibility feature (screen reader, high contrast, captions). | `user_id`, `feature_type`, `device_category` |
| `flow_entry` | User enters the guided accessible workflow. | `flow_id`, `entry_point`, `assistive_tech_type`, `locale` |
| `flow_checkpoint` | Intermediate milestone within the flow. | `flow_id`, `checkpoint_id`, `elapsed_seconds`, `error_state` |
| `flow_success` | User completes the workflow. | `flow_id`, `completion_time_seconds`, `satisfaction_rating` |
| `support_ticket_created` | Accessibility-related support ticket filed. | `ticket_id`, `issue_theme`, `severity`, `resolution_time_hours` |

## Monitoring Workbook
- Use the provided CSV template `accessibility_pathway_fairness_template.csv` to track completion rate parity across assistive technology types.
- Refresh dashboards weekly to monitor completion time deltas between assisted and baseline flows.

## Alerts
- Configure an alert when the ratio `assisted_completion_rate / baseline_completion_rate` drops below 0.85 for any segment.
- Trigger a PagerDuty incident when more than five high-severity support tickets are filed within a rolling 7-day period.

## Remediation Log
Document all issues and fixes using the decision log template in `docs/toolkit/decision_log_template.md`, referencing the ticket IDs and affected flows.
