# Meaningful Metrics Specification

> **Version:** 1.0.0
> **Status:** Draft (Conceptual)
> **Owner:** jstilb
> **Created:** 2026-01-21
> **Last Updated:** 2026-01-21

---

## Overview

**Purpose:** Framework of metrics for training AI systems to optimize for human wellbeing and goal achievement rather than engagement maximization.

**Type:** Framework / Pipeline Component
- [ ] Autonomous Agent
- [ ] Task Executor
- [ ] Assistant/Copilot
- [x] Pipeline Component

**Summary:** Meaningful Metrics addresses a critical gap in AI alignment: current systems optimize for time-on-app rather than user wellbeing. This framework provides differentiable, measurable metrics that can train AI to optimize for quality of experience, goal alignment, and meaningful outcomes.

---

## 1. Commands & Capabilities

### 1.1 Primary Capability

Provide a mathematical framework of metrics that AI systems can optimize against to serve human flourishing.

**Core Operation:**
```
Input: User's goals, priorities, time allocations, and consumption patterns
Process: Calculate quality scores → Track against targets → Generate recommendations
Output: Quality Time Score, goal alignment metrics, actionable insights
```

### 1.2 Core Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Quality Time Score** | `Σ(Tᵢ × Pᵢ)` | Weighted sum of time × priority |
| **Goal Alignment** | `Time_goal_related / Total_time` | % of time on stated goals |
| **Distraction Ratio** | `Time_distraction / Total_time` | % of time on non-goals |
| **Actionability Score** | `Items_acted_on / Items_consumed` | Information → action conversion |
| **Locality Score** | `Local_relevance × Engagement` | Weight for community relevance |

### 1.3 Supporting Capabilities

| Capability | Purpose | Priority |
|------------|---------|----------|
| Time Tracking by Domain | Measure time per category | Critical |
| Priority Scoring | Rank domains by user goals | Critical |
| Diminishing Returns | Cap value after X hours | Important |
| Weekly Bucketing | Track patterns over time | Important |
| Cross-Platform Aggregation | Unify metrics across apps | Nice-to-have |

### 1.4 Capability Boundaries

**In Scope:**
- Metric definitions and formulas
- Score calculation algorithms
- Goal-setting interfaces
- Progress tracking
- Recommendation generation

**Out of Scope:**
- Platform-level implementation (separate projects)
- Browser extension development
- Mobile app development
- Actual AI model training

---

## 2. Testing & Validation

### 2.1 Success Criteria

| Criterion | Measurement | Target |
|-----------|-------------|--------|
| Metric Differentiability | Can be used in ML optimization | 100% |
| Measurability | Can be computed from available data | 100% |
| Correlation with Wellbeing | Self-reported satisfaction | Positive correlation |
| Behavior Change | Users with metrics improve habits | Measurable improvement |

### 2.2 Test Cases

**Critical Path Tests:**

```
TEST 1: Quality Time Calculation
Given: User spends 2h on high-priority learning (P=1.0), 1h social media (P=0.2)
When: Quality Time Score calculated
Then: Score = (2×1.0) + (1×0.2) = 2.2 (vs raw 3.0 hours)
```

```
TEST 2: Diminishing Returns
Given: User sets "Reading" as max 2h/day value
When: User reads for 4 hours
Then: Score caps at 2h contribution, not 4h
```

### 2.3 Validation Approach

| Method | Purpose |
|--------|---------|
| User Studies | Correlate metrics with self-reported wellbeing |
| A/B Testing | Compare optimizing for QTS vs time-on-app |
| Long-term Tracking | Monitor goal achievement rates |

---

## 3. Structure & Context

### 3.1 Data Requirements

| Data Type | Source | Required |
|-----------|--------|----------|
| Time per domain | Browser/app tracking | Yes |
| User goals | User input | Yes |
| Priority weights | User input | Yes |
| Action outcomes | User logging | Optional |

### 3.2 Input Specification

**User Goals Input:**
```typescript
interface UserGoals {
  goals: Goal[];
  weeklyTimeBudgets: TimeBudget[];
  priorities: DomainPriority[];
}

interface Goal {
  id: string;
  name: string;
  domains: string[];  // Related content domains
  targetHoursPerWeek: number;
}

interface DomainPriority {
  domain: string;    // e.g., "learning", "news", "social"
  priority: number;  // 0.0 - 1.0
  maxDailyHours?: number;  // Diminishing returns cap
}
```

### 3.3 Output Specification

**Metrics Output:**
```typescript
interface MetricsReport {
  period: 'daily' | 'weekly';
  qualityTimeScore: number;
  rawTimeHours: number;
  goalAlignmentPercent: number;
  distractionPercent: number;
  actionabilityScore: number;

  byDomain: DomainMetrics[];
  recommendations: Recommendation[];
}

interface DomainMetrics {
  domain: string;
  timeSpent: number;
  effectiveTime: number;  // After diminishing returns
  priority: number;
  contribution: number;   // To QTS
}
```

