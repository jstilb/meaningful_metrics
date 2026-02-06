# Model Card: Meaningful Metrics Scoring Framework

## Model Details

- **Name**: Meaningful Metrics v0.1.0
- **Type**: Rule-based scoring framework (not a trained ML model)
- **Authors**: [jstilb](https://github.com/jstilb)
- **License**: MIT
- **Repository**: https://github.com/jstilb/meaningful_metrics

## Intended Use

### Primary Use Cases

- **Product teams** evaluating whether their AI systems optimize for user wellbeing over engagement maximization
- **Researchers** studying the impact of attention-economy metrics on user behavior
- **Policy analysts** assessing platform accountability through human-centered KPIs
- **ML engineers** incorporating wellbeing-aligned reward signals into training pipelines

### Out of Scope

- Real-time production inference (designed for batch evaluation)
- Replacing domain-specific clinical or psychological assessments
- Automated decision-making without human review

## Metrics

| Metric | Description | Range | Interpretation |
|--------|-------------|-------|----------------|
| Quality Time Score | Priority-weighted time with diminishing returns | [0, inf) | Higher = more time on high-priority activities |
| Goal Alignment | Percentage of time on stated goals | [0, 100] | Higher = more goal-directed behavior |
| Distraction Ratio | Percentage of time on non-goal activities | [0, 100] | Lower = less distraction |
| Actionability Score | Information-to-action conversion rate | [0, inf) | Higher = content drives concrete action |
| Locality Score | Community relevance weighting | [0, 1] | Higher = more locally relevant engagement |

## Ethical Considerations

### Potential Benefits

- Shifts optimization targets from engagement to wellbeing
- Makes diminishing returns explicit through configurable caps
- Provides transparency through documented formulas
- Supports user agency through user-defined goals and priorities

### Potential Risks

- **Gamification**: Metrics could be gamed if users optimize for scores rather than genuine wellbeing
- **Cultural bias**: Default weight values reflect assumptions about "productive" vs. "unproductive" time that may not generalize across cultures
- **Reductionism**: Complex human experiences are simplified into numeric scores
- **Privacy**: Time-tracking data required for computation is inherently sensitive

### Mitigations

- All weights and caps are user-configurable -- no hardcoded value judgments
- Recommendations are advisory, not prescriptive
- The framework is designed for self-assessment, not external evaluation
- No data is collected or transmitted by the library itself

## Limitations

- Formulas are heuristic, not empirically validated against wellbeing outcomes
- Diminishing returns use a linear cap rather than a smooth decay curve
- The recommendation engine uses fixed thresholds (e.g., 30% goal alignment triggers a warning)
- No temporal modeling -- each evaluation is a snapshot, not a trend

## Evaluation

See `results/metrics.json` for benchmark evaluation results and `results/figures/` for visualizations of metric behavior under various input conditions.
