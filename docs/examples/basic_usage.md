# Basic Usage Examples

## Setup

First, install the library:

```bash
pip install meaningful-metrics
```

## Example 1: Calculate Quality Time Score

```python
from meaningful_metrics import calculate_quality_time_score
from meaningful_metrics.schemas import TimeEntry, DomainPriority

# Define your domain priorities
priorities = [
    DomainPriority(
        domain="learning",
        priority=1.0,
        max_daily_hours=4.0,
    ),
    DomainPriority(
        domain="work",
        priority=0.8,
        max_daily_hours=8.0,
    ),
    DomainPriority(
        domain="social_media",
        priority=0.2,
        max_daily_hours=1.0,
    ),
    DomainPriority(
        domain="entertainment",
        priority=0.4,
        max_daily_hours=2.0,
    ),
]

# Track your daily time
time_entries = [
    TimeEntry(domain="learning", hours=2.5),
    TimeEntry(domain="work", hours=6.0),
    TimeEntry(domain="social_media", hours=1.5),  # Over the cap!
    TimeEntry(domain="entertainment", hours=1.0),
]

# Calculate QTS
qts = calculate_quality_time_score(time_entries, priorities)

print(f"Raw time: {sum(e['hours'] for e in time_entries)} hours")
print(f"Quality Time Score: {qts:.2f}")

# Output:
# Raw time: 11.0 hours
# Quality Time Score: 7.5
# (Social media capped at 1h, so 1.5h only contributes 1*0.2=0.2)
```

## Example 2: Track Goal Alignment

```python
from meaningful_metrics import calculate_goal_alignment
from meaningful_metrics.schemas import TimeEntry, Goal

# Define your goals
goals = [
    Goal(
        id="learn-spanish",
        name="Learn Spanish",
        domains=["language_learning", "spanish_media"],
        target_hours_per_week=7.0,
    ),
    Goal(
        id="get-fit",
        name="Get Fit",
        domains=["exercise", "fitness_content"],
        target_hours_per_week=5.0,
    ),
]

# Weekly time entries
time_entries = [
    TimeEntry(domain="language_learning", hours=4.0),
    TimeEntry(domain="work", hours=40.0),
    TimeEntry(domain="exercise", hours=3.0),
    TimeEntry(domain="social_media", hours=7.0),
    TimeEntry(domain="entertainment", hours=10.0),
]

# Calculate alignment
alignment = calculate_goal_alignment(time_entries, goals)

print(f"Goal Alignment: {alignment:.1f}%")
# Output: Goal Alignment: 10.9%
# (7 hours on goals out of 64 total hours)
```

## Example 3: Generate Full Report

```python
from meaningful_metrics import generate_metrics_report
from meaningful_metrics.schemas import (
    TimeEntry,
    DomainPriority,
    Goal,
    ActionLog,
)

# Set up all inputs
priorities = [
    DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
    DomainPriority(domain="work", priority=0.8, max_daily_hours=8.0),
    DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
]

goals = [
    Goal(id="upskill", name="Upskill", domains=["learning", "tutorials"]),
]

time_entries = [
    TimeEntry(domain="learning", hours=2.0),
    TimeEntry(domain="work", hours=5.0),
    TimeEntry(domain="social_media", hours=2.0),
]

actions = ActionLog(
    consumed=50,
    bookmarked=10,
    shared=3,
    applied=2,
)

# Generate report
report = generate_metrics_report(
    time_entries=time_entries,
    priorities=priorities,
    goals=goals,
    actions=actions,
    period="daily",
)

# Print results
print(f"Quality Time Score: {report['quality_time_score']:.2f}")
print(f"Raw Hours: {report['raw_time_hours']:.1f}")
print(f"Goal Alignment: {report['goal_alignment_percent']:.1f}%")
print(f"Actionability: {report['actionability_score']:.2%}")

print("\nDomain Breakdown:")
for domain in report["by_domain"]:
    print(f"  {domain['domain']}: {domain['contribution']:.2f} contribution")

print("\nRecommendations:")
for rec in report["recommendations"]:
    print(f"  [{rec['priority']}] {rec['message']}")
```

## Example 4: Custom Actionability Weights

```python
from meaningful_metrics import calculate_actionability_score
from meaningful_metrics.schemas import ActionWeights

# Custom weights for your workflow
weights = ActionWeights(
    bookmarked=0.2,  # Bookmarking is less valuable to you
    shared=0.3,      # Sharing isn't a priority
    applied=1.5,     # Application is extra valuable
)

score = calculate_actionability_score(
    consumed=100,
    bookmarked=20,
    shared=5,
    applied=10,
    weights=weights,
)

print(f"Actionability: {score:.2%}")
```

## Example 5: Weekly Trends

```python
from meaningful_metrics import generate_metrics_report
from meaningful_metrics.schemas import TimeEntry, DomainPriority, Goal

# Define consistent priorities and goals
priorities = [
    DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
    DomainPriority(domain="work", priority=0.8),
]

goals = [Goal(id="learn", name="Learn", domains=["learning"])]

# Track multiple days
daily_entries = {
    "monday": [
        TimeEntry(domain="learning", hours=2.0),
        TimeEntry(domain="work", hours=8.0),
    ],
    "tuesday": [
        TimeEntry(domain="learning", hours=1.0),
        TimeEntry(domain="work", hours=9.0),
    ],
    "wednesday": [
        TimeEntry(domain="learning", hours=3.0),
        TimeEntry(domain="work", hours=7.0),
    ],
}

# Generate daily reports
for day, entries in daily_entries.items():
    report = generate_metrics_report(entries, priorities, goals)
    print(f"{day.capitalize()}: QTS={report['quality_time_score']:.2f}, "
          f"Alignment={report['goal_alignment_percent']:.0f}%")

# Output:
# Monday: QTS=8.4, Alignment=20%
# Tuesday: QTS=8.2, Alignment=10%
# Wednesday: QTS=8.6, Alignment=30%
```
