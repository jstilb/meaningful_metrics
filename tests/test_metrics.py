"""Tests for core metric calculation functions.

These tests verify the mathematical correctness of the Meaningful Metrics
formulas and edge case handling.
"""

from __future__ import annotations

import pytest

from meaningful_metrics.metrics import (
    calculate_actionability_score,
    calculate_distraction_ratio,
    calculate_goal_alignment,
    calculate_locality_score,
    calculate_quality_time_score,
    soft_min,
)
from meaningful_metrics.schemas import (
    ActionWeights,
    DomainPriority,
    Goal,
    TimeEntry,
)


class TestQualityTimeScore:
    """Tests for calculate_quality_time_score function."""

    def test_basic_calculation(self) -> None:
        """Test basic QTS calculation without caps."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
            TimeEntry(domain="work", hours=5.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
            DomainPriority(domain="work", priority=0.8),
        ]

        qts = calculate_quality_time_score(entries, priorities)

        # QTS = 2.0 * 1.0 + 5.0 * 0.8 = 2.0 + 4.0 = 6.0
        assert qts == pytest.approx(6.0)

    def test_with_diminishing_returns_cap(self) -> None:
        """Test QTS calculation with diminishing returns caps."""
        entries = [
            TimeEntry(domain="learning", hours=5.0),  # Over cap
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0, max_daily_hours=3.0),
        ]

        qts = calculate_quality_time_score(entries, priorities)

        # Capped at 3.0 hours: QTS = min(5.0, 3.0) * 1.0 = 3.0
        assert qts == pytest.approx(3.0)

    def test_under_cap(self) -> None:
        """Test QTS when time is under the cap."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),  # Under cap
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
        ]

        qts = calculate_quality_time_score(entries, priorities)

        # Under cap, use actual time: QTS = 2.0 * 1.0 = 2.0
        assert qts == pytest.approx(2.0)

    def test_default_priority_for_unknown_domain(self) -> None:
        """Test that unknown domains get default priority."""
        entries = [
            TimeEntry(domain="unknown_domain", hours=2.0),
        ]
        priorities = []  # No priorities defined

        qts = calculate_quality_time_score(entries, priorities, default_priority=0.5)

        # Default priority 0.5: QTS = 2.0 * 0.5 = 1.0
        assert qts == pytest.approx(1.0)

    def test_zero_time(self) -> None:
        """Test QTS with zero time entries."""
        entries = [
            TimeEntry(domain="learning", hours=0.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
        ]

        qts = calculate_quality_time_score(entries, priorities)

        assert qts == pytest.approx(0.0)

    def test_empty_entries(self) -> None:
        """Test QTS with no time entries."""
        entries: list[TimeEntry] = []
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
        ]

        qts = calculate_quality_time_score(entries, priorities)

        assert qts == pytest.approx(0.0)

    def test_multiple_domains_mixed_caps(self) -> None:
        """Test QTS with multiple domains, some capped, some not."""
        entries = [
            TimeEntry(domain="learning", hours=3.0),  # Capped at 2.0
            TimeEntry(domain="work", hours=6.0),  # No cap
            TimeEntry(domain="social_media", hours=2.0),  # Capped at 1.0
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0, max_daily_hours=2.0),
            DomainPriority(domain="work", priority=0.8),
            DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
        ]

        qts = calculate_quality_time_score(entries, priorities)

        # QTS = min(3,2)*1.0 + 6*0.8 + min(2,1)*0.2 = 2.0 + 4.8 + 0.2 = 7.0
        assert qts == pytest.approx(7.0)


