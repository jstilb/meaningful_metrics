# Quick Start

Get up and running with Meaningful Metrics in under 5 minutes.

## Installation

```bash
pip install meaningful-metrics
```

Requires Python 3.11+.

## Core Concepts (30-second version)

Meaningful Metrics has three inputs and one output:

| Input | What it is |
|-------|-----------|
| `TimeEntry` | Time spent in a domain (e.g., "coding: 2 hours") |
| `DomainPriority` | How valuable that domain is to the user (0.0–1.0) |
| `Goal` | What the user is trying to achieve, linked to domains |

| Output | What it is |
|--------|-----------|
| `MetricsReport` | QTS, goal alignment %, distraction %, recommendations |

## Step 1: Define Your Goals

Goals represent what the user wants to achieve. Each goal maps to one or more content domains.

```python
from meaningful_metrics.schemas import Goal

goals = [
    Goal(
        id="learn-ml",
        name="Learn Machine Learning",
        domains=["ml_courses", "coding", "research_papers"],
        target_hours_per_week=10.0,
    ),
    Goal(
        id="health",
        name="Maintain Health",
        domains=["exercise", "meal_prep", "sleep_tracking"],
    ),
]
```

## Step 2: Set Domain Priorities

Priorities weight how valuable each domain is. Set `max_daily_hours` to apply diminishing returns.

```python
from meaningful_metrics.schemas import DomainPriority

priorities = [
    DomainPriority(domain="ml_courses", priority=1.0, max_daily_hours=3.0),
    DomainPriority(domain="coding", priority=0.9, max_daily_hours=4.0),
    DomainPriority(domain="research_papers", priority=0.8),
    DomainPriority(domain="exercise", priority=0.7, max_daily_hours=1.5),
    DomainPriority(domain="social_media", priority=0.1),
    DomainPriority(domain="news", priority=0.3),
]
```

## Step 3: Log Time Entries

```python
from meaningful_metrics.schemas import TimeEntry

# Today's time log
entries = [
    TimeEntry(domain="coding", hours=2.5),
    TimeEntry(domain="ml_courses", hours=1.0),
    TimeEntry(domain="social_media", hours=2.0),
    TimeEntry(domain="exercise", hours=0.75),
    TimeEntry(domain="news", hours=0.5),
]
```

## Step 4: Generate Report

```python
from meaningful_metrics import generate_metrics_report

report = generate_metrics_report(
    time_entries=entries,
    priorities=priorities,
    goals=goals,
    period="daily",
)

print(f"Quality Time Score: {report.quality_time_score:.2f}")
print(f"Goal Alignment:     {report.goal_alignment_percent:.1f}%")
print(f"Distraction Ratio:  {report.distraction_percent:.1f}%")
print()
print("Recommendations:")
for rec in report.recommendations:
    print(f"  [{rec.priority.upper()}] {rec.message}")
```

Output:

```
Quality Time Score: 3.58
Goal Alignment:     57.9%
Distraction Ratio:  42.1%

Recommendations:
  [LOW] Great job! Goal alignment is 58%. Keep up the good work.
  [MEDIUM] Spent 2.0h on low-priority domain 'social_media'. Consider reducing this time.
```

## Step 5: Inspect Domain Breakdown

```python
print("\nBy Domain:")
for domain in report.by_domain:
    print(
        f"  {domain.domain}: "
        f"{domain.time_spent:.1f}h spent, "
        f"{domain.effective_time:.1f}h effective, "
        f"contribution={domain.contribution:.2f}"
    )
```

Output:

```
By Domain:
  coding: 2.5h spent, 2.5h effective, contribution=2.25
  ml_courses: 1.0h spent, 1.0h effective, contribution=1.00
  social_media: 2.0h spent, 2.0h effective, contribution=0.20
  exercise: 0.8h spent, 0.8h effective, contribution=0.53
  news: 0.5h spent, 0.5h effective, contribution=0.15
```

## Using Individual Metrics

You can also call metrics directly without generating a full report:

```python
from meaningful_metrics import (
    calculate_quality_time_score,
    calculate_goal_alignment,
    calculate_distraction_ratio,
    calculate_actionability_score,
)

# Just the QTS
qts = calculate_quality_time_score(entries, priorities)

# Goal alignment
alignment = calculate_goal_alignment(entries, goals)

# Actionability (requires action log)
from meaningful_metrics.schemas import ActionLog

actions = ActionLog(consumed=50, bookmarked=8, shared=3, applied=5)
actionability = calculate_actionability_score(
    consumed=actions.consumed,
    bookmarked=actions.bookmarked,
    shared=actions.shared,
    applied=actions.applied,
)
print(f"Actionability Score: {actionability:.3f}")
# Actionability Score: 0.224
```

## Next Steps

- [Concepts](concepts.md) — Understand the math behind each metric
- [API Reference](api/index.md) — Full function signatures
- [Case Studies](case-studies/chatgpt-goal-alignment.md) — See how to evaluate an AI product
