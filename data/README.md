# Data Directory

This directory contains datasets used for testing, evaluation, and demonstration of the Meaningful Metrics framework.

## Structure

```
data/
  raw/          # Unprocessed input data (time logs, action logs)
  processed/    # Cleaned and transformed data ready for analysis
```

## Data Format

Input data follows the Pydantic schemas defined in `src/meaningful_metrics/schemas.py`:

### TimeEntry
```json
{"domain": "learning", "hours": 2.5}
```

### Goal
```json
{"id": "learn-python", "name": "Learn Python", "domains": ["programming", "tutorials"], "target_hours_per_week": 5.0}
```

### DomainPriority
```json
{"domain": "learning", "priority": 1.0, "max_daily_hours": 4.0}
```

### ActionLog
```json
{"consumed": 100, "bookmarked": 20, "shared": 5, "applied": 10}
```

## Privacy

All data in this directory is synthetic. No real user data is stored in this repository.

## Adding Data

When contributing sample datasets:

1. Use realistic but synthetic values
2. Include a `README.md` or header comment describing the dataset
3. Follow the schema formats above
4. Place raw data in `raw/` and any derived data in `processed/`
