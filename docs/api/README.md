# API Reference

## Overview

The Meaningful Metrics library provides functions for calculating wellbeing-focused metrics from time tracking and activity data.

## Core Modules

### metrics.py

Core metric calculation functions.

```python
from meaningful_metrics import (
    calculate_quality_time_score,
    calculate_goal_alignment,
    calculate_distraction_ratio,
    calculate_actionability_score,
    calculate_locality_score,
)
```

### scoring.py

Composite scoring and report generation.

```python
from meaningful_metrics import (
    generate_metrics_report,
    calculate_domain_contributions,
    generate_recommendations,
)
```

### schemas.py

Data models for inputs and outputs.

```python
from meaningful_metrics.schemas import (
    # Input types
    Goal,
    DomainPriority,
    TimeEntry,
    ActionLog,

    # Output types
    MetricsReport,
    DomainMetrics,
    Recommendation,
)
```

## Quick Reference

### calculate_quality_time_score

```python
def calculate_quality_time_score(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
) -> float:
    """Calculate the Quality Time Score.

    QTS = sum(min(Ti, Capi) * Pi)

    Args:
        time_entries: Time spent per domain.
        priorities: Priority and cap settings per domain.

    Returns:
        Quality Time Score as a float.
    """
```

### calculate_goal_alignment

```python
def calculate_goal_alignment(
    time_entries: list[TimeEntry],
    goals: list[Goal],
) -> float:
    """Calculate goal alignment percentage.

    GA = sum(Time_goal_domains) / Total_time * 100

    Args:
        time_entries: Time spent per domain.
        goals: User's goals with linked domains.

    Returns:
        Percentage of time on goal-related activities.
    """
```

### calculate_actionability_score

```python
def calculate_actionability_score(
    consumed: int,
    bookmarked: int = 0,
    shared: int = 0,
    applied: int = 0,
    weights: ActionWeights | None = None,
) -> float:
    """Calculate actionability score.

    AS = weighted_actions / consumed

    Args:
        consumed: Total items consumed.
        bookmarked: Items saved for later.
        shared: Items shared with others.
        applied: Items that led to action.
        weights: Custom weights (default: 0.3, 0.5, 1.0).

    Returns:
        Actionability score (0.0 to 1.0+).
    """
```

### generate_metrics_report

```python
def generate_metrics_report(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
    goals: list[Goal],
    actions: ActionLog | None = None,
    period: Literal["daily", "weekly"] = "daily",
) -> MetricsReport:
    """Generate a complete metrics report.

    Args:
        time_entries: Time spent per domain.
        priorities: Priority settings.
        goals: User's goals.
        actions: Optional action log for actionability.
        period: Reporting period.

    Returns:
        Complete MetricsReport with all metrics and recommendations.
    """
```

## Type Definitions

### Input Types

```python
class TimeEntry(TypedDict):
    domain: str
    hours: float

class DomainPriority(TypedDict):
    domain: str
    priority: float  # 0.0 - 1.0
    max_daily_hours: NotRequired[float]

class Goal(TypedDict):
    id: str
    name: str
    domains: list[str]
    target_hours_per_week: NotRequired[float]

class ActionLog(TypedDict):
    consumed: int
    bookmarked: int
    shared: int
    applied: int
```

### Output Types

```python
class DomainMetrics(TypedDict):
    domain: str
    time_spent: float
    effective_time: float  # After caps applied
    priority: float
    contribution: float  # To QTS

class Recommendation(TypedDict):
    type: Literal["increase", "decrease", "maintain"]
    domain: str
    message: str
    priority: Literal["high", "medium", "low"]

class MetricsReport(TypedDict):
    period: Literal["daily", "weekly"]
    quality_time_score: float
    raw_time_hours: float
    goal_alignment_percent: float
    distraction_percent: float
    actionability_score: float
    by_domain: list[DomainMetrics]
    recommendations: list[Recommendation]
```

## Usage Examples

See the [examples directory](../examples/) for complete usage examples.
