# Copilot Instructions for Meaningful Metrics

## Project Overview

Meaningful Metrics is a Python library providing a conceptual framework for training AI systems to optimize for human wellbeing rather than engagement maximization.

## Key Concepts

### Core Metrics

1. **Quality Time Score (QTS)**: `sum(min(Ti, Capi) * Pi)`
   - Ti = Time spent in domain i
   - Capi = Max valuable hours (diminishing returns cap)
   - Pi = Priority score (0.0 - 1.0)

2. **Goal Alignment**: `Time_goal_related / Total_time * 100%`

3. **Distraction Ratio**: `Time_distraction / Total_time * 100%`

4. **Actionability Score**: `Items_acted_on / Items_consumed`

5. **Locality Score**: `Local_relevance * Engagement`

## Code Style

### Python Standards
- Use Python 3.11+
- Type hints required on all functions
- Pydantic or TypedDict for data models
- Docstrings in Google style format
- Maximum line length: 88 characters (Black formatter)

### Example Function

```python
def calculate_quality_time_score(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
) -> float:
    """Calculate the Quality Time Score from time entries and priorities.

    The QTS weights time spent by priority and applies diminishing returns
    caps to prevent over-optimization on any single domain.

    Args:
        time_entries: List of time spent per domain.
        priorities: List of domain priorities with optional caps.

    Returns:
        The calculated Quality Time Score as a float.

    Example:
        >>> entries = [TimeEntry(domain="learning", hours=2.0)]
        >>> priorities = [DomainPriority(domain="learning", priority=1.0)]
        >>> calculate_quality_time_score(entries, priorities)
        2.0
    """
```

## Testing Requirements

- All functions must have corresponding tests
- Test edge cases (zero time, max caps, missing domains)
- Use pytest as the test framework
- Aim for 100% coverage on core metrics

## Data Models

### Input Types

```python
class Goal(TypedDict):
    id: str
    name: str
    domains: list[str]
    target_hours_per_week: float

class DomainPriority(TypedDict):
    domain: str
    priority: float  # 0.0 - 1.0
    max_daily_hours: float | None

class TimeEntry(TypedDict):
    domain: str
    hours: float
```

### Output Types

```python
class MetricsReport(TypedDict):
    period: Literal["daily", "weekly"]
    quality_time_score: float
    raw_time_hours: float
    goal_alignment_percent: float
    distraction_percent: float
    by_domain: list[DomainMetrics]
    recommendations: list[Recommendation]
```

## Ethical Guidelines

When writing code for this project:

1. **Never optimize for engagement** - All metrics should promote wellbeing
2. **Transparency required** - No hidden calculations or magic numbers
3. **User control** - Users must be able to set all parameters
4. **No dark patterns** - No guilt, shame, or manipulation
5. **Privacy first** - Data stays local by default

## Common Tasks

### Adding a New Metric

1. Define the formula mathematically in docs/concepts/
2. Create the schema in src/schemas.py
3. Implement the calculation in src/metrics.py
4. Add tests in tests/test_metrics.py
5. Export from src/__init__.py

### Modifying Existing Metrics

1. Ensure backwards compatibility
2. Update all affected tests
3. Document the change rationale
4. Consider impact on downstream integrations

## File Structure

```
src/
  __init__.py      - Package exports
  metrics.py       - Core metric calculations
  scoring.py       - QTS and composite scoring
  schemas.py       - Pydantic/TypedDict models

tests/
  test_metrics.py  - Metric function tests
  test_scoring.py  - Scoring function tests
  test_schemas.py  - Schema validation tests

docs/
  concepts/        - Conceptual documentation
  api/             - API reference
  examples/        - Usage examples
```

## Dependencies

- pydantic >= 2.0 (data validation)
- pytest (testing)
- mypy (type checking)
- black (formatting)
- ruff (linting)

## Quick Commands

```bash
# Run tests
make test

# Type check
make typecheck

# Format code
make format

# Lint
make lint

# Build docs
make docs
```
