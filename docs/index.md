# Meaningful Metrics

[![CI](https://github.com/jstilb/meaningful_metrics/actions/workflows/ci.yml/badge.svg)](https://github.com/jstilb/meaningful_metrics/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/meaningful-metrics)](https://pypi.org/project/meaningful-metrics/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://jstilb.github.io/meaningful_metrics)

**A Python framework for evaluating AI systems against human wellbeing rather than engagement.**

---

## The Problem

Modern AI products are optimized for a single goal: maximize engagement. Watch time, click-through rates, session duration — these metrics reward the algorithm for keeping users on the platform, regardless of whether that time was spent well.

The result: recommendation systems that pull users toward outrage, social platforms designed to trigger compulsive checking, and AI assistants that flatter rather than inform.

## The Solution

Meaningful Metrics provides a composable set of evaluation primitives that measure what actually matters:

- **Goal Alignment** — Is the user making progress on what they said they wanted to do?
- **Quality Time Score** — Is time being spent on high-priority, purposeful activities?
- **Actionability Score** — Does consumed information translate into action?
- **Distraction Ratio** — How much time is lost to low-priority activities?
- **Locality Score** — Is content relevant to the user's actual context?

These metrics are differentiable (suitable for ML optimization), transparent (documented formulas), and user-controlled (user sets the priorities).

## Quick Example

```python
from meaningful_metrics import (
    calculate_quality_time_score,
    calculate_goal_alignment,
    generate_metrics_report,
)
from meaningful_metrics.schemas import (
    TimeEntry, DomainPriority, Goal
)

# User defines their goals
goals = [
    Goal(id="learn", name="Learn Python", domains=["coding", "tutorials"]),
    Goal(id="fitness", name="Stay Fit", domains=["exercise"]),
]

# User defines domain priorities
priorities = [
    DomainPriority(domain="coding", priority=1.0, max_daily_hours=4.0),
    DomainPriority(domain="tutorials", priority=0.9, max_daily_hours=2.0),
    DomainPriority(domain="exercise", priority=0.8, max_daily_hours=1.5),
    DomainPriority(domain="social_media", priority=0.2),
]

# Today's time entries
entries = [
    TimeEntry(domain="coding", hours=3.0),
    TimeEntry(domain="social_media", hours=1.5),
    TimeEntry(domain="exercise", hours=0.5),
]

# Generate report
report = generate_metrics_report(entries, priorities, goals)

print(f"Quality Time Score: {report.quality_time_score:.2f}")
print(f"Goal Alignment: {report.goal_alignment_percent:.1f}%")
print(f"Distraction: {report.distraction_percent:.1f}%")

# Quality Time Score: 3.30
# Goal Alignment: 70.0%
# Distraction: 30.0%
```

## Connection to Constitutional AI

This framework is philosophically aligned with [Anthropic's Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) approach to AI evaluation. Where Constitutional AI asks models to evaluate outputs against a set of human values, Meaningful Metrics asks product teams to evaluate user experiences against declared human intentions.

Both approaches share a core conviction: **AI systems should be accountable to explicit human principles, not implicit engagement signals.**

The Meaningful Metrics framework operationalizes this at the product layer — giving teams concrete measurements to hold their AI features accountable to user wellbeing.

## Installation

```bash
pip install meaningful-metrics
```

## Next Steps

- [Quick Start](quickstart.md) — Install and run your first evaluation in 5 minutes
- [Concepts](concepts.md) — Understand the framework's core ideas
- [API Reference](api/index.md) — Full function documentation
- [Case Studies](case-studies/chatgpt-goal-alignment.md) — Real-world evaluations
