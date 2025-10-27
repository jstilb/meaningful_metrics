# Meaningful Metrics

Meaningful Metrics is an open-source initiative for creating metrics that help people and organizations build ethical, human-centered products. Instead of optimizing for vanity numbers like raw watch time or ad impressions, we collect and design measures that reward products for empowering, educating, and respecting the humans who use them. As AI systems become core to digital experiences, our mission also includes developing evaluation frameworks that hold intelligent products accountable to the same human-first standards.

## Vision

Modern data products influence how people learn, work, socialize, and make decisions. We believe metrics should reinforce positive behaviors—encouraging depth over distraction, action over passivity, and wellbeing over addiction. This repository is a collaborative space where practitioners, researchers, and product teams can co-create metrics that align business success with human flourishing.

## Core Principles

- **Human impact first** – Metrics should describe the benefit to people, not just the product or business.
- **Actionable and measurable** – Each metric must be grounded in data that can be collected responsibly and acted upon.
- **Right-sized engagement** – Reward sustained, purposeful use and discourage harmful overuse or binge behavior.
- **Transparency and accountability** – Document assumptions, potential harms, and validation steps so teams can implement responsibly.
- **Collaborative stewardship** – We value open dialogue, iteration, and evidence-based improvements from the community.

## Repository Structure

```
.
├── docs/
│   ├── metric_template.md   # Guidance for drafting a new metric proposal
│   └── eval_template.md     # Checklist for designing a responsible AI evaluation
├── metrics/
│   └── examples/            # Sample metric submissions
├── evals/
│   └── examples/            # Sample AI evaluation playbooks
├── CONTRIBUTING.md          # How to participate
├── CODE_OF_CONDUCT.md       # Community expectations
└── README.md                # Project overview
```

## Getting Started

1. **Explore the metric examples** in [`metrics/examples`](metrics/examples/) and the AI evaluation examples in [`evals/examples`](evals/examples/) to understand the level of depth we expect.
2. **Use the templates** in [`docs/metric_template.md`](docs/metric_template.md) or [`docs/eval_template.md`](docs/eval_template.md) to frame your idea. Focus on who benefits, why it matters, and how to measure success responsibly.
3. **Discuss big ideas** by opening a GitHub issue tagged with `discussion` before submitting major proposals. Early collaboration helps align on scope and ethics.
4. **Submit a pull request** following the steps in [CONTRIBUTING.md](CONTRIBUTING.md). We review submissions for clarity, measurability, and ethical alignment.

## What Makes a Metric "Meaningful"?

A good submission should include:

- **Intent** – What human outcome are we promoting or protecting?
- **Signals** – Which qualitative or quantitative inputs reflect that outcome?
- **Incentives** – How will this metric change product decisions compared to traditional success measures?
- **Guardrails** – What thresholds or tapering effects prevent negative side effects?
- **Validation** – How can we verify the metric works and surfaces what we intend?

## Example Highlights

- [`engaged_learning_time`](metrics/examples/engaged_learning_time.md) balances time spent with demonstrated skill growth and reflective breaks, rewarding focused learning over endless consumption.
- [`actionable_recommendation_rate`](metrics/examples/actionable_recommendation_rate.md) encourages recommendation systems to surface content that viewers can act on within their current goals, discouraging passive binge-watching loops.

## AI Evaluation Playbooks for Ethical Businesses

AI-native organizations need evaluation suites that connect model performance with the human outcomes promised in their mission statements. Explore the detailed playbooks in [`evals/examples`](evals/examples/) for in-depth guidance on designing and governing AI evals programs that uphold ethical business practices:

- [`trust_centered_deployment_review`](evals/examples/trust_centered_deployment_review.md) pairs disclosure and consent audits with cross-functional reviews before expanding conversational AI deployments.
- [`impact_equity_monitor`](evals/examples/impact_equity_monitor.md) operationalizes fairness metrics, qualitative harm assessments, and mitigation follow-up plans for ranking and risk-scoring models.
- [`sustainable_automation_scorecard`](evals/examples/sustainable_automation_scorecard.md) measures how automation affects employee wellbeing, oversight quality, and environmental sustainability.

Each playbook documents collection methods, review cadences, and responsible owners so that teams can iterate transparently. Contributors are encouraged to submit additional AI eval examples tailored to their industries—especially those that surface long-term human and societal impacts.

## Community

Meaningful Metrics is maintained by volunteers who believe ethical design should be the default. We welcome contributors from product, research, design, policy, and lived-experience backgrounds. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

If you use these metrics—or improve upon them—let us know! Sharing learnings helps us collectively build better products.

## License

This project is available under the [MIT License](LICENSE).
