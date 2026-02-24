# API Reference

This section provides complete API documentation for the `meaningful_metrics` package, auto-generated from docstrings.

## Package Structure

```
meaningful_metrics/
├── __init__.py       # Public API exports
├── metrics.py        # Core metric calculation functions
├── schemas.py        # Pydantic data models
└── scoring.py        # Composite scoring and report generation
```

## Quick Navigation

- [Metrics](metrics.md) — Core calculation functions (`calculate_quality_time_score`, `calculate_goal_alignment`, etc.)
- [Schemas](schemas.md) — Data models (`Goal`, `TimeEntry`, `DomainPriority`, `MetricsReport`, etc.)
- [Scoring](scoring.md) — Report generation (`generate_metrics_report`, `generate_recommendations`, etc.)

## Top-Level Exports

All public functions and types are available directly from the `meaningful_metrics` namespace:

```python
from meaningful_metrics import (
    # Core metrics
    calculate_quality_time_score,
    calculate_goal_alignment,
    calculate_distraction_ratio,
    calculate_actionability_score,
    calculate_locality_score,
    # Composite scoring
    generate_metrics_report,
    generate_recommendations,
    calculate_domain_contributions,
    # Data models
    Goal,
    DomainPriority,
    TimeEntry,
    ActionLog,
    ActionWeights,
    DomainMetrics,
    Recommendation,
    MetricsReport,
)
```
