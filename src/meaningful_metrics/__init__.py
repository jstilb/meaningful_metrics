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
    calculate_actionability_score,
    calculate_distraction_ratio,
    calculate_goal_alignment,
    calculate_locality_score,
    calculate_quality_time_score,
)
from meaningful_metrics.schemas import (
    ActionLog,
    ActionWeights,
    DomainMetrics,
    DomainPriority,
    Goal,
    MetricsReport,
    Recommendation,
    TimeEntry,
)
from meaningful_metrics.scoring import (
    calculate_domain_contributions,
    generate_metrics_report,
    generate_recommendations,
)

__all__ = [
    "ActionLog",
    "ActionWeights",
    "DomainMetrics",
    "DomainPriority",
    "Goal",
    "MetricsReport",
    "Recommendation",
    "TimeEntry",
    "__version__",
    "calculate_actionability_score",
    "calculate_distraction_ratio",
    "calculate_domain_contributions",
    "calculate_goal_alignment",
    "calculate_locality_score",
    "calculate_quality_time_score",
    "generate_metrics_report",
    "generate_recommendations",
]
