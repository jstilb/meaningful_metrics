"""Core metric calculation functions.

This module implements the fundamental metrics of the Meaningful Metrics framework:

- Quality Time Score (QTS): Priority-weighted time with diminishing returns
- Goal Alignment: Percentage of time on stated goals
- Distraction Ratio: Percentage of time on non-goal activities
- Actionability Score: Information to action conversion rate
- Locality Score: Community relevance weighting

All metrics are designed to be:
- Differentiable (for ML optimization)
- Transparent (formulas are documented)
- User-controlled (parameters set by user)
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from meaningful_metrics.schemas import (
        ActionLog,
        ActionWeights,
        DomainPriority,
        Goal,
        TimeEntry,
    )


def calculate_quality_time_score(
    time_entries: list[TimeEntry],
    priorities: list[DomainPriority],
    *,
    default_priority: float = 0.5,
) -> float:
    """Calculate the Quality Time Score from time entries and priorities.

    The QTS weights time spent by priority and applies diminishing returns
    caps to prevent over-optimization on any single domain.

    Formula:
        QTS = sum(min(Ti, Capi) * Pi)

        Where:
        - Ti = Time spent in domain i
        - Capi = Max valuable hours for domain i (or infinity if not set)
        - Pi = Priority score for domain i (0.0 - 1.0)

    Args:
        time_entries: List of time spent per domain.
        priorities: List of domain priorities with optional caps.
        default_priority: Priority for domains without explicit priority (default: 0.5).

    Returns:
        The calculated Quality Time Score as a float.

    Raises:
        ValueError: If time entries contain negative hours.

    Example:
        >>> from meaningful_metrics.schemas import TimeEntry, DomainPriority
        >>> entries = [TimeEntry(domain="learning", hours=2.0)]
        >>> priorities = [DomainPriority(domain="learning", priority=1.0)]
        >>> calculate_quality_time_score(entries, priorities)
        2.0

        >>> # With diminishing returns cap
        >>> priorities = [DomainPriority(domain="learning", priority=1.0, max_daily_hours=1.0)]
        >>> calculate_quality_time_score(entries, priorities)
        1.0
    """
    # Build priority lookup
    priority_map: dict[str, DomainPriority] = {p.domain: p for p in priorities}

    qts = 0.0

    for entry in time_entries:
        if entry.hours < 0:
            msg = f"Negative hours not allowed: {entry.domain} = {entry.hours}"
            raise ValueError(msg)

        # Get priority settings for this domain
        priority_config = priority_map.get(entry.domain)

        if priority_config:
            priority = priority_config.priority
            cap = priority_config.max_daily_hours
        else:
            priority = default_priority
            cap = None

        # Apply diminishing returns cap
        effective_time = entry.hours if cap is None else min(entry.hours, cap)

        # Add weighted contribution
        qts += effective_time * priority

    return qts


def calculate_goal_alignment(
    time_entries: list[TimeEntry],
    goals: list[Goal],
) -> float:
    """Calculate goal alignment percentage.

    Goal Alignment measures what percentage of tracked time is spent on
    activities that directly support the user's stated goals.

    Formula:
        GA = (sum(Time_goal_domains) / Total_time) * 100

    Args:
        time_entries: List of time spent per domain.
        goals: List of user's goals with linked domains.

    Returns:
        Percentage of time spent on goal-related activities (0.0 to 100.0).

    Example:
        >>> from meaningful_metrics.schemas import TimeEntry, Goal
        >>> entries = [
        ...     TimeEntry(domain="learning", hours=2.0),
        ...     TimeEntry(domain="social_media", hours=3.0),
        ... ]
        >>> goals = [Goal(id="learn", name="Learn", domains=["learning"])]
        >>> calculate_goal_alignment(entries, goals)
        40.0
    """
    if not time_entries:
        return 0.0

    # Collect all goal-related domains
    goal_domains: set[str] = set()
    for goal in goals:
        goal_domains.update(goal.domains)

    # Calculate totals
    total_time = sum(entry.hours for entry in time_entries)
    goal_time = sum(
        entry.hours for entry in time_entries if entry.domain in goal_domains
    )

    if total_time == 0:
        return 0.0

    return (goal_time / total_time) * 100


def calculate_distraction_ratio(
    time_entries: list[TimeEntry],
    goals: list[Goal],
) -> float:
    """Calculate distraction ratio percentage.

    The Distraction Ratio is the inverse of Goal Alignment - it measures
    what percentage of time is spent on non-goal activities.

    Formula:
        DR = 100 - Goal_Alignment

    Args:
        time_entries: List of time spent per domain.
        goals: List of user's goals with linked domains.

    Returns:
        Percentage of time spent on non-goal activities (0.0 to 100.0).

    Example:
        >>> from meaningful_metrics.schemas import TimeEntry, Goal
        >>> entries = [
        ...     TimeEntry(domain="learning", hours=2.0),
        ...     TimeEntry(domain="social_media", hours=3.0),
        ... ]
        >>> goals = [Goal(id="learn", name="Learn", domains=["learning"])]
        >>> calculate_distraction_ratio(entries, goals)
        60.0
    """
    return 100.0 - calculate_goal_alignment(time_entries, goals)


def calculate_actionability_score(
    consumed: int,
    bookmarked: int = 0,
    shared: int = 0,
    applied: int = 0,
    weights: ActionWeights | None = None,
) -> float:
    """Calculate actionability score from content consumption and actions.

    The Actionability Score measures how effectively consumed information
    translates into meaningful action. Higher scores indicate more
    action-oriented consumption.

    Formula:
        AS = (bookmarked * w_b + shared * w_s + applied * w_a) / consumed

        Default weights: w_b=0.3, w_s=0.5, w_a=1.0

    Args:
        consumed: Total items consumed (articles, videos, etc.).
        bookmarked: Items saved for later (default: 0).
        shared: Items shared with others (default: 0).
        applied: Items that led to concrete action (default: 0).
        weights: Custom ActionWeights (default: standard weights).

    Returns:
        Actionability score as a float (typically 0.0 to 1.0, can exceed 1.0).

    Example:
        >>> calculate_actionability_score(consumed=100, bookmarked=20, shared=5, applied=10)
        0.185
    """
    if consumed == 0:
        return 0.0

    # Use default weights if not provided
    if weights is None:
        from meaningful_metrics.schemas import ActionWeights

        weights = ActionWeights()

    weighted_actions = (
        bookmarked * weights.bookmarked
        + shared * weights.shared
        + applied * weights.applied
    )

    return weighted_actions / consumed


def calculate_actionability_score_from_log(
    action_log: ActionLog,
    weights: ActionWeights | None = None,
) -> float:
    """Calculate actionability score from an ActionLog object.

    Convenience function that unpacks an ActionLog and calls
    calculate_actionability_score.

    Args:
        action_log: ActionLog containing consumption and action data.
        weights: Custom ActionWeights (default: standard weights).

    Returns:
        Actionability score as a float.

    Example:
        >>> from meaningful_metrics.schemas import ActionLog
        >>> log = ActionLog(consumed=100, bookmarked=20, shared=5, applied=10)
        >>> calculate_actionability_score_from_log(log)
        0.185
    """
    return calculate_actionability_score(
        consumed=action_log.consumed,
        bookmarked=action_log.bookmarked,
        shared=action_log.shared,
        applied=action_log.applied,
        weights=weights,
    )


def calculate_locality_score(
    local_relevance: float,
    engagement: float,
) -> float:
    """Calculate locality score for community-relevant content.

    The Locality Score weights content by its relevance to the user's
    local community, multiplied by engagement level.

    Formula:
        LS = local_relevance * engagement

    Args:
        local_relevance: Relevance to local community (0.0 to 1.0).
        engagement: User's engagement with the content (0.0 to 1.0).

    Returns:
        Locality score as a float (0.0 to 1.0).

    Raises:
        ValueError: If inputs are outside valid range.

    Example:
        >>> calculate_locality_score(local_relevance=0.8, engagement=0.6)
        0.48
    """
    if not 0.0 <= local_relevance <= 1.0:
        msg = f"local_relevance must be between 0.0 and 1.0, got {local_relevance}"
        raise ValueError(msg)

    if not 0.0 <= engagement <= 1.0:
        msg = f"engagement must be between 0.0 and 1.0, got {engagement}"
        raise ValueError(msg)

    return local_relevance * engagement


def soft_min(a: float, b: float, alpha: float = 10.0) -> float:
    """Smooth approximation of min(a, b) for differentiable optimization.

    Uses the log-sum-exp trick to create a differentiable approximation
    of the minimum function. Useful for ML optimization where gradients
    are needed.

    Formula:
        soft_min(a, b) = -1/alpha * log(exp(-alpha * a) + exp(-alpha * b))

    Args:
        a: First value.
        b: Second value.
        alpha: Smoothing parameter (higher = closer to true min).

    Returns:
        Smooth approximation of min(a, b).

    Example:
        >>> soft_min(2.0, 3.0)  # Close to 2.0
        1.9999...
    """
    # Numerical stability: subtract max before exp
    max_val = max(-alpha * a, -alpha * b)
    return (
        -1
        / alpha
        * (
            max_val
            + math.log(math.exp(-alpha * a - max_val) + math.exp(-alpha * b - max_val))
        )
    )
