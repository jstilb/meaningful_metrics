# Actionability Score

## Definition

The Actionability Score measures how effectively consumed information translates into meaningful action.

## Formula

```
Actionability = (Items_bookmarked + Items_shared + Items_applied) / Items_consumed
```

Or in simplified form:
```
Actionability = Items_acted_on / Items_consumed
```

## Purpose

### The Information Overload Problem

We consume vast amounts of content:
- Articles read
- Videos watched
- Podcasts heard
- Social posts scrolled

But how much of this drives actual change?

### Why Actionability Matters

Information without action is entertainment, not learning.

A high Actionability Score indicates:
- Consuming relevant, useful content
- Having systems to capture and apply insights
- Quality over quantity consumption

## Action Categories

### Bookmarked

Content saved for future reference:
- Read-later lists
- Saved articles
- Pinned posts

**Weight**: 0.3 (weakest action)

### Shared

Content shared with others:
- Forwarded articles
- Social shares
- Recommendations

**Weight**: 0.5 (moderate action)

### Applied

Content that led to behavior change:
- Notes taken and reviewed
- Concepts implemented
- Skills practiced

**Weight**: 1.0 (strongest action)

## Weighted Formula

```python
def calculate_actionability(
    consumed: int,
    bookmarked: int,
    shared: int,
    applied: int,
) -> float:
    """Calculate weighted actionability score.

    Args:
        consumed: Total items consumed.
        bookmarked: Items saved for later.
        shared: Items shared with others.
        applied: Items that led to action.

    Returns:
        Actionability score (0.0 to 1.0+).
    """
    if consumed == 0:
        return 0.0

    weighted_actions = (
        bookmarked * 0.3 +
        shared * 0.5 +
        applied * 1.0
    )

    return weighted_actions / consumed
```

## Example

### Weekly Consumption

- Articles read: 50
- Videos watched: 20
- Podcasts: 5
- Total consumed: 75

### Actions Taken

- Articles bookmarked: 10
- Articles shared: 5
- Concepts applied: 3

### Calculation

```
Weighted actions = (10 * 0.3) + (5 * 0.5) + (3 * 1.0)
                 = 3.0 + 2.5 + 3.0
                 = 8.5

Actionability = 8.5 / 75 = 0.113 (11.3%)
```

### Interpretation

Only 11.3% of consumed content led to any form of action. This suggests:
- Possible content overload
- Need for better capture systems
- Opportunity to be more selective

## Improving Actionability

### Strategies

1. **Consume less, act more**: Quality over quantity
2. **Implement capture systems**: Notes, highlights, reviews
3. **Regular review cycles**: Weekly review of bookmarks
4. **Action-first filtering**: "Will I do anything with this?"

### Tools That Help

- Readwise (capture and resurface)
- Anki (spaced repetition for learning)
- Action-oriented note systems (Zettelkasten)

## Benchmarks

| Score | Interpretation |
|-------|----------------|
| < 5% | Consumption mode (passive) |
| 5-15% | Typical range |
| 15-30% | Active learner |
| 30%+ | Highly selective, action-oriented |

## Limitations

### Tracking Challenges

"Applied" is hard to track automatically:
- Requires user input
- Subjective judgment
- Delayed effects

### Not All Content Needs Action

Some content is legitimately for:
- Entertainment
- Rest
- Idle curiosity

Consider domain-specific actionability rather than global.

## Related Metrics

- **Quality Time Score**: Weights time by priority
- **Goal Alignment**: Time on goal-related activities
- **Learning Velocity**: Rate of skill acquisition
