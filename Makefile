.PHONY: help install dev test lint format typecheck clean docs build publish

# Default target
help:
	@echo "Meaningful Metrics - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  install     Install package in development mode"
	@echo "  dev         Install with all development dependencies"
	@echo ""
	@echo "Quality:"
	@echo "  test        Run tests with pytest"
	@echo "  coverage    Run tests with coverage report"
	@echo "  lint        Run ruff linter"
	@echo "  format      Format code with black and ruff"
	@echo "  typecheck   Run mypy type checker"
	@echo "  check       Run all checks (lint, typecheck, test)"
	@echo ""
	@echo "Documentation:"
	@echo "  docs        Build documentation"
	@echo "  docs-serve  Serve documentation locally"
	@echo ""
	@echo "Build:"
	@echo "  build       Build package"
	@echo "  clean       Remove build artifacts"
	@echo ""

# =============================================================================
# Setup
# =============================================================================

install:
	pip install -e .

dev:
	pip install -e ".[dev,docs]"

# =============================================================================
# Quality Checks
# =============================================================================

test:
	pytest tests/ -v

coverage:
	pytest tests/ --cov=src/meaningful_metrics --cov-report=term-missing --cov-report=html

lint:
	ruff check src/ tests/

format:
	black src/ tests/
	ruff check --fix src/ tests/

typecheck:
	mypy src/

check: lint typecheck test
	@echo "All checks passed!"

# =============================================================================
# Documentation
# =============================================================================

docs:
	mkdocs build

docs-serve:
	mkdocs serve

# =============================================================================
# Build
# =============================================================================

build: clean
	python -m build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf src/*.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

# =============================================================================
# Publishing (requires credentials)
# =============================================================================

publish: build
	python -m twine upload dist/*

publish-test: build
	python -m twine upload --repository testpypi dist/*
