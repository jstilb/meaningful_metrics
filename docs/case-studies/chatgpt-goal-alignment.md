# Case Study: ChatGPT Scores 76% on Goal Alignment

**Framework:** Meaningful Metrics v0.1.0
**Product Evaluated:** ChatGPT (OpenAI)
**Evaluation Type:** Cross-segment user population analysis
**Date:** February 2024

---

## Summary

Using the Meaningful Metrics framework, we evaluate ChatGPT as an AI product
against four core dimensions: Goal Alignment, Quality Time Score, Distraction
Ratio, and Actionability Score. Data is constructed from published research on
ChatGPT usage patterns across three distinct user segments.

**Headline: ChatGPT scores 76% on Goal Alignment across the general user population.**

This is a stronger result than engagement-only metrics would suggest — but the
per-segment breakdown reveals a critical insight: the 24% of usage time that
*doesn't* advance user goals is concentrated in the largest user segment (Casual
Explorers, 38% of users), and would be completely invisible to standard product
analytics.

---

## Context

### Why Evaluate ChatGPT?

ChatGPT is the most widely adopted AI assistant product, with over 100 million
weekly active users as of late 2023 (OpenAI, 2023). It represents the
archetypal general-purpose AI assistant — making it an ideal first subject for
demonstrating how the Meaningful Metrics framework surfaces insights that
engagement metrics cannot.

Standard ChatGPT product metrics include: daily active users, session duration,
messages per session, and retention rates. None of these metrics answer the
question that matters most: *Is users' time with ChatGPT actually advancing
their goals?*

### What This Evaluation Is (and Isn't)

This is a **population-level framework demonstration**, not a live product audit.
Data points are derived from published research on ChatGPT usage patterns —
not from OpenAI's internal analytics. The purpose is to show how Meaningful
Metrics would be applied and what insights it would surface.

This evaluation is **not a criticism of ChatGPT**. A 76% Goal Alignment score
is genuinely strong for a general-purpose tool. The more important finding is
what the framework surfaces that standard metrics hide.

---

## Methodology

### User Segments

We identified three primary ChatGPT user segments based on Pew Research Center
(2023) usage pattern research:

| Segment | Population Share | Primary Use Case |
|---------|-----------------|-----------------|
| Knowledge Workers | 34% | Professional productivity tasks |
| Students | 28% | Learning and academic work |
| Casual Explorers | 38% | Exploration, entertainment, curiosity |

### Data Sources

Usage time allocation by segment:
- **MIT Sloan Management Review (2023):** Knowledge worker AI usage patterns
  (drafting 42%, summarizing 31%, brainstorming 18%, off-task 9%)
- **Stanford VPTL (2023):** Student AI usage patterns
  (essay help 58%, concept explanation 42%, problem solving 31%)
- **Pew Research Center (2023):** Demographic breakdown and casual usage patterns
- **Bastani et al. (2023), NBER Working Paper:** AI tutoring impact on learning outcomes;
  distinguishes interactive tutoring (high retention) from passive answer-fetching (low retention)

Actionability data:
- Stanford HAI (2023) session goal achievement rates (~67% for knowledge workers)
- Bastani et al. (2023) knowledge retention rates (~35% in student segment)

### Metrics Configuration

Goals and domain priorities were defined to reflect each segment's declared
objectives — not inferred from behavioral data. This is intentional: Meaningful
Metrics starts from explicit human intentions.

The full evaluation script is at: `results/case-studies/run_chatgpt_study.py`

---

## Findings

### Knowledge Worker Segment (34% of users)

```
Quality Time Score:   2.54
Goal Alignment:       92.3%
Distraction Ratio:     7.7%
Actionability Score:  0.495
```

**Interpretation:** This is the highest-performing segment by a wide margin.
Knowledge workers come to ChatGPT with concrete tasks and mostly execute them.
The 92.3% Goal Alignment reflects the high-intent, task-specific nature of
professional use.

The 0.495 Actionability Score (out of max 1.0+ theoretical) indicates nearly
half of all interactions produce a bookmarked, shared, or directly applied
output — well above passive consumption.

**Notable pattern:** Drafting and task completion together account for ~70% of
QTS contributions. These are the use cases where ChatGPT delivers clearest value.

### Student Segment (28% of users)

```
Quality Time Score:   3.24
Goal Alignment:       76.5%
Distraction Ratio:    23.5%
Actionability Score:  0.570
```

**Interpretation:** Students show strong goal alignment with a surprising
finding: the highest QTS of any segment. This reflects prioritization — learning
and problem-solving activities carry high priority weights, boosting quality score
even when raw hours are similar across segments.

The critical finding from Bastani et al. (2023) appears in the domain breakdown:
`passive_answer_fetching` (0.70 hours/week) carries a 0.15 priority weight and
contributes only 0.10 QTS. This domain represents the "shortcut" use pattern
that produces high engagement metrics but poor learning outcomes.

An engagement-optimized product would celebrate these sessions (they're long,
they generate tokens, the user returns). A goal-alignment-optimized product
would recognize that these sessions fail the student's actual objective (building
genuine understanding) and would design prompting strategies to redirect toward
interactive tutoring.

**Key recommendation surfaced:** Students are spending time over the
`drafting` domain cap — suggesting ChatGPT is being used for more essay
generation than is healthy for learning. The framework surfaces this; standard
engagement metrics would not.

### Casual Explorer Segment (38% of users)

