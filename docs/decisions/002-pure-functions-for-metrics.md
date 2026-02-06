# ADR-002: Pure Functions for Metric Calculations

## Status

Accepted

## Date

2024-12-01

## Context

The core metric calculations (Quality Time Score, Goal Alignment, etc.) need an implementation pattern that:

- Makes formulas auditable and testable
- Supports both standalone usage and composition into reports
- Enables future ML optimization (gradient-based training)
- Keeps the codebase simple for open-source contributors

Options considered:
1. **Pure functions** -- Stateless functions taking typed inputs
2. **Class-based calculators** -- `MetricsCalculator` with methods and internal state
3. **Strategy pattern** -- Abstract base class with pluggable implementations
4. **Pipeline/chain pattern** -- Composable transformation steps

## Decision

Implement all metrics as pure functions in `metrics.py`, composed by higher-level functions in `scoring.py`.

## Rationale

- **Testability**: Pure functions with no side effects are trivial to unit test -- provide inputs, assert outputs. No setup/teardown, no mocking.
- **Auditability**: Each function's docstring contains the exact mathematical formula. Reviewers can verify correctness by reading a single function.
- **Composability**: `scoring.py` composes individual metrics into reports without coupling. Adding a new metric means adding one function and one line in the report generator.
- **ML compatibility**: Pure functions can be wrapped in differentiable frameworks. The `soft_min` utility demonstrates this -- a smooth approximation of `min()` for gradient computation.
- **Simplicity**: No class hierarchies, no state management, no dependency injection. A contributor can understand any metric by reading one function.

## Consequences

- **Positive**: Each metric is independently testable with ~5 lines of test code per case.
- **Positive**: The `scoring.py` composition layer is a thin orchestrator, easy to extend.
- **Negative**: Shared computation (e.g., priority lookup) is duplicated across functions. Acceptable at current scale; can be refactored if metrics grow beyond 10+.
- **Negative**: No caching of intermediate results. Acceptable because the computational cost is trivial (linear in number of time entries).
