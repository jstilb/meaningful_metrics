# Quality Time Score (QTS)

## Definition

The Quality Time Score is the primary metric in the Meaningful Metrics framework. It provides a weighted measure of time spent that accounts for user priorities and diminishing returns.

## Formula

```
QTS = sum(min(Ti, Capi) * Pi)
```

Where:
- **Ti** = Time spent in domain i (hours)
- **Capi** = Maximum valuable hours for domain i (diminishing returns cap)
- **Pi** = Priority score for domain i (0.0 - 1.0)

## Rationale

### Why Not Raw Time?

Raw time treats all hours equally:
- 1 hour learning = 1 hour scrolling social media
- 4 hours of focused work = 4 hours of distracted browsing

This fails to capture the *quality* of time spent.

### Priority Weighting

Users define what matters to them:
- Learning might have priority 1.0
- Entertainment might have priority 0.5
- Mindless scrolling might have priority 0.1

The QTS weights time accordingly.

### Diminishing Returns

The cap prevents over-optimization:
- Reading for 4 hours when 2 hours is optimal = 2 hours contribution
- This encourages balanced time allocation
- Prevents "gaming" the metric with excessive time in one area

## Example Calculation

### Scenario

A user's time allocation for a day:
- Learning: 3 hours
- Work: 5 hours
- Social Media: 2 hours
- News: 1 hour

Their priorities:
- Learning: P=1.0, Cap=4h
- Work: P=0.8, Cap=8h
- Social Media: P=0.2, Cap=1h
- News: P=0.5, Cap=1h

### Calculation

```
QTS = min(3, 4) * 1.0    # Learning: 3 * 1.0 = 3.0
    + min(5, 8) * 0.8    # Work: 5 * 0.8 = 4.0
    + min(2, 1) * 0.2    # Social Media: 1 * 0.2 = 0.2 (capped!)
    + min(1, 1) * 0.5    # News: 1 * 0.5 = 0.5

QTS = 3.0 + 4.0 + 0.2 + 0.5 = 7.7
```

### Comparison to Raw Time

Raw time = 3 + 5 + 2 + 1 = 11 hours

QTS efficiency = 7.7 / 11 = 70%

This tells the user that 70% of their time was spent meaningfully according to their own priorities.

## Implementation Notes

### Differentiability

The QTS formula uses `min()` which has a subgradient at the boundary. For smooth optimization, consider using a soft-min approximation:

```python
def soft_min(a: float, b: float, alpha: float = 10.0) -> float:
    """Smooth approximation of min(a, b) for differentiability."""
    return -1/alpha * log(exp(-alpha * a) + exp(-alpha * b))
```

### Edge Cases

1. **Missing priorities**: Default to 0.5 (neutral)
2. **No cap defined**: Use infinity (no diminishing returns)
3. **Zero time**: QTS contribution is 0
4. **Negative time**: Raise validation error

### Recommended Defaults

| Domain | Default Priority | Default Cap |
|--------|------------------|-------------|
| Learning | 1.0 | 4 hours |
| Deep Work | 0.9 | 6 hours |
| Communication | 0.6 | 2 hours |
| News | 0.5 | 1 hour |
| Entertainment | 0.4 | 2 hours |
| Social Media | 0.2 | 1 hour |

## Related Metrics

- **Goal Alignment**: Measures what percentage of time goes to goal-related domains
- **Distraction Ratio**: Inverse - time on non-goal activities
- **Actionability Score**: Whether consumed content leads to action

## References

- Attention Economics (Herbert Simon)
- Flow State Research (Csikszentmihalyi)
- Time Blocking Methodology (Cal Newport)