---

## 4. Style & Behavior

### 4.1 Communication Style

**Tone:** Supportive coach, not judgmental tracker

**Characteristics:**
- Focus on progress, not perfection
- Highlight wins before gaps
- Suggest, don't shame

### 4.2 Metric Presentation

**Dashboard Elements:**
- Quality Time Score (prominent)
- Goal progress bars
- Domain breakdown pie chart
- Week-over-week trends
- Actionable recommendations

---

## 5. Workflow & Process

### 5.1 User Setup Flow

```
┌─────────────┐
│ ONBOARDING  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ SET GOALS   │ What do you want to achieve?
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ PRIORITIZE  │ Rank your content domains
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ SET LIMITS  │ Max useful time per domain
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ CONNECT     │ Link data sources
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  TRACKING   │ Begin measurement
└─────────────┘
```

### 5.2 Continuous Improvement Loop

```
┌─────────────┐
│   MEASURE   │ Track time and actions
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  CALCULATE  │ Compute metrics
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   REFLECT   │ Weekly review
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   ADJUST    │ Refine goals/priorities
└──────┬──────┘
       │
       └──────→ [MEASURE]
```

---

## 6. Boundaries & Guardrails

### 6.1 ✅ Always (No Approval Required)

- Calculate metrics from provided data
- Generate recommendations
- Show progress visualizations
- Export personal data

### 6.2 ⚠️ Ask First (Requires Confirmation)

- Share metrics with third parties
- Integrate with new data sources
- Modify established goals

### 6.3 🚫 Never (Absolutely Prohibited)

- Shame or guilt users
- Optimize for engagement over wellbeing
- Share individual data without consent
- Create addictive tracking loops
- Penalize taking breaks

### 6.4 Ethical Principles

| Principle | Implementation |
|-----------|----------------|
| User Autonomy | User sets all goals and priorities |
| Transparency | All metrics and formulas visible |
| Privacy | All data stays local or user-controlled |
| No Manipulation | Never use dark patterns |
| Wellbeing First | Metrics optimize for flourishing |

---

## 7. Integration

### 7.1 Potential Integrations

| System | Data Provided | Format |
|--------|---------------|--------|
| Browser Extensions | Web time tracking | Time per domain |
| Mobile Screen Time | App usage | Time per app |
| Calendar | Scheduled activities | Events |
| Readwise/Anki | Learning actions | Items reviewed |

### 7.2 Feeds Into

| Consumer | Data Provided | Purpose |
|----------|---------------|---------|
| Information Venture | Quality metrics | Optimize for QTS not engagement |
| AI Training | Reward signal | Train models on wellbeing |
| Personal Dashboards | Weekly reports | User reflection |

---

## 8. Operational

### 8.1 Technical Requirements

**For ML Optimization:**
- All metrics must be differentiable
- Metrics must be computable in real-time
- Support for multi-objective optimization
- Batch and streaming calculation modes

### 8.2 Formula Specifications

**Quality Time Score:**
```
QTS = Σ(min(Tᵢ, Capᵢ) × Pᵢ)

Where:
- Tᵢ = Time spent in domain i
- Capᵢ = Max valuable hours for domain i (diminishing returns)
- Pᵢ = Priority score for domain i (0.0 - 1.0)
```

**Goal Alignment:**
```
GA = Σ(Tgoal_domains) / Ttotal × 100%
```

**Actionability:**
```
AS = (Items_bookmarked + Items_shared + Items_applied) / Items_consumed
```

### 8.3 Implementation Status

| Component | Status |
|-----------|--------|
| Framework definition | Complete |
| Formula specification | Complete |
| Reference implementation | Not started |
| Integration APIs | Not started |
| Dashboard UI | Not started |

---

## Appendix

### A. Problems Being Solved

| Current Reality | Meaningful Metrics Solution |
|-----------------|---------------------------|
| Optimize for time-on-app | Optimize for Quality Time Score |
| All time weighted equally | Priority-weighted time |
| No diminishing returns | Caps on useful time |
| Engagement = success | Goal achievement = success |
| Hidden algorithms | Transparent metrics |

### B. Research Foundation

Based on concepts from:
- Attention economics
- Wellbeing research
- Goal-setting theory
- Information diet frameworks
- Time tracking methodologies

### C. Future Research

- Correlation studies with self-reported wellbeing
- Long-term behavior change analysis
- Cross-cultural validation
- Integration with AI reward modeling

---

**Spec Generated By:** SpecSheet Skill
**Generation Date:** 2026-01-21
