"""Tests for schema validation and data models."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

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


class TestGoal:
    """Tests for Goal schema."""

    def test_valid_goal(self) -> None:
        """Test creating a valid goal."""
        goal = Goal(
            id="learn-python",
            name="Learn Python",
            domains=["programming", "tutorials"],
            target_hours_per_week=5.0,
        )

        assert goal.id == "learn-python"
        assert goal.name == "Learn Python"
        assert goal.domains == ["programming", "tutorials"]
        assert goal.target_hours_per_week == 5.0

    def test_goal_without_target(self) -> None:
        """Test goal without target hours."""
        goal = Goal(
            id="learn",
            name="Learn",
            domains=["learning"],
        )

        assert goal.target_hours_per_week is None

    def test_goal_empty_domains(self) -> None:
        """Test goal with empty domains list."""
        goal = Goal(
            id="learn",
            name="Learn",
            domains=[],
        )

        assert goal.domains == []

    def test_goal_empty_id_fails(self) -> None:
        """Test that empty id fails validation."""
        with pytest.raises(ValidationError):
            Goal(id="", name="Learn", domains=[])

    def test_goal_negative_target_fails(self) -> None:
        """Test that negative target hours fails."""
        with pytest.raises(ValidationError):
            Goal(
                id="learn",
                name="Learn",
                domains=[],
                target_hours_per_week=-5.0,
            )


class TestDomainPriority:
    """Tests for DomainPriority schema."""

    def test_valid_priority(self) -> None:
        """Test creating a valid priority."""
        priority = DomainPriority(
            domain="learning",
            priority=0.8,
            max_daily_hours=4.0,
        )

        assert priority.domain == "learning"
        assert priority.priority == 0.8
        assert priority.max_daily_hours == 4.0

    def test_priority_without_cap(self) -> None:
        """Test priority without max hours cap."""
        priority = DomainPriority(
            domain="learning",
            priority=1.0,
        )

        assert priority.max_daily_hours is None

    def test_priority_bounds(self) -> None:
        """Test priority at boundary values."""
        min_priority = DomainPriority(domain="test", priority=0.0)
        max_priority = DomainPriority(domain="test", priority=1.0)

        assert min_priority.priority == 0.0
        assert max_priority.priority == 1.0

    def test_priority_out_of_range_fails(self) -> None:
        """Test that priority outside 0-1 fails."""
        with pytest.raises(ValidationError):
            DomainPriority(domain="test", priority=1.5)

        with pytest.raises(ValidationError):
            DomainPriority(domain="test", priority=-0.1)

    def test_zero_cap_fails(self) -> None:
        """Test that zero max hours fails."""
        with pytest.raises(ValidationError):
            DomainPriority(domain="test", priority=1.0, max_daily_hours=0.0)


class TestTimeEntry:
    """Tests for TimeEntry schema."""

    def test_valid_entry(self) -> None:
        """Test creating a valid time entry."""
        entry = TimeEntry(domain="learning", hours=2.5)

        assert entry.domain == "learning"
        assert entry.hours == 2.5

    def test_zero_hours(self) -> None:
        """Test entry with zero hours."""
        entry = TimeEntry(domain="learning", hours=0.0)

        assert entry.hours == 0.0

    def test_negative_hours_fails(self) -> None:
        """Test that negative hours fails validation."""
        with pytest.raises(ValidationError):
            TimeEntry(domain="learning", hours=-1.0)

    def test_empty_domain_fails(self) -> None:
        """Test that empty domain fails."""
        with pytest.raises(ValidationError):
            TimeEntry(domain="", hours=1.0)


class TestActionLog:
    """Tests for ActionLog schema."""

    def test_valid_log(self) -> None:
        """Test creating a valid action log."""
        log = ActionLog(
            consumed=100,
            bookmarked=20,
            shared=5,
            applied=10,
        )

        assert log.consumed == 100
        assert log.bookmarked == 20
        assert log.shared == 5
        assert log.applied == 10

    def test_defaults(self) -> None:
        """Test action log with defaults."""
        log = ActionLog(consumed=50)

        assert log.consumed == 50
        assert log.bookmarked == 0
        assert log.shared == 0
        assert log.applied == 0

    def test_negative_values_fail(self) -> None:
        """Test that negative values fail."""
        with pytest.raises(ValidationError):
            ActionLog(consumed=-1)


class TestActionWeights:
    """Tests for ActionWeights schema."""

    def test_defaults(self) -> None:
        """Test default weights."""
        weights = ActionWeights()

        assert weights.bookmarked == 0.3
        assert weights.shared == 0.5
        assert weights.applied == 1.0

    def test_custom_weights(self) -> None:
        """Test custom weights."""
        weights = ActionWeights(
            bookmarked=0.5,
            shared=0.7,
            applied=2.0,
        )

        assert weights.bookmarked == 0.5
        assert weights.shared == 0.7
        assert weights.applied == 2.0


class TestDomainMetrics:
    """Tests for DomainMetrics schema."""

    def test_valid_metrics(self) -> None:
        """Test creating valid domain metrics."""
        metrics = DomainMetrics(
            domain="learning",
            time_spent=3.0,
            effective_time=2.0,
            priority=1.0,
            contribution=2.0,
        )

        assert metrics.domain == "learning"
        assert metrics.time_spent == 3.0
        assert metrics.effective_time == 2.0
        assert metrics.priority == 1.0
        assert metrics.contribution == 2.0


class TestRecommendation:
    """Tests for Recommendation schema."""

    def test_valid_recommendation(self) -> None:
        """Test creating a valid recommendation."""
        rec = Recommendation(
            type="increase",
            domain="learning",
            message="Spend more time learning.",
            priority="high",
        )

        assert rec.type == "increase"
        assert rec.domain == "learning"
        assert rec.priority == "high"

    def test_valid_types(self) -> None:
        """Test all valid recommendation types."""
        for rec_type in ["increase", "decrease", "maintain"]:
            rec = Recommendation(
                type=rec_type,
                domain="test",
                message="Test message",
                priority="medium",
            )
            assert rec.type == rec_type

    def test_invalid_type_fails(self) -> None:
        """Test that invalid type fails."""
        with pytest.raises(ValidationError):
            Recommendation(
                type="invalid",
                domain="test",
                message="Test",
                priority="high",
            )


class TestMetricsReport:
    """Tests for MetricsReport schema."""

    def test_valid_report(self) -> None:
        """Test creating a valid report."""
        report = MetricsReport(
            period="daily",
            quality_time_score=6.0,
            raw_time_hours=8.0,
            goal_alignment_percent=50.0,
            distraction_percent=50.0,
            actionability_score=0.2,
            by_domain=[],
            recommendations=[],
        )

        assert report.period == "daily"
        assert report.quality_time_score == 6.0

    def test_defaults(self) -> None:
        """Test report with defaults."""
        report = MetricsReport(
            period="weekly",
            quality_time_score=10.0,
            raw_time_hours=20.0,
            goal_alignment_percent=40.0,
            distraction_percent=60.0,
        )

        assert report.actionability_score == 0.0
        assert report.by_domain == []
        assert report.recommendations == []

    def test_alignment_bounds(self) -> None:
        """Test goal alignment bounds."""
        with pytest.raises(ValidationError):
            MetricsReport(
                period="daily",
                quality_time_score=1.0,
                raw_time_hours=1.0,
                goal_alignment_percent=150.0,  # Invalid
                distraction_percent=0.0,
            )
