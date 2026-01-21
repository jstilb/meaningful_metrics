# Meaningful Metrics Framework

> A conceptual framework for training AI systems to optimize for human wellbeing and goal achievement rather than engagement maximization.

## Overview

Meaningful Metrics addresses a critical gap in AI alignment: current systems optimize for time-on-app rather than user wellbeing. This framework provides differentiable, measurable metrics that can train AI to optimize for quality of experience, goal alignment, and meaningful outcomes.

## Core Philosophy

### The Problem
- Current AI systems maximize engagement (time-on-app)
- All time is weighted equally regardless of value
- No diminishing returns on consumption
- Hidden algorithms with no transparency
- Success = more scrolling

### The Solution
- Optimize for Quality Time Score (QTS)
- Priority-weighted time allocation
- Caps on useful time per domain
- Goal achievement as the success metric
- Transparent, user-controlled metrics

## Core Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Quality Time Score** | `QTS = sum(min(Ti, Capi) * Pi)` | Weighted sum of time * priority with diminishing returns |
| **Goal Alignment** | `GA = Time_goal_related / Total_time` | Percentage of time spent on stated goals |
| **Distraction Ratio** | `DR = Time_distraction / Total_time` | Percentage of time on non-goal activities |
| **Actionability Score** | `AS = Items_acted_on / Items_consumed` | Information to action conversion rate |
| **Locality Score** | `LS = Local_relevance * Engagement` | Weight for community-relevant content |

## Usage

### Installation

```bash
pip install meaningful-metrics
```

### Basic Usage

```python
from meaningful_metrics import calculate_quality_time_score
from meaningful_metrics.schemas import TimeEntry, DomainPriority

# Define your priorities
priorities = [
    DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
    DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
    DomainPriority(domain="news", priority=0.5, max_daily_hours=1.0),
]

# Track your time
entries = [
    TimeEntry(domain="learning", hours=2.0),
    TimeEntry(domain="social_media", hours=1.5),
]

# Calculate your Quality Time Score
qts = calculate_quality_time_score(entries, priorities)
print(f"Quality Time Score: {qts}")  # QTS considers priority and caps
```

## Architecture

```
meaningful_metrics/
├── src/
│   ├── __init__.py          # Package exports
│   ├── metrics.py            # Core metric calculations
│   ├── scoring.py            # Quality Time Score calculation
│   └── schemas.py            # Data models (TypedDict/Pydantic)
├── tests/
│   ├── test_metrics.py       # Metric calculation tests
│   ├── test_scoring.py       # Scoring function tests
│   └── test_schemas.py       # Schema validation tests
└── docs/
    ├── concepts/             # Conceptual documentation
    ├── api/                  # API reference
    └── examples/             # Usage examples
```

## Ethical Principles

| Principle | Implementation |
|-----------|----------------|
| **User Autonomy** | User sets all goals and priorities |
| **Transparency** | All metrics and formulas are visible |
| **Privacy** | All data stays local or user-controlled |
| **No Manipulation** | Never use dark patterns |
| **Wellbeing First** | Metrics optimize for flourishing, not engagement |

## Guardrails

### Always (No Approval Required)
- Calculate metrics from provided data
- Generate recommendations
- Show progress visualizations
- Export personal data

### Never (Absolutely Prohibited)
- Shame or guilt users
- Optimize for engagement over wellbeing
- Share individual data without consent
- Create addictive tracking loops
- Penalize taking breaks

## For AI Agents Working on This Project

### Key Context
- This is a **conceptual framework**, not a running application
- The Python library provides reference implementations of metrics
- The goal is to enable OTHER systems to optimize for human wellbeing
- Think of this as a "reward signal library" for AI alignment

### Development Principles
1. All metrics must be **differentiable** for ML optimization
2. Formulas must be **transparent** and explainable
3. Privacy is **non-negotiable** - no data leaves user control
4. **Test-driven development** is required

### When Extending This Framework
1. Ensure new metrics align with wellbeing optimization
2. Add comprehensive tests with edge cases
3. Document the mathematical foundation
4. Consider integration with existing data sources

## Research Foundation

Based on concepts from:
- Attention economics
- Wellbeing research (positive psychology)
- Goal-setting theory
- Information diet frameworks
- Time tracking methodologies

## License

MIT License - See LICENSE file for details.

---

**Meaningful Metrics** - Because time spent should be time well spent.