```
Quality Time Score:   1.32
Goal Alignment:       60.0%
Distraction Ratio:    40.0%
Actionability Score:  0.225
```

**Interpretation:** This is the most complex segment to evaluate. "Casual
exploration" is not inherently bad — curiosity, play, and entertainment are
legitimate human needs. But this segment accounts for 38% of users and has the
lowest goal alignment, suggesting significant time is spent in ways users
themselves would not identify as purposeful.

The 0.225 Actionability Score is the lowest of any segment — casual interactions
rarely produce saved, shared, or applied outputs. Contrast with the knowledge
worker segment's 0.495. This doesn't mean casual use is wasteful, but it does
signal that ChatGPT has not found strong product-market fit for casual users
seeking *meaningful* outcomes.

The domain breakdown shows `off_task_exploration` (1.5 hours/week, priority 0.15)
as a major time sink. This is precisely the "dopamine scroll" equivalent for
AI assistants — engaging, low-value time that an engagement-optimized product
would silently reward.

---

## Population-Weighted Aggregate

Weighting each segment by its share of the user population:

```
Quality Time Score:   2.27
Goal Alignment:       76.0%
Distraction Ratio:    24.4%
Actionability Score:  0.413
```

### Interpretation

**76% Goal Alignment is genuinely strong.** For a general-purpose tool used
across radically different contexts, sustaining three-quarters of usage time
on user-declared objectives is meaningful. ChatGPT is not TikTok.

**The 24% distraction gap reveals an opportunity.** Almost a quarter of all
ChatGPT usage time does not advance the user's stated goals. At the scale of
100 million weekly users, this represents an enormous aggregate opportunity cost.

**Actionability at 0.413 suggests moderate output quality.** Fewer than half
of all interactions produce an artifact the user saves, shares, or acts on.
This is consistent with a product that is useful but not yet reliably
purposeful.

---

## Recommendations

Based on the Meaningful Metrics analysis, three concrete product improvements
would move the needle on Goal Alignment:

### 1. Session Intention Prompts

**For:** Casual Explorer segment
**Mechanism:** At session start, prompt the user: "What do you want to accomplish
today?" (optional, never mandatory). Map the response to a goal domain.
**Expected impact:** Even a 15% shift of `off_task_exploration` time to
`personal_advice` or `research_synthesis` would raise aggregate goal alignment
by ~2-3 points.

### 2. Learning Mode with Recall Prompts

**For:** Student segment
**Mechanism:** When ChatGPT detects study-related context, offer "Learning Mode"
that witholds direct answers, instead prompting the student to reason through
the problem and offering hints. At session end, prompt recall: "Without looking,
what's the key thing you learned?"
**Expected impact:** Directly targets the `passive_answer_fetching` problem surfaced
by Bastani et al. (2023). Would improve Actionability Score by shifting from
consumption to retention.

### 3. Action Capture at Session End

**For:** All segments
**Mechanism:** After each conversation, offer one-click options: "Save this,"
"Share with someone," "Add to my notes," "I'll apply this to [task]."
**Expected impact:** Would directly increase Actionability Score from 0.413 toward
0.5+, and creates data for the user's own goal tracking.

---

## Limitations

1. **No ground truth data.** This evaluation uses research-derived approximations,
   not OpenAI's internal telemetry. The segment proportions and time allocations
   are estimates based on survey data.

2. **Goal alignment requires declared goals.** Users who have not explicitly
   declared goals cannot have goal alignment measured. The framework requires
   a product-level mechanism for capturing user intentions.

3. **Domain taxonomy is an approximation.** Real ChatGPT usage does not arrive
   pre-labeled by domain. Applying this framework in production would require
   an intent classification model or explicit user tagging.

4. **Normative assumptions.** The priority weights assigned to domains
   (e.g., "passive_answer_fetching" priority 0.15 for students) encode
   value judgments. Different researchers might assign different weights.
   This is a feature, not a bug — it forces explicit articulation of values
   that engagement metrics leave implicit.

---

## Conclusion

The Meaningful Metrics framework reveals what engagement metrics hide: ChatGPT's
strong overall Goal Alignment (76%) coexists with a meaningful gap in the largest
user segment (Casual Explorers, 38% of users, 40% distraction ratio) and a
structural problem in the Student segment (passive answer-fetching undermining
the learning goal).

This is the core argument for measurement frameworks grounded in human intentions:
**a product can have excellent engagement metrics and still fail to serve users
well.** The framework makes that failure visible, measurable, and actionable.

---

## Reproduce This Analysis

```bash
# Install the package
pip install meaningful-metrics

# Clone the repo
git clone https://github.com/jstilb/meaningful_metrics.git
cd meaningful_metrics

# Run the evaluation
python results/case-studies/run_chatgpt_study.py
```

---

## References

- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2023).
  *Generative AI Can Harm Learning*. NBER Working Paper.
- Pew Research Center. (2023). *AI in Everyday Life: Patterns of Use Across
  Demographics*.
- MIT Sloan Management Review. (2023). *Generative AI at Work: Early Evidence
  from Professionals*.
- Stanford Human-Centered AI. (2023). *AI Assistant Interaction Quality: A
  Multi-Study Assessment*.
- Stanford VPTL. (2023). *Student Use of AI Writing Tools: Patterns, Outcomes,
  and Guidance*.
- OpenAI. (2023). *ChatGPT: 100 Million Weekly Active Users*. Company blog.
