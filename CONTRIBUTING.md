# Contributing to Meaningful Metrics

We are excited to collaborate with practitioners, researchers, and advocates who want to build metrics that prioritize human wellbeing. This guide outlines how to propose new metrics, improve existing ones, and participate in community discussions.

## Ways to Contribute

- **Propose a new metric** using the [metric template](docs/metric_template.md).
- **Share an AI evaluation playbook** using the [evaluation template](docs/eval_template.md).
- **Refine existing ideas** by commenting on issues or improving documentation.
- **Add tooling** that helps teams adopt meaningful metrics in practice.
- **Document implementation evidence** (case studies, survey results, changelog updates) in the `community/` directory.

## Before You Start

1. Read the [README](README.md) to understand the project mission and principles.
2. Review the [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to uphold these standards.
3. Check for existing [issues](https://github.com/meaningfulmetrics/meaningful_metrics/issues) or discussions related to your idea. Collaborating early reduces duplicated work.
4. Decide which **maturity tier** fits your contribution:
   - **Idea** – Conceptual framing and initial signals; requires community discussion prior to merge.
   - **Draft** – Includes preliminary validation evidence and references relevant tooling assets.
   - **Field-Tested** – Demonstrates impact with documented outcomes, governance rituals, and maintenance owners.
   Mention the tier in issues, pull requests, and the front matter of your artifact.

## Proposing a Metric or Evaluation

1. **Open a "New Artifact Proposal" issue.** Use the template to outline the problem, target users, and maturity tier. Gather early feedback before drafting.
2. **Draft your proposal.** Copy `docs/metric_template.md` or `docs/eval_template.md` into the appropriate directory and complete each section.
3. **Link supporting assets.** Reference relevant tooling quick starts, validation checklists, or community resources that operationalize your idea.
4. **Submit a pull request.** Include:
   - A summary of the artifact and who it benefits.
   - The declared maturity tier plus any validation evidence or adoption stories.
   - Links to supporting research and toolkit assets (e.g., fairness audits, decision logs).
5. **Incorporate feedback.** Maintainers and community members may ask for clarification or suggest improvements. We aim for collaborative, respectful review.

## Improving Existing Artifacts

- Highlight missing guardrails, unintended consequences, or opportunities to increase maturity tier.
- Suggest additional signals, validation methods, or references from lived experience.
- Provide implementation learnings (dashboards, survey results, changelog links) if you have tested the metric or evaluation in a real-world setting.
- Update tooling assets, governance templates, or community docs to reflect lessons learned.

## Development & Review Workflow

1. Fork the repository and create a feature branch.
2. Make your changes with clear, descriptive commits and update or create tooling/governance assets as needed.
3. Run any relevant checks or linters for the files you touched.
4. Open a pull request using the template provided in `.github/PULL_REQUEST_TEMPLATE.md` with:
   - A descriptive title and maturity tier.
   - A summary of changes and rationale.
   - Validation evidence, impacted tooling assets, and links to community updates.
   - Any follow-up questions or areas where you need feedback.
5. Respond to review comments and update the community changelog when your contribution merges.

## Community Expectations

- Be kind and curious. We are collectively learning how to build better metrics.
- Assume good intent, but name harms and biases when you see them.
- Cite sources for research or claims, and call out where evidence is still emerging.
- Respect privacy: do not share data that could identify real people.

Thank you for contributing to Meaningful Metrics! Together we can help teams build ethical, impactful products.
