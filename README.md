# Meaningful Metrics

[![CI](https://github.com/jstilb/meaningful_metrics/actions/workflows/ci.yml/badge.svg)](https://github.com/jstilb/meaningful_metrics/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/meaningful-metrics)](https://pypi.org/project/meaningful-metrics/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://jstilb.github.io/meaningful_metrics)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)
[![Coverage: >90%](https://img.shields.io/badge/coverage-%3E90%25-brightgreen.svg)](#evaluation-results)

A Python framework for evaluating AI systems against human-centered outcomes instead of engagement-maximization proxies. Provides composable, mathematically transparent metrics that reward products for empowering users rather than capturing their attention.

## Why I Built This

The attention economy optimizes for the wrong thing. Products track time-on-site, click-through rates, and session length -- metrics that reward addictive design over user wellbeing. As AI systems become the interface layer for digital experiences, the metrics we optimize for will shape how billions of people spend their time.

**Meaningful Metrics** provides an alternative: a scoring framework where "success" means users accomplished their goals, engaged purposefully, and took action on what they consumed -- not that they scrolled for three more hours.

This project exists at the intersection of my interests in **AI evaluation**, **responsible ML**, and **product analytics**. It demonstrates how evaluation frameworks can be designed to align AI behavior with human flourishing rather than engagement maximization.

## Connection to Constitutional AI

This framework is philosophically aligned with [Anthropic's Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) approach to AI evaluation. Where Constitutional AI asks models to evaluate outputs against a set of human values, Meaningful Metrics asks product teams to evaluate user experiences against declared human intentions.

Both approaches share a core conviction: **AI systems should be accountable to explicit human principles, not implicit engagement signals.**

## Key Metrics

| Metric | What It Measures | Why It Matters |
|--------|-----------------|----------------|
| **Quality Time Score** | Priority-weighted time with diminishing returns caps | Prevents over-optimization on any single domain |
| **Goal Alignment** | % of time on user-stated goals | Measures purposeful vs. passive engagement |
| **Distraction Ratio** | % of time on non-goal activities | Surfaces attention leakage |
| **Actionability Score** | Information-to-action conversion rate | Rewards content that drives behavior change |
| **Locality Score** | Community relevance weighting | Prioritizes locally impactful content |

## Quick Start

```bash
pip install meaningful-metrics
```

```python
from meaningful_metrics import (
    calculate_quality_time_score,
    generate_metrics_report,
)
from meaningful_metrics.schemas import (
    ActionLog,
    DomainPriority,
    Goal,
    TimeEntry,
)

# Define how a user spent their day
time_entries = [
    TimeEntry(domain="learning", hours=3.0),
    TimeEntry(domain="work", hours=5.0),
    TimeEntry(domain="social_media", hours=1.5),
]

# Set priorities (what SHOULD matter)
priorities = [
    DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
    DomainPriority(domain="work", priority=0.8),
    DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
]

# Define goals
goals = [
    Goal(id="learn-ml", name="Learn ML", domains=["learning"]),
]

# Generate a complete report
report = generate_metrics_report(
    time_entries=time_entries,
    priorities=priorities,
    goals=goals,
    actions=ActionLog(consumed=50, bookmarked=12, shared=3, applied=8),
)

print(f"Quality Time Score: {report.quality_time_score:.1f}")
print(f"Goal Alignment: {report.goal_alignment_percent:.0f}%")
print(f"Actionability: {report.actionability_score:.3f}")
```

## Evaluation Results

Benchmarked across three synthetic user profiles representing different engagement patterns:

| Profile | QTS | Goal Alignment | Actionability | Recommendations |
|---------|-----|----------------|---------------|-----------------|
| Balanced Learner | 8.1 | 38.1% | 0.242 | 2 |
| Distracted User | 1.0 | 5.3% | 0.023 | 4 |
| Focused Professional | 7.7 | 94.7% | 0.617 | 1 |

**Key findings:**
- The QTS correctly penalizes time on low-priority domains through diminishing returns caps (the "distracted user" scores 1.0 vs. 8.1 for the balanced learner despite spending similar total hours)
- Goal alignment drops sharply when non-goal domains dominate time allocation
- The actionability score distinguishes passive consumption (0.023) from active engagement (0.617)
- The recommendation engine generates more suggestions for users with greater room for improvement

See [`results/metrics.json`](results/metrics.json) for full benchmark data and [`results/figures/`](results/figures/) for visualizations.

**Real-world case study:** [ChatGPT scores 76% on Goal Alignment](results/case-studies/chatgpt-goal-alignment.md) — applying the framework to evaluate ChatGPT across three user segments, based on published research.

## Architecture

```
meaningful_metrics/
  src/meaningful_metrics/
    __init__.py        # Public API exports
    schemas.py         # Pydantic data models (input/output types)
    metrics.py         # Core metric functions (pure, stateless)
    scoring.py         # Composite scoring and report generation
  tests/               # pytest suite (>90% coverage)
  docs/
    architecture.md    # System design with Mermaid diagrams
    model_card.md      # Model card (risks, limitations, mitigations)
    decisions/         # Architecture Decision Records
  results/             # Benchmark data, visualizations, and case studies
  evals/               # AI evaluation playbooks and examples
  metrics/             # Human-centered metric proposals
  notebooks/           # Jupyter quickstart notebook
```

The framework follows a three-layer architecture:

1. **Schema Layer** (Pydantic v2) -- Validates all inputs at the boundary
2. **Metrics Core** (pure functions) -- Implements mathematical formulas with documented semantics
3. **Scoring Layer** -- Composes individual metrics into reports with actionable recommendations

See [`docs/architecture.md`](docs/architecture.md) for detailed diagrams and design rationale.

## Tech Stack

- **Python 3.11+** -- Type-annotated with `from __future__ import annotations`
- **Pydantic v2** -- Runtime data validation with Rust-powered performance
- **pytest + pytest-cov** -- Test suite with >90% coverage enforcement
- **ruff** -- Linting and formatting (replaces flake8 + black + isort)
- **mypy (strict)** -- Static type checking with full strict mode
- **GitHub Actions** -- CI/CD with lint, typecheck, and test jobs across Python 3.11-3.13

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run the full check suite
make check        # lint + typecheck + test

# Individual commands
make lint          # ruff check
make typecheck     # mypy strict
make test          # pytest
make coverage      # pytest with coverage report
make format        # auto-format with ruff
```

## Documentation

- [Full Docs Site](https://jstilb.github.io/meaningful_metrics) -- MkDocs with auto-generated API reference
- [Architecture & Design](docs/architecture.md) -- System diagrams and module relationships
- [Model Card](docs/model_card.md) -- Intended use, limitations, ethical considerations
- [ADR-001: Pydantic for Schemas](docs/decisions/001-pydantic-for-schemas.md) -- Why Pydantic over alternatives
- [ADR-002: Pure Functions](docs/decisions/002-pure-functions-for-metrics.md) -- Why stateless functions over classes
- [Metric Proposals](metrics/examples/) -- Example human-centered metrics
- [AI Eval Playbooks](evals/examples/) -- Responsible AI evaluation frameworks

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Contributions welcome for:
- New metric proposals (use [`docs/metric_template.md`](docs/metric_template.md))
- AI evaluation playbooks (use [`docs/eval_template.md`](docs/eval_template.md))
- Implementation tooling and integrations
- Research validating metric effectiveness

## License

MIT -- see [LICENSE](LICENSE).
