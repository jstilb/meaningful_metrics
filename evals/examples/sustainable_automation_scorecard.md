# Sustainable Automation Scorecard

**Maturity:** Draft

## Summary
Assesses whether AI-enabled automation programs improve stakeholder wellbeing while meeting environmental sustainability goals.

## When to Use This Evaluation
Deploy after major automation feature releases that affect frontline employees, suppliers, or energy-intensive infrastructure.

## Evaluation Objectives
- Verify automation reduces low-value toil without increasing burnout or eliminating critical human oversight.
- Measure environmental impact of training and inference workloads relative to business value delivered.
- Ensure remediation plans exist when wellbeing or sustainability thresholds are missed.

## Test Assets & Signals
- **Input data:**
  - Employee sentiment surveys (burnout, perceived autonomy) collected pre- and post-launch.
  - Operational logs capturing escalation rates, quality issues, and handoff frequency.
  - Energy usage reports from cloud providers, including carbon intensity by region.
- **Metrics & rubrics:**
  - Wellbeing delta score combining changes in burnout (-3 to +3), job satisfaction (-3 to +3), and voluntary attrition rates.
  - Oversight sufficiency checklist verifying human-in-the-loop coverage for high-risk decisions.
  - Carbon efficiency ratio comparing kg CO₂e per task automated vs. baseline manual process.
- **Guardrails:** Automatic remediation when wellbeing delta < 0, oversight checklist fails, or carbon efficiency ratio worsens by >15%.

## Execution Playbook
1. Partner with People Ops to anonymize and aggregate employee survey responses; ensure participation exceeds 60% of affected staff.
2. Analyze operational KPIs to confirm automation improves accuracy and turnaround without increasing escalations.
3. Collaborate with sustainability teams to attribute energy usage to the automation feature and calculate carbon intensity.
4. Facilitate a synthesis workshop where cross-functional stakeholders review findings and agree on mitigation or expansion steps.

## Acceptance Criteria & Reporting
- Publish a quarterly automation impact report summarizing wellbeing, oversight, and sustainability metrics with narrative context.
- Require leadership approval before scaling automation to new regions if any guardrail breaches persist.

## Governance & Maintenance
- Sustainability program manager co-owns the scorecard with the operations lead; update inputs when infrastructure providers change.
- Trigger ad-hoc evaluations after major model retraining or infrastructure migrations.
- Reference tooling assets in [`tooling/evals`](../../tooling/evals/) and capture follow-up actions in the decision log and community changelog.

## References & Inspiration
- World Economic Forum guidelines on human-centered automation.
- Green Software Foundation carbon accounting standards.
