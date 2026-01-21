# Goal Alignment Metric

## Definition

Goal Alignment measures the percentage of time spent on activities that directly support the user's stated goals.

## Formula

```
Goal Alignment = (sum(Time_goal_domains) / Total_time) * 100%
```

Where:
- **Time_goal_domains** = Time spent in domains linked to active goals
- **Total_time** = Total tracked time

## Purpose

### Why Track Goal Alignment?

Users often have intentions that don't match their behavior:
- "I want to learn to code" (goal)
- But spend 3 hours on social media (behavior)

Goal Alignment quantifies this gap.

### Relationship to QTS

While QTS weights all time by priority, Goal Alignment focuses specifically on:
- Time that advances stated objectives
- Binary classification: goal-related or not

## Example

### User's Goals

1. **Learn Spanish** - domains: ["language_learning", "spanish_content"]
2. **Get fit** - domains: ["exercise", "fitness_content", "nutrition"]

### Time Spent (Weekly)

| Domain | Hours |
|--------|-------|
| language_learning | 5 |
| social_media | 10 |
| work | 30 |
| exercise | 3 |
| entertainment | 8 |

### Calculation

Goal-related domains: language_learning (5h) + exercise (3h) = 8 hours
Total tracked: 56 hours

```
Goal Alignment = 8 / 56 * 100% = 14.3%
```

### Interpretation

Only 14.3% of this user's time directly supports their goals. This provides clear feedback for behavior change.

## Implementation

```python
def calculate_goal_alignment(
    time_entries: list[TimeEntry],
    goals: list[Goal],
) -> float:
    """Calculate goal alignment percentage.

    Args:
        time_entries: Time spent per domain.
        goals: User's defined goals with linked domains.

    Returns:
        Percentage of time spent on goal-related activities.
    """
    goal_domains = set()
    for goal in goals:
        goal_domains.update(goal.domains)

    total_time = sum(e.hours for e in time_entries)
    goal_time = sum(
        e.hours for e in time_entries
        if e.domain in goal_domains
    )

    if total_time == 0:
        return 0.0

    return (goal_time / total_time) * 100
```

## Considerations

### Domain Mapping

Goals should map to trackable domains:
- Goal: "Learn to code" -> Domains: ["coding", "tutorials", "documentation"]
- Goal: "Stay informed" -> Domains: ["news", "newsletters", "podcasts"]

### Exclusions

Some domains shouldn't count as "distraction":
- Sleep
- Meals
- Necessary errands

Consider a "neutral" category that doesn't affect Goal Alignment.

### Target Ranges

Suggested goal alignment targets:
- **10-20%**: Low alignment (common starting point)
- **30-40%**: Moderate alignment
- **50%+**: High alignment (aspirational for most)

Note: 100% alignment is not the goal. Rest, recovery, and leisure are important.

## Related Metrics

- **Distraction Ratio**: The inverse (time on non-goal activities)
- **Quality Time Score**: Weighted time including goals
- **Progress Velocity**: Rate of goal completion over time
