"""Generate benchmark visualization figures for Meaningful Metrics.

This script reads results/metrics.json and produces publication-quality
charts in results/figures/.

Usage:
    python results/generate_figures.py
"""

from __future__ import annotations

import json
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
except ImportError:
    print("matplotlib is required: pip install matplotlib")
    raise SystemExit(1)


def load_results() -> dict:
    """Load benchmark results from metrics.json."""
    results_path = Path(__file__).parent / "metrics.json"
    with results_path.open() as f:
        return json.load(f)


def plot_profile_comparison(data: dict) -> None:
    """Create a grouped bar chart comparing profiles across key metrics."""
    profiles = data["profiles"]
    names = [p["name"].replace("_", "\n") for p in profiles]

    qts = [p["results"]["quality_time_score"] for p in profiles]
    alignment = [p["results"]["goal_alignment_percent"] for p in profiles]
    actionability = [p["results"]["actionability_score"] * 100 for p in profiles]

    x = range(len(names))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 6))

    bars1 = ax.bar([i - width for i in x], qts, width, label="Quality Time Score", color="#2196F3")
    bars2 = ax.bar(x, alignment, width, label="Goal Alignment (%)", color="#4CAF50")
    bars3 = ax.bar([i + width for i in x], actionability, width, label="Actionability (x100)", color="#FF9800")

    ax.set_xlabel("User Profile", fontsize=12)
    ax.set_ylabel("Score", fontsize=12)
    ax.set_title("Meaningful Metrics: Profile Comparison", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10)
    ax.legend(fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(0, 105)

    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"{height:.1f}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    plt.tight_layout()
    fig.savefig(Path(__file__).parent / "figures" / "profile_comparison.png", dpi=150)
    plt.close(fig)
    print("Saved: results/figures/profile_comparison.png")


def plot_diminishing_returns(data: dict) -> None:
    """Show the effect of diminishing returns caps on QTS contribution."""
    fig, ax = plt.subplots(figsize=(10, 6))

    hours = [i * 0.5 for i in range(21)]  # 0 to 10 hours
    caps = [2.0, 4.0, 6.0, None]
    priority = 1.0
    colors = ["#E91E63", "#9C27B0", "#2196F3", "#4CAF50"]
    labels = ["Cap: 2h", "Cap: 4h", "Cap: 6h", "No cap"]

    for cap, color, label in zip(caps, colors, labels):
        contributions = []
        for h in hours:
            effective = min(h, cap) if cap is not None else h
            contributions.append(effective * priority)
        ax.plot(hours, contributions, linewidth=2, color=color, label=label)

    ax.set_xlabel("Hours Spent", fontsize=12)
    ax.set_ylabel("QTS Contribution", fontsize=12)
    ax.set_title("Diminishing Returns: How Caps Affect Quality Time Score", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)

    plt.tight_layout()
    fig.savefig(Path(__file__).parent / "figures" / "diminishing_returns.png", dpi=150)
    plt.close(fig)
    print("Saved: results/figures/diminishing_returns.png")


def plot_domain_breakdown(data: dict) -> None:
    """Create stacked bar chart showing domain contributions per profile."""
    profiles = data["profiles"]
    names = [p["name"].replace("_", "\n") for p in profiles]

    all_domains: set[str] = set()
    for p in profiles:
        all_domains.update(p["results"]["domain_breakdown"].keys())
    domains = sorted(all_domains)

    colors = {
        "learning": "#4CAF50",
        "work": "#2196F3",
        "deep_work": "#1565C0",
        "social_media": "#F44336",
        "exercise": "#FF9800",
        "entertainment": "#9C27B0",
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    bottoms = [0.0] * len(profiles)
    for domain in domains:
        values = []
        for p in profiles:
            breakdown = p["results"]["domain_breakdown"]
            values.append(breakdown.get(domain, {}).get("contribution", 0))
        color = colors.get(domain, "#757575")
        ax.bar(names, values, bottom=bottoms, label=domain.replace("_", " ").title(), color=color)
        bottoms = [b + v for b, v in zip(bottoms, values)]

    ax.set_xlabel("User Profile", fontsize=12)
    ax.set_ylabel("QTS Contribution", fontsize=12)
    ax.set_title("Domain Contributions to Quality Time Score", fontsize=14, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig.savefig(Path(__file__).parent / "figures" / "domain_breakdown.png", dpi=150)
    plt.close(fig)
    print("Saved: results/figures/domain_breakdown.png")


if __name__ == "__main__":
    data = load_results()
    plot_profile_comparison(data)
    plot_diminishing_returns(data)
    plot_domain_breakdown(data)
    print("All figures generated successfully.")
