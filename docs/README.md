# Meaningful Metrics Documentation

Welcome to the Meaningful Metrics documentation.

## Contents

### Concepts

Understand the theory behind the metrics:

- [Quality Time Score](concepts/quality-time-score.md) - The primary metric
- [Goal Alignment](concepts/goal-alignment.md) - Tracking goal-related time
- [Actionability](concepts/actionability.md) - Information to action conversion

### API Reference

Technical documentation:

- [API Reference](api/README.md) - Function signatures and types

### Examples

Practical usage examples:

- [Basic Usage](examples/basic_usage.md) - Getting started

## Quick Start

```python
from meaningful_metrics import calculate_quality_time_score
from meaningful_metrics.schemas import TimeEntry, DomainPriority

# Define priorities
priorities = [
    DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
]

# Track time
entries = [TimeEntry(domain="learning", hours=2.0)]

# Calculate
qts = calculate_quality_time_score(entries, priorities)
print(f"Quality Time Score: {qts}")
```

## Philosophy

Meaningful Metrics is built on the belief that:

1. **Users should define what matters** - Not algorithms
2. **All metrics should be transparent** - No hidden calculations
3. **Privacy is non-negotiable** - Data stays local
4. **Wellbeing trumps engagement** - Always

## Contributing

See the main [README](../README.md) for development setup.
