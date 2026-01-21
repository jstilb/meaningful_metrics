"""Meaningful Metrics: A framework for AI systems that optimize for human wellbeing.

This library provides metrics and scoring functions that can be used to train
AI systems to optimize for quality of experience, goal alignment, and meaningful
outcomes rather than engagement maximization.

Core Metrics:
    - Quality Time Score (QTS): Priority-weighted time with diminishing returns
    - Goal Alignment: Percentage of time on stated goals
    - Distraction Ratio: Percentage of time on non-goal activities
    - Actionability Score: Information to action conversion rate
    - Locality Score: Community relevance weighting

Example:
    >>> from meaningful_metrics import calculate_quality_time_score
    >>> from meaningful_metrics.schemas import TimeEntry, DomainPriority
    >>>
    >>> priorities = [DomainPriority(domain="learning", priority=1.0)]
    >>> entries = [TimeEntry(domain="learning", hours=2.0)]
    >>> calculate_quality_time_score(entries, priorities)
    2.0
"""

__version__ = "0.1.0"
__author__ = "jstilb"

from meaningful_metrics.metrics import (
    calculate_quality_time_score,
    calculate_goal_alignment,
    calculate_distraction_ratio,
    calculate_actionability_score,
    calculate_locality_score,
)

from meaningful_metrics.scoring import (
    generate_metrics_report,
    calculate_domain_contributions,
    generate_recommendations,
)

from meaningful_metrics.schemas import (
    # Input types
    Goal,
    DomainPriority,
    TimeEntry,
    ActionLog,
    ActionWeights,
    # Output types
    MetricsReport,
    DomainMetrics,
    Recommendation,
)

__all__ = [
    # Version
    "__version__",
    # Core metric functions
    "calculate_quality_time_score",
    "calculate_goal_alignment",
    "calculate_distraction_ratio",
    "calculate_actionability_score",
    "calculate_locality_score",
    # Scoring functions
    "generate_metrics_report",
    "calculate_domain_contributions",
    "generate_recommendations",
    # Input schemas
    "Goal",
    "DomainPriority",
    "TimeEntry",
    "ActionLog",
    "ActionWeights",
    # Output schemas
    "MetricsReport",
    "DomainMetrics",
    "Recommendation",
]
