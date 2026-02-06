# ADR-001: Use Pydantic v2 for Data Schemas

## Status

Accepted

## Date

2024-12-01

## Context

The Meaningful Metrics library needs a data validation layer that:

- Enforces type safety at runtime for user-provided inputs
- Provides clear error messages when inputs are invalid
- Supports serialization to/from JSON for API integration
- Works well with Python type checkers (mypy)
- Has minimal overhead for the computational workload

Options considered:
1. **Pydantic v2** -- Industry standard for data validation in Python
2. **dataclasses + manual validation** -- Lightweight but requires boilerplate
3. **attrs** -- Powerful but less ecosystem support than Pydantic
4. **TypedDict** -- Zero runtime overhead but no validation

## Decision

Use Pydantic v2 (`BaseModel`) for all input and output schemas.

## Rationale

- **Runtime validation**: Pydantic catches invalid inputs (negative hours, out-of-range priorities) before they reach metric calculations, preventing silent mathematical errors.
- **JSON serialization**: Built-in `.model_dump()` and `.model_validate()` make it trivial to serialize reports for dashboards and APIs.
- **Developer experience**: Pydantic v2's `Field()` descriptors serve as inline documentation, and validation errors include the field name and constraint that failed.
- **Type checker compatibility**: Pydantic v2's generated `__init__` signatures work with mypy in strict mode.
- **Performance**: Pydantic v2 uses Rust-based validation (pydantic-core), making validation overhead negligible compared to the metric calculations themselves.

## Consequences

- **Positive**: Clean separation between validation (schemas) and computation (metrics). New contributors can add fields without touching metric logic.
- **Positive**: JSON serialization enables integration with dashboards, APIs, and data pipelines with zero additional code.
- **Negative**: Adds `pydantic>=2.0` as a runtime dependency. Acceptable given Pydantic's ubiquity in the Python ecosystem.
- **Negative**: Slight learning curve for contributors unfamiliar with Pydantic model patterns.