class TestGoalAlignment:
    """Tests for calculate_goal_alignment function."""

    def test_full_alignment(self) -> None:
        """Test 100% goal alignment."""
        entries = [
            TimeEntry(domain="learning", hours=5.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        alignment = calculate_goal_alignment(entries, goals)

        assert alignment == pytest.approx(100.0)

    def test_no_alignment(self) -> None:
        """Test 0% goal alignment."""
        entries = [
            TimeEntry(domain="social_media", hours=5.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        alignment = calculate_goal_alignment(entries, goals)

        assert alignment == pytest.approx(0.0)

    def test_partial_alignment(self) -> None:
        """Test partial goal alignment."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
            TimeEntry(domain="social_media", hours=3.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        alignment = calculate_goal_alignment(entries, goals)

        # 2 / 5 * 100 = 40%
        assert alignment == pytest.approx(40.0)

    def test_multiple_goals(self) -> None:
        """Test alignment with multiple goals."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
            TimeEntry(domain="exercise", hours=1.0),
            TimeEntry(domain="social_media", hours=2.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
            Goal(id="fitness", name="Get Fit", domains=["exercise"]),
        ]

        alignment = calculate_goal_alignment(entries, goals)

        # (2 + 1) / 5 * 100 = 60%
        assert alignment == pytest.approx(60.0)

    def test_empty_entries(self) -> None:
        """Test alignment with no time entries."""
        entries: list[TimeEntry] = []
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        alignment = calculate_goal_alignment(entries, goals)

        assert alignment == pytest.approx(0.0)

    def test_no_goals(self) -> None:
        """Test alignment with no goals defined."""
        entries = [
            TimeEntry(domain="learning", hours=5.0),
        ]
        goals: list[Goal] = []

        alignment = calculate_goal_alignment(entries, goals)

        # No goals = nothing can be aligned
        assert alignment == pytest.approx(0.0)


class TestDistractionRatio:
    """Tests for calculate_distraction_ratio function."""

    def test_inverse_of_alignment(self) -> None:
        """Test that distraction ratio is inverse of alignment."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
            TimeEntry(domain="social_media", hours=3.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        alignment = calculate_goal_alignment(entries, goals)
        distraction = calculate_distraction_ratio(entries, goals)

        assert alignment + distraction == pytest.approx(100.0)

    def test_full_distraction(self) -> None:
        """Test 100% distraction."""
        entries = [
            TimeEntry(domain="social_media", hours=5.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        distraction = calculate_distraction_ratio(entries, goals)

        assert distraction == pytest.approx(100.0)

    def test_no_distraction(self) -> None:
        """Test 0% distraction."""
        entries = [
            TimeEntry(domain="learning", hours=5.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        distraction = calculate_distraction_ratio(entries, goals)

        assert distraction == pytest.approx(0.0)


class TestActionabilityScore:
    """Tests for calculate_actionability_score function."""

    def test_basic_calculation(self) -> None:
        """Test basic actionability calculation."""
        score = calculate_actionability_score(
            consumed=100,
            bookmarked=20,
            shared=5,
            applied=10,
        )

        # (20*0.3 + 5*0.5 + 10*1.0) / 100 = (6 + 2.5 + 10) / 100 = 0.185
        assert score == pytest.approx(0.185)

    def test_zero_consumption(self) -> None:
        """Test actionability with zero consumption."""
        score = calculate_actionability_score(consumed=0, applied=10)

        assert score == pytest.approx(0.0)

    def test_custom_weights(self) -> None:
        """Test actionability with custom weights."""
        weights = ActionWeights(bookmarked=0.5, shared=0.5, applied=2.0)
        score = calculate_actionability_score(
            consumed=100,
            bookmarked=10,
            shared=10,
            applied=10,
            weights=weights,
        )

        # (10*0.5 + 10*0.5 + 10*2.0) / 100 = (5 + 5 + 20) / 100 = 0.3
        assert score == pytest.approx(0.3)

    def test_only_applied(self) -> None:
        """Test actionability with only applied actions."""
        score = calculate_actionability_score(
            consumed=50,
            applied=10,
        )

        # (10*1.0) / 50 = 0.2
        assert score == pytest.approx(0.2)


class TestLocalityScore:
    """Tests for calculate_locality_score function."""

    def test_basic_calculation(self) -> None:
        """Test basic locality score calculation."""
        score = calculate_locality_score(
            local_relevance=0.8,
            engagement=0.6,
        )

        assert score == pytest.approx(0.48)

    def test_zero_relevance(self) -> None:
        """Test locality with zero relevance."""
        score = calculate_locality_score(
            local_relevance=0.0,
            engagement=1.0,
        )

        assert score == pytest.approx(0.0)

    def test_full_values(self) -> None:
        """Test locality with maximum values."""
        score = calculate_locality_score(
            local_relevance=1.0,
            engagement=1.0,
        )

        assert score == pytest.approx(1.0)

    def test_invalid_relevance(self) -> None:
        """Test that invalid relevance raises error."""
        with pytest.raises(ValueError, match="local_relevance"):
            calculate_locality_score(local_relevance=1.5, engagement=0.5)

    def test_invalid_engagement(self) -> None:
        """Test that invalid engagement raises error."""
        with pytest.raises(ValueError, match="engagement"):
            calculate_locality_score(local_relevance=0.5, engagement=-0.1)


class TestSoftMin:
    """Tests for soft_min approximation function."""

    def test_approximates_min(self) -> None:
        """Test that soft_min approximates min function."""
        result = soft_min(2.0, 5.0, alpha=10.0)

        # Should be close to 2.0
        assert result == pytest.approx(2.0, abs=0.01)

    def test_symmetric(self) -> None:
        """Test that soft_min is symmetric."""
        result1 = soft_min(2.0, 5.0)
        result2 = soft_min(5.0, 2.0)

        assert result1 == pytest.approx(result2)

    def test_equal_values(self) -> None:
        """Test soft_min with equal values."""
        result = soft_min(3.0, 3.0)

        # Should be close to 3.0 (slightly less due to log-sum-exp)
        assert result == pytest.approx(3.0, abs=0.1)
