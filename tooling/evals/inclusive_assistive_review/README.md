# Inclusive Assistive Review — Operations Toolkit

## Automation Script (Pseudocode)
Use the Python snippet to validate privacy redaction behavior nightly.

```python
from privacy_checks import generate_prompts, run_assistant, assert_redaction

prompts = generate_prompts(categories=["medical", "financial", "education"], locales=["en-US", "es-ES"]) 

for prompt in prompts:
    response = run_assistant(prompt.text, assistive_mode=prompt.assistive_mode)
    assert_redaction(response, prompt.expected_masks)
```

Log results to the decision log with fields `prompt_category`, `result`, and `ticket_reference`.

## Facilitation Checklist
- Confirm attendance of Accessibility PM, model leads, policy counsel, support representative, and at least two disabled advisors.
- Review quantitative dashboards (completion, privacy incidents, handoff SLAs) prior to the meeting.
- Capture action items with owners and due dates, linking to the remediation backlog.

## Inputs Required
- Latest empowerment survey results exported via `empowerment_survey_results.csv`.
- Transcript samples flagged for quality review.
- Support ticket summary filtered to accessibility-related categories.

Store artifacts in an accessible drive and reference them in meeting minutes recorded in `community/meeting_notes.md`.
