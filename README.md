# Meaningful Metrics

[![CI](https://github.com/jstilb/meaningful_metrics/actions/workflows/ci.yml/badge.svg)](https://github.com/jstilb/meaningful_metrics/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
│   ├── metric_template.md     # Guidance for drafting a new metric proposal
│   ├── eval_template.md       # Checklist for designing a responsible AI evaluation
│   └── toolkit/               # Reusable validation and governance assets
├── metrics/
│   └── examples/              # Sample metric submissions across domains
├── evals/
│   └── examples/              # Sample AI evaluation playbooks
├── tooling/
│   ├── metrics/               # Quick-start instrumentation guides and queries
│   └── evals/                 # Checklists and workflow automations for reviews
├── community/                 # Feedback loops, changelog, and adoption stories
├── .github/                   # Contribution templates and governance workflow
├── CONTRIBUTING.md          # How to participate
├── CODE_OF_CONDUCT.md       # Community expectations
└── README.md                # Project overview
```

## Getting Started

1. **Explore the metric examples** in [`metrics/examples`](metrics/examples/) and the AI evaluation examples in [`evals/examples`](evals/examples/) to understand the level of depth we expect.
2. **Review the maturity tiers** below to position your contribution as an Idea, Draft, or Field-Tested artifact before you start writing.
3. **Use the templates** in [`docs/metric_template.md`](docs/metric_template.md) or [`docs/eval_template.md`](docs/eval_template.md) to frame your idea. Focus on who benefits, why it matters, and how to measure success responsibly.
4. **Discuss big ideas** by opening a GitHub issue using the "New Artifact Proposal" template before submitting major proposals. Early collaboration helps align on scope and ethics.
5. **Submit a pull request** following the steps in [CONTRIBUTING.md](CONTRIBUTING.md). We review submissions for clarity, measurability, ethical alignment, and evidence that supports the stated maturity level.

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
- [`civic_participation_depth`](metrics/examples/civic_participation_depth.md) supports civic-tech platforms by measuring how often residents progress from awareness to concrete participation opportunities.
- [`accessibility_success_pathways`](metrics/examples/accessibility_success_pathways.md) centers disabled learners by tracking completion of accessible learning flows and surfacing blockers for remediation.

## AI Evaluation Playbooks for Ethical Businesses

AI-native organizations need evaluation suites that connect model performance with the human outcomes promised in their mission statements. Explore the detailed playbooks in [`evals/examples`](evals/examples/) for in-depth guidance on designing and governing AI evals programs that uphold ethical business practices:

- [`trust_centered_deployment_review`](evals/examples/trust_centered_deployment_review.md) pairs disclosure and consent audits with cross-functional reviews before expanding conversational AI deployments.
- [`impact_equity_monitor`](evals/examples/impact_equity_monitor.md) operationalizes fairness metrics, qualitative harm assessments, and mitigation follow-up plans for ranking and risk-scoring models.
- [`sustainable_automation_scorecard`](evals/examples/sustainable_automation_scorecard.md) measures how automation affects employee wellbeing, oversight quality, and environmental sustainability.
- [`inclusive_assistive_review`](evals/examples/inclusive_assistive_review.md) ensures AI accessibility assistants improve autonomy while protecting privacy and minimizing misdirection risk.
- [`civic_outreach_accountability_board`](evals/examples/civic_outreach_accountability_board.md) governs municipal AI outreach tools with transparency, bias remediation, and public reporting obligations.

Each playbook documents collection methods, review cadences, and responsible owners so that teams can iterate transparently. Contributors are encouraged to submit additional AI eval examples tailored to their industries—especially those that surface long-term human and societal impacts.

## Implementation Quick Starts

Every exemplar links to actionable assets in [`tooling/`](tooling/) so teams can move from documentation to execution. You'll find:

- **Instrumentation guides** that describe required events, schemas, and logging standards.
- **Reference queries and notebooks** for deriving each metric responsibly, including fairness slices and guardrails.
- **Evaluation playbooks** with facilitation checklists, automation scripts, and decision log templates that connect directly to review cadences.

Use these assets as a foundation, adapting them to your context while preserving the human-centered intent of each metric or evaluation.

## Contribution Maturity Tiers

To help adopters gauge reliability, every contribution must declare a maturity level:

- **Idea** – Conceptual framing with initial signals and guardrails. Requires community discussion before merge.
- **Draft** – Includes preliminary validation evidence (e.g., pilot data, qualitative research) and references tooling assets for implementation.
- **Field-Tested** – Demonstrated impact in production or programs with documented outcomes, maintenance owners, and governance rituals.

Issue and PR templates collect this information, and maintainers verify the maturity label before merging. Artifacts can be promoted between tiers once new evidence is documented in the community changelog.

## Community

Meaningful Metrics is maintained by volunteers who believe ethical design should be the default. We welcome contributors from product, research, design, policy, and lived-experience backgrounds. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

Visit the [`community/`](community/) area to browse changelogs, adoption stories, and upcoming office hours. Share your feedback via the intake form outlined there so we can publish regular updates and close the loop on requests.

## License

This project is available under the [MIT License](LICENSE).
