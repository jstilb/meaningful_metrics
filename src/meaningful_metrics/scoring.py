"""Composite scoring and report generation.

This module provides higher-level functions for generating complete metrics
reports and recommendations based on the core metrics.

Functions:
    - generate_metrics_report: Create a complete metrics report
    - calculate_domain_contributions: Break down QTS by domain
    - generate_recommendations: Create actionable improvement suggestions
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from meaningful_metrics.metrics import (
    calculate_actionability_score_from_log,
    calculate_distraction_ratio,
    calculate_goal_alignment,
    calculate_quality_time_score,
)
from meaningful_metrics.schemas import (
    DomainMetrics,
    MetricsReport,
    Recommendation,
)

if TYPE_CHECKING:
    from meaningful_metrics.schemas import (
        ActionLog,
        DomainPriority,
        Goal,
        TimeEntry,
    )


def calculate_domain_contributions(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
    *,
    default_priority: float = 0.5,
) -> list[DomainMetrics]:
    """Calculate per-domain contributions to the Quality Time Score.

    Breaks down the QTS calculation to show how each domain contributes,
    including the effect of diminishing returns caps.

    Args:
        time_entries: List of time spent per domain.
        priorities: List of domain priorities with optional caps.
        default_priority: Priority for domains without explicit priority.

    Returns:
        List of DomainMetrics with contribution details.

    Example:
        >>> from meaningful_metrics.schemas import TimeEntry, DomainPriority
        >>> entries = [TimeEntry(domain="learning", hours=3.0)]
        >>> priorities = [
        ...     DomainPriority(domain="learning", priority=1.0, max_daily_hours=2.0)
        ... ]
        >>> metrics = calculate_domain_contributions(entries, priorities)
        >>> metrics[0].effective_time  # Capped at 2.0
        2.0
        >>> metrics[0].contribution  # 2.0 * 1.0
        2.0
    """
    priority_map: dict[str, DomainPriority] = {p.domain: p for p in priorities}
    domain_metrics: list[DomainMetrics] = []

    for entry in time_entries:
        priority_config = priority_map.get(entry.domain)

        if priority_config:
            priority = priority_config.priority
            cap = priority_config.max_daily_hours
        else:
            priority = default_priority
            cap = None

        effective_time = entry.hours if cap is None else min(entry.hours, cap)
        contribution = effective_time * priority

        domain_metrics.append(
            DomainMetrics(
                domain=entry.domain,
                time_spent=entry.hours,
                effective_time=effective_time,
                priority=priority,
                contribution=contribution,
            )
        )

    return domain_metrics


def generate_recommendations(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
    goals: list[Goal],
    goal_alignment: float,
) -> list[Recommendation]:
    """Generate actionable recommendations based on metrics analysis.

    Analyzes time allocation against goals and priorities to suggest
    improvements that would increase wellbeing metrics.

    Args:
        time_entries: List of time spent per domain.
        priorities: List of domain priorities.
        goals: List of user's goals.
        goal_alignment: Current goal alignment percentage.

    Returns:
        List of Recommendation objects with improvement suggestions.

    Example:
        >>> # When goal alignment is low
        >>> recs = generate_recommendations(entries, priorities, goals, 15.0)
        >>> any(r.type == "increase" for r in recs)
        True
    """
    recommendations: list[Recommendation] = []
    priority_map: dict[str, DomainPriority] = {p.domain: p for p in priorities}

    # Collect goal domains
    goal_domains: set[str] = set()
    for goal in goals:
        goal_domains.update(goal.domains)

    # Analyze each time entry
    time_by_domain: dict[str, float] = {e.domain: e.hours for e in time_entries}

    # Low goal alignment recommendation
    if goal_alignment < 30.0 and goal_domains:
        recommendations.append(
            Recommendation(
                type="increase",
                domain=next(iter(goal_domains)),
                message=f"Goal alignment is only {goal_alignment:.0f}%. Consider spending more time on goal-related activities.",
                priority="high",
            )
        )

    # Check for domains exceeding caps
    for entry in time_entries:
        priority_config = priority_map.get(entry.domain)
        if (
            priority_config
            and priority_config.max_daily_hours
            and entry.hours > priority_config.max_daily_hours
        ):
            excess = entry.hours - priority_config.max_daily_hours
            recommendations.append(
                Recommendation(
                    type="decrease",
                    domain=entry.domain,
                    message=f"You spent {excess:.1f}h over your cap for {entry.domain}. Consider reallocating to higher-priority activities.",
                    priority="medium",
                )
            )

    # Check for low-priority domains taking significant time
    for entry in time_entries:
        priority_config = priority_map.get(entry.domain)
        priority = priority_config.priority if priority_config else 0.5

        if priority < 0.3 and entry.hours > 2.0:
            recommendations.append(
                Recommendation(
                    type="decrease",
                    domain=entry.domain,
                    message=f"Spent {entry.hours:.1f}h on low-priority domain '{entry.domain}'. Consider reducing this time.",
                    priority="medium",
                )
            )

    # Check for under-utilized goal domains
    for goal in goals:
        if goal.target_hours_per_week:
            goal_time = sum(time_by_domain.get(d, 0.0) for d in goal.domains)
            if goal_time < goal.target_hours_per_week * 0.5:
                recommendations.append(
                    Recommendation(
                        type="increase",
                        domain=goal.domains[0] if goal.domains else "goal_activities",
                        message=f"Progress on '{goal.name}' is behind target. Spent {goal_time:.1f}h vs {goal.target_hours_per_week:.0f}h target.",
                        priority="high",
                    )
                )

    # Positive reinforcement for good alignment
    if goal_alignment >= 50.0:
        recommendations.append(
            Recommendation(
                type="maintain",
                domain="overall",
                message=f"Great job! Goal alignment is {goal_alignment:.0f}%. Keep up the good work.",
                priority="low",
            )
        )

    return recommendations


def generate_metrics_report(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
    goals: list[Goal],
    actions: ActionLog | None = None,
    period: Literal["daily", "weekly"] = "daily",
) -> MetricsReport:
    """Generate a complete metrics report.

    Combines all metrics into a comprehensive report with domain
    breakdowns and actionable recommendations.

    Args:
        time_entries: List of time spent per domain.
        priorities: List of domain priorities with optional caps.
        goals: List of user's goals with linked domains.
        actions: Optional action log for actionability calculation.
        period: Reporting period ("daily" or "weekly").

    Returns:
        Complete MetricsReport with all metrics and recommendations.

    Example:
        >>> from meaningful_metrics.schemas import TimeEntry, DomainPriority, Goal
        >>> entries = [TimeEntry(domain="learning", hours=2.0)]
        >>> priorities = [DomainPriority(domain="learning", priority=1.0)]
        >>> goals = [Goal(id="learn", name="Learn", domains=["learning"])]
        >>> report = generate_metrics_report(entries, priorities, goals)
        >>> report.quality_time_score
        2.0
        >>> report.goal_alignment_percent
        100.0
    """
    # Calculate core metrics
    qts = calculate_quality_time_score(time_entries, priorities)
    goal_alignment = calculate_goal_alignment(time_entries, goals)
    distraction = calculate_distraction_ratio(time_entries, goals)

    # Calculate actionability if action log provided
    actionability = 0.0
    if actions is not None:
        actionability = calculate_actionability_score_from_log(actions)

    # Calculate domain breakdowns
    domain_metrics = calculate_domain_contributions(time_entries, priorities)

    # Generate recommendations
    recommendations = generate_recommendations(
        time_entries, priorities, goals, goal_alignment
    )

    # Calculate raw time
    raw_time = sum(entry.hours for entry in time_entries)

    return MetricsReport(
        period=period,
        quality_time_score=qts,
        raw_time_hours=raw_time,
        goal_alignment_percent=goal_alignment,
        distraction_percent=distraction,
        actionability_score=actionability,
        by_domain=domain_metrics,
        recommendations=recommendations,
    )
