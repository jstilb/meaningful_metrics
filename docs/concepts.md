# Framework Concepts

Meaningful Metrics is built on a set of composable, transparent primitives. This page explains the "why" behind the framework's design.

## The Engagement Trap

Traditional digital product metrics are defined by what is easy to measure, not what matters:

| Metric | What It Optimizes | What It Ignores |
|--------|------------------|-----------------|
| Session duration | More time on platform | Whether time was well-spent |
| Click-through rate | More clicks | Whether action was desired |
| Daily active users | More frequent visits | Whether visits were valuable |
| Watch time | More content consumed | Whether content was beneficial |

These metrics are not malicious — they're just easy to collect. But optimizing for them creates products that extract attention rather than respect it.

## Human-Centered Alternatives

Meaningful Metrics replaces these proxies with direct measures of human outcomes:

### 1. Quality Time Score (QTS)

**The question it answers:** How much valuable time did the user actually spend?

QTS weights time by priority and applies diminishing returns caps to prevent over-optimization on a single domain.

```
QTS = sum(min(Ti, Capi) * Pi)
```

Where `Ti` is time spent, `Capi` is the diminishing returns cap, and `Pi` is the user's priority weight.

See [Quality Time Score](concepts/quality-time-score.md) for full details.

### 2. Goal Alignment

**The question it answers:** Is the user making progress on what they said they care about?

```
Goal Alignment = (sum(Time on goal domains) / Total time) * 100%
```

See [Goal Alignment](concepts/goal-alignment.md) for full details.

### 3. Actionability Score

**The question it answers:** Does consumed information translate into meaningful action?

```
AS = (bookmarked * 0.3 + shared * 0.5 + applied * 1.0) / consumed
```

See [Actionability](concepts/actionability.md) for full details.

### 4. Distraction Ratio

**The question it answers:** How much time is being lost to low-priority activities?

```
Distraction Ratio = 100% - Goal Alignment
```

### 5. Locality Score

**The question it answers:** Is content relevant to the user's actual community and context?

```
Locality Score = local_relevance * engagement
```

## Design Principles

### User-Controlled Parameters

Every metric in this framework is parameterized by user-defined values:

- **Priorities** are set by the user, not inferred by the platform
- **Goals** are declared by the user, not predicted by the algorithm
- **Caps** are defined by the user, not optimized by engagement loops

This is a deliberate inversion of the standard model. Most platforms use behavioral data to infer what users "want" — then optimize for that inferred preference. Meaningful Metrics starts with explicit user declarations.

### Transparent Formulas

Every metric has a documented formula. There are no black-box scoring systems. Users and developers can inspect, audit, and challenge any calculation.

### Differentiable (for ML)

All metrics are designed to be usable as training signals for ML systems. The `soft_min` function provides a differentiable approximation of the diminishing returns cap, enabling gradient-based optimization.

### Privacy-Preserving

The framework processes time entries and action logs. It does not require user identity, behavioral fingerprints, or third-party tracking.

## Relationship to Constitutional AI

Anthropic's [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) approach establishes explicit principles that AI systems are evaluated against during training. Meaningful Metrics applies the same logic at the product evaluation layer.

Where Constitutional AI asks: *"Does this model output violate human values?"*

Meaningful Metrics asks: *"Does this product experience violate the user's declared intentions?"*

Both frameworks share the conviction that AI systems need explicit human principles as guardrails — not just implicit feedback from engagement data.

## When to Use This Framework

**Good fit:**

- Evaluating AI assistant products (chatbots, recommendation systems)
- Designing training incentives for RLHF pipelines
- Auditing existing products for alignment with user wellbeing
- Research on human-AI interaction quality

**Not designed for:**

- Real-time content ranking (too computationally expensive per-request)
- Individual recommendation scoring
- Aggregate population-level analytics without individual goal data
