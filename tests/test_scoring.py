"""Tests for composite scoring and report generation functions."""

from __future__ import annotations

import pytest

from meaningful_metrics.schemas import (
    ActionLog,
    DomainPriority,
    Goal,
    TimeEntry,
)
from meaningful_metrics.scoring import (
    calculate_domain_contributions,
    generate_metrics_report,
    generate_recommendations,
)


class TestDomainContributions:
    """Tests for calculate_domain_contributions function."""

    def test_basic_contributions(self) -> None:
        """Test basic domain contribution calculation."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
            TimeEntry(domain="work", hours=5.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
            DomainPriority(domain="work", priority=0.8),
        ]

        contributions = calculate_domain_contributions(entries, priorities)

        assert len(contributions) == 2

        learning = next(c for c in contributions if c.domain == "learning")
        assert learning.time_spent == pytest.approx(2.0)
        assert learning.effective_time == pytest.approx(2.0)
        assert learning.priority == pytest.approx(1.0)
        assert learning.contribution == pytest.approx(2.0)

        work = next(c for c in contributions if c.domain == "work")
        assert work.time_spent == pytest.approx(5.0)
        assert work.effective_time == pytest.approx(5.0)
        assert work.priority == pytest.approx(0.8)
        assert work.contribution == pytest.approx(4.0)

    def test_capped_contributions(self) -> None:
        """Test domain contributions with caps applied."""
        entries = [
            TimeEntry(domain="learning", hours=5.0),  # Over cap
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0, max_daily_hours=3.0),
        ]

        contributions = calculate_domain_contributions(entries, priorities)

        assert len(contributions) == 1
        learning = contributions[0]
        assert learning.time_spent == pytest.approx(5.0)  # Raw time
        assert learning.effective_time == pytest.approx(3.0)  # Capped
        assert learning.contribution == pytest.approx(3.0)  # 3.0 * 1.0

    def test_default_priority(self) -> None:
        """Test that unknown domains get default priority."""
        entries = [
            TimeEntry(domain="unknown", hours=2.0),
        ]
        priorities: list[DomainPriority] = []

        contributions = calculate_domain_contributions(
            entries, priorities, default_priority=0.5
        )

        assert len(contributions) == 1
        assert contributions[0].priority == pytest.approx(0.5)
        assert contributions[0].contribution == pytest.approx(1.0)  # 2.0 * 0.5


class TestGenerateRecommendations:
    """Tests for generate_recommendations function."""

    def test_low_alignment_recommendation(self) -> None:
        """Test that low goal alignment triggers recommendation."""
        entries = [
            TimeEntry(domain="social_media", hours=8.0),
            TimeEntry(domain="learning", hours=1.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
            DomainPriority(domain="social_media", priority=0.2),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        recommendations = generate_recommendations(
            entries, priorities, goals, goal_alignment=11.1
        )

        # Should recommend increasing goal-related activity
        increase_recs = [r for r in recommendations if r.type == "increase"]
        assert len(increase_recs) > 0
        assert any("alignment" in r.message.lower() for r in increase_recs)

    def test_over_cap_recommendation(self) -> None:
        """Test that exceeding cap triggers recommendation."""
        entries = [
            TimeEntry(domain="social_media", hours=3.0),  # Over 1h cap
        ]
        priorities = [
            DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
        ]
        goals: list[Goal] = []

        recommendations = generate_recommendations(
            entries, priorities, goals, goal_alignment=50.0
        )

        # Should recommend decreasing time
        decrease_recs = [r for r in recommendations if r.type == "decrease"]
        assert len(decrease_recs) > 0
        assert any("cap" in r.message.lower() for r in decrease_recs)

    def test_low_priority_high_time_recommendation(self) -> None:
        """Test that low priority + high time triggers recommendation."""
        entries = [
            TimeEntry(domain="social_media", hours=5.0),  # Low priority, high time
        ]
        priorities = [
            DomainPriority(domain="social_media", priority=0.2),
        ]
        goals: list[Goal] = []

        recommendations = generate_recommendations(
            entries, priorities, goals, goal_alignment=50.0
        )

        # Should recommend reducing low-priority time
        decrease_recs = [r for r in recommendations if r.type == "decrease"]
        assert len(decrease_recs) > 0

    def test_positive_reinforcement(self) -> None:
        """Test that high alignment gets positive recommendation."""
        entries = [
            TimeEntry(domain="learning", hours=5.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        recommendations = generate_recommendations(
            entries, priorities, goals, goal_alignment=100.0
        )

        # Should have a positive "maintain" recommendation
        maintain_recs = [r for r in recommendations if r.type == "maintain"]
        assert len(maintain_recs) > 0
        assert any(
            "great" in r.message.lower() or "good" in r.message.lower()
            for r in maintain_recs
        )


class TestGenerateMetricsReport:
    """Tests for generate_metrics_report function."""

    def test_complete_report(self) -> None:
        """Test generating a complete metrics report."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
            TimeEntry(domain="work", hours=5.0),
            TimeEntry(domain="social_media", hours=1.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0, max_daily_hours=4.0),
            DomainPriority(domain="work", priority=0.8),
            DomainPriority(domain="social_media", priority=0.2, max_daily_hours=1.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]
        actions = ActionLog(consumed=50, bookmarked=10, shared=3, applied=5)

        report = generate_metrics_report(
            time_entries=entries,
            priorities=priorities,
            goals=goals,
            actions=actions,
            period="daily",
        )

        # Check all fields are populated
        assert report.period == "daily"
        assert report.raw_time_hours == pytest.approx(8.0)

        # QTS = 2*1.0 + 5*0.8 + 1*0.2 = 2 + 4 + 0.2 = 6.2
        assert report.quality_time_score == pytest.approx(6.2)

        # Goal alignment = 2/8 * 100 = 25%
        assert report.goal_alignment_percent == pytest.approx(25.0)
        assert report.distraction_percent == pytest.approx(75.0)

        # Actionability = (10*0.3 + 3*0.5 + 5*1.0) / 50 = 9.5/50 = 0.19
        assert report.actionability_score == pytest.approx(0.19)

        # Check domain breakdown
        assert len(report.by_domain) == 3

        # Check recommendations exist
        assert isinstance(report.recommendations, list)

    def test_report_without_actions(self) -> None:
        """Test report generation without action log."""
        entries = [
            TimeEntry(domain="learning", hours=2.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
        ]
        goals = [
            Goal(id="learn", name="Learn", domains=["learning"]),
        ]

        report = generate_metrics_report(
            time_entries=entries,
            priorities=priorities,
            goals=goals,
            actions=None,  # No action log
        )

        assert report.actionability_score == pytest.approx(0.0)

    def test_weekly_period(self) -> None:
        """Test report with weekly period."""
        entries = [
            TimeEntry(domain="learning", hours=10.0),
        ]
        priorities = [
            DomainPriority(domain="learning", priority=1.0),
        ]
        goals: list[Goal] = []

        report = generate_metrics_report(
            time_entries=entries,
            priorities=priorities,
            goals=goals,
            period="weekly",
        )

        assert report.period == "weekly"

    def test_empty_entries(self) -> None:
        """Test report with no time entries."""
        entries: list[TimeEntry] = []
        priorities: list[DomainPriority] = []
        goals: list[Goal] = []

        report = generate_metrics_report(
            time_entries=entries,
            priorities=priorities,
            goals=goals,
        )

        assert report.raw_time_hours == pytest.approx(0.0)
        assert report.quality_time_score == pytest.approx(0.0)
        assert report.goal_alignment_percent == pytest.approx(0.0)
        assert len(report.by_domain) == 0
