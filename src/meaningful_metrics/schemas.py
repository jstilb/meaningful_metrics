"""Data models for Meaningful Metrics.

This module defines all input and output types used by the metrics library.
Types are defined using Pydantic for runtime validation and TypedDict for
lightweight type hints.

Input Types:
    - Goal: A user's goal with linked domains
    - DomainPriority: Priority and cap settings for a domain
    - TimeEntry: Time spent in a domain
    - ActionLog: Log of actions taken on consumed content
    - ActionWeights: Custom weights for actionability calculation

Output Types:
    - DomainMetrics: Metrics for a single domain
    - Recommendation: A suggested action for the user
    - MetricsReport: Complete metrics report
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, ValidationInfo, field_validator


# =============================================================================
# Input Types
# =============================================================================


class Goal(BaseModel):
    """A user's goal with linked content domains.

    Goals define what the user wants to achieve and which content domains
    support that goal. This is used to calculate Goal Alignment.

    Attributes:
        id: Unique identifier for the goal.
        name: Human-readable name for the goal.
        domains: List of content domains that support this goal.
        target_hours_per_week: Optional weekly time target for this goal.

    Example:
        >>> goal = Goal(
        ...     id="learn-spanish",
        ...     name="Learn Spanish",
        ...     domains=["language_learning", "spanish_media"],
        ...     target_hours_per_week=7.0,
        ... )
    """

    id: str = Field(..., min_length=1, description="Unique identifier for the goal")
    name: str = Field(..., min_length=1, description="Human-readable goal name")
    domains: list[str] = Field(
        default_factory=list,
        description="Content domains that support this goal",
    )
    target_hours_per_week: float | None = Field(
        default=None,
        ge=0,
        description="Optional weekly time target in hours",
    )


class DomainPriority(BaseModel):
    """Priority and cap settings for a content domain.

    Domain priorities weight time spent in different activities according
    to user preferences. The optional cap implements diminishing returns.

    Attributes:
        domain: The content domain identifier (e.g., "learning", "social_media").
        priority: Priority weight from 0.0 (lowest) to 1.0 (highest).
        max_daily_hours: Optional cap for diminishing returns.

    Example:
        >>> priority = DomainPriority(
        ...     domain="learning",
        ...     priority=1.0,
        ...     max_daily_hours=4.0,
        ... )
    """

    domain: str = Field(..., min_length=1, description="Content domain identifier")
    priority: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Priority weight (0.0 to 1.0)",
    )
    max_daily_hours: float | None = Field(
        default=None,
        gt=0,
        description="Maximum valuable hours per day (diminishing returns cap)",
    )

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, v: float) -> float:
        """Ensure priority is within valid range."""
        if not 0.0 <= v <= 1.0:
            msg = "Priority must be between 0.0 and 1.0"
            raise ValueError(msg)
        return v


class TimeEntry(BaseModel):
    """Time spent in a content domain.

    Represents tracked time for metric calculations.

    Attributes:
        domain: The content domain identifier.
        hours: Time spent in hours (must be non-negative).

    Example:
        >>> entry = TimeEntry(domain="learning", hours=2.5)
    """

    domain: str = Field(..., min_length=1, description="Content domain identifier")
    hours: float = Field(..., ge=0, description="Time spent in hours")

    @field_validator("hours")
    @classmethod
    def validate_hours(cls, v: float) -> float:
        """Ensure hours is non-negative."""
        if v < 0:
            msg = "Hours cannot be negative"
            raise ValueError(msg)
        return v


class ActionLog(BaseModel):
    """Log of actions taken on consumed content.

    Used to calculate the Actionability Score.

    Attributes:
        consumed: Total items consumed (articles, videos, etc.).
        bookmarked: Items saved for later.
        shared: Items shared with others.
        applied: Items that led to concrete action.

    Example:
        >>> log = ActionLog(consumed=100, bookmarked=20, shared=5, applied=10)
    """

    consumed: int = Field(..., ge=0, description="Total items consumed")
    bookmarked: int = Field(default=0, ge=0, description="Items saved for later")
    shared: int = Field(default=0, ge=0, description="Items shared with others")
    applied: int = Field(default=0, ge=0, description="Items that led to action")

    @field_validator("bookmarked", "shared", "applied")
    @classmethod
    def validate_not_exceeds_consumed(cls, v: int, info: ValidationInfo) -> int:
        """Warn if action count seems high relative to consumed."""
        # Note: This is a soft validation - items can be acted on multiple ways
        return v


class ActionWeights(BaseModel):
    """Custom weights for actionability score calculation.

    Allows users to customize the relative importance of different actions.

    Attributes:
        bookmarked: Weight for bookmarked items (default: 0.3).
        shared: Weight for shared items (default: 0.5).
        applied: Weight for applied items (default: 1.0).

    Example:
        >>> weights = ActionWeights(bookmarked=0.2, shared=0.4, applied=1.5)
    """

    bookmarked: float = Field(default=0.3, ge=0, description="Weight for bookmarks")
    shared: float = Field(default=0.5, ge=0, description="Weight for shares")
    applied: float = Field(default=1.0, ge=0, description="Weight for applications")


# =============================================================================
# Output Types
# =============================================================================


class DomainMetrics(BaseModel):
    """Metrics for a single content domain.

    Provides detailed breakdown of how a domain contributes to overall metrics.

    Attributes:
        domain: The content domain identifier.
        time_spent: Raw time spent in hours.
        effective_time: Time after applying diminishing returns cap.
        priority: The domain's priority weight.
        contribution: Contribution to Quality Time Score.
    """

    domain: str = Field(..., description="Content domain identifier")
    time_spent: float = Field(..., ge=0, description="Raw time spent in hours")
    effective_time: float = Field(
        ...,
        ge=0,
        description="Time after diminishing returns cap",
    )
    priority: float = Field(..., ge=0, le=1, description="Domain priority weight")
    contribution: float = Field(..., ge=0, description="Contribution to QTS")


class Recommendation(BaseModel):
    """A suggested action for the user.

    Recommendations are generated based on metrics analysis to help
    users improve their time allocation.

    Attributes:
        type: Whether to increase, decrease, or maintain time in domain.
        domain: The content domain this recommendation applies to.
        message: Human-readable recommendation message.
        priority: Importance level of this recommendation.
    """

    type: Literal["increase", "decrease", "maintain"] = Field(
        ...,
        description="Action type",
    )
    domain: str = Field(..., description="Target content domain")
    message: str = Field(..., description="Human-readable recommendation")
    priority: Literal["high", "medium", "low"] = Field(
        ...,
        description="Recommendation importance",
    )


class MetricsReport(BaseModel):
    """Complete metrics report for a time period.

    Aggregates all metrics and provides actionable recommendations.

    Attributes:
        period: The reporting period (daily or weekly).
        quality_time_score: The calculated QTS.
        raw_time_hours: Total raw time tracked.
        goal_alignment_percent: Percentage of time on goal-related activities.
        distraction_percent: Percentage of time on non-goal activities.
        actionability_score: Information to action conversion rate.
        by_domain: Breakdown of metrics by domain.
        recommendations: Suggested actions for improvement.
    """

    period: Literal["daily", "weekly"] = Field(..., description="Reporting period")
    quality_time_score: float = Field(..., ge=0, description="Quality Time Score")
    raw_time_hours: float = Field(..., ge=0, description="Total raw time in hours")
    goal_alignment_percent: float = Field(
        ...,
        ge=0,
        le=100,
        description="Goal alignment percentage",
    )
    distraction_percent: float = Field(
        ...,
        ge=0,
        le=100,
        description="Distraction percentage",
    )
    actionability_score: float = Field(
        default=0.0,
        ge=0,
        description="Actionability score",
    )
    by_domain: list[DomainMetrics] = Field(
        default_factory=list,
        description="Per-domain metrics",
    )
    recommendations: list[Recommendation] = Field(
        default_factory=list,
        description="Improvement recommendations",
    )
