# Contributing to Meaningful Metrics

We are excited to collaborate with practitioners, researchers, and advocates who want to build metrics that prioritize human wellbeing. This guide outlines how to propose new metrics, improve existing ones, and participate in community discussions.

## Ways to Contribute

- **Propose a new metric** using the [metric template](docs/metric_template.md)
- **Refine existing ideas** by commenting on issues or improving documentation
- **Share research** that validates or challenges the assumptions behind a metric
- **Build tooling** that helps teams adopt meaningful metrics in practice

## Before You Start

1. Read the [README](README.md) to understand the project mission and principles.
2. Review the [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to uphold these standards.
3. Check for existing [issues](https://github.com/meaningfulmetrics/meaningful_metrics/issues) or discussions related to your idea. Collaborating early reduces duplicated work.

## Proposing a Metric

1. **Start with a discussion (optional but encouraged).** Open a GitHub issue with the `discussion` label to outline the problem and desired outcome.
2. **Draft your proposal.** Copy `docs/metric_template.md` into `metrics/<your_metric_name>.md` (or an appropriate subdirectory) and complete each section.
3. **Submit a pull request.** Include:
   - A summary of the metric and who it benefits
   - Notes on validation, ethics, and potential blind spots
   - Links to any supporting research
4. **Incorporate feedback.** Maintainers and community members may ask for clarification or suggest improvements. We aim for collaborative, respectful review.

## Improving Existing Metrics

- Highlight any missing guardrails or potential unintended consequences.
- Suggest additional signals, validation methods, or references.
- Provide implementation learnings if you have tested the metric in a real-world setting.

## Development Workflow

1. Fork the repository and create a feature branch.
2. Make your changes with clear, descriptive commits.
3. Run any relevant checks or linters for the files you touched.
4. Open a pull request with:
   - A descriptive title
   - A summary of changes and rationale
   - Any follow-up questions or areas where you need feedback

## Community Expectations

- Be kind and curious. We are collectively learning how to build better metrics.
- Assume good intent, but name harms and biases when you see them.
- Cite sources for research or claims, and call out where evidence is still emerging.
- Respect privacy: do not share data that could identify real people.

Thank you for contributing to Meaningful Metrics! Together we can help teams build ethical, impactful products.
