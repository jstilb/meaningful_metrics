# Meaningful Metrics

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A conceptual framework for training AI systems to optimize for human wellbeing rather than engagement maximization.

## The Problem

Current AI systems optimize for the wrong thing:
- **Engagement metrics** (time-on-app, clicks, scrolls)
- **All time weighted equally** (1 hour learning = 1 hour doomscrolling)
- **No diminishing returns** (4 hours of social media is "4x better")
- **Hidden algorithms** with no transparency

## The Solution

**Meaningful Metrics** provides alternative metrics that can train AI to optimize for:
- **Quality Time Score** - Priority-weighted time with diminishing returns
- **Goal Alignment** - Percentage of time on stated goals
- **Actionability** - Information to action conversion rate

## Installation

```bash
pip install meaningful-metrics
```

## Quick Start

```python
from meaningful_metrics import calculate_quality_time_score, generate_metrics_report
from meaningful_metrics.schemas import TimeEntry, DomainPriority, Goal

# Define your priorities
priorities = [
    DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
    DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
]

# Track your time
entries = [
    TimeEntry(domain="learning", hours=2.0),
    TimeEntry(domain="social_media", hours=1.5),  # Over cap!
]

# Calculate Quality Time Score
qts = calculate_quality_time_score(entries, priorities)
print(f"Quality Time Score: {qts}")  # 2.0*1.0 + 1.0*0.2 = 2.2 (not 3.5!)
```

## Core Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Quality Time Score** | `sum(min(Ti, Capi) * Pi)` | Weighted time with diminishing returns |
| **Goal Alignment** | `Time_goal / Total_time * 100%` | % time on stated goals |
| **Distraction Ratio** | `Time_distraction / Total_time * 100%` | % time on non-goals |
| **Actionability** | `Items_acted_on / Items_consumed` | Information to action rate |

## Key Features

- **Differentiable metrics** - Can be used in ML optimization
- **User-controlled** - Users set all priorities and goals
- **Transparent** - All formulas are documented and visible
- **Privacy-first** - Data stays local by default

## Ethical Principles

| Principle | Implementation |
|-----------|----------------|
| **User Autonomy** | User sets all goals and priorities |
| **Transparency** | All metrics and formulas visible |
| **Privacy** | All data stays local or user-controlled |
| **No Manipulation** | Never use dark patterns |
| **Wellbeing First** | Optimize for flourishing, not engagement |

## Documentation

- [Concepts](docs/concepts/) - Understanding the metrics
- [API Reference](docs/api/) - Function documentation
- [Examples](docs/examples/) - Usage examples

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
make test

# Type check
make typecheck

# Format code
make format

# Run all checks
make check
```

## Project Status

| Component | Status |
|-----------|--------|
| Framework definition | Complete |
| Formula specification | Complete |
| Python reference implementation | Complete |
| Integration APIs | Not started |
| Dashboard UI | Not started |

## License

MIT License - See [LICENSE](LICENSE) for details.

---

**Meaningful Metrics** - Because time spent should be time well spent.
