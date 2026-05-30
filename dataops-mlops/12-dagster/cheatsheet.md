```markdown
# Dagster Fundamentals — Cheatsheet

## Section 1: DataOps + MLOps Overview

| Thing                | Syntax                                    | Notes                                                      |
|---------------------|-------------------------------------------|------------------------------------------------------------|
| Pipeline Definition  | `@dagster.pipeline`                       | Decorator to define a pipeline.                             |
| Solid Definition     | `@dagster.solid`                         | Decorator for defining a solid (a unit of computation).    |
| Asset Definition     | `@dagster.asset`                          | Used to define software-defined assets for data.           |
| Job Definition       | `@dagster.job`                            | Combines multiple solids into a single job.                |
| Schedule            | `@dagster.schedule`                       | Defines a periodic schedule to run a job.                  |
| Sensor              | `@dagster.sensor`                         | Monitors external events and triggers jobs.                 |

## Section 2: Common Operations

```python
from dagster import job, op, ScheduleDefinition

@op
def extract():
    return [1, 2, 3]

@op
def transform(data):
    return [x * 2 for x in data]

@op
def load(data):
    print("Loading:", data)

@job
def my_pipeline():
    load(transform(extract()))

# Schedule to run daily at midnight
my_schedule = ScheduleDefinition(
    job=my_pipeline,
    cron_schedule="0 0 * * *"  # Runs every day at midnight
)
```

## Gotchas

- ⚠️ Ensure all dependencies between solids are correctly defined; otherwise, you may face runtime errors.
- ⚠️ Watch out for circular dependencies in your pipeline; they will cause execution failures.

## Mental model

1. **Pipelines are workflows** composed of interconnected solids.
2. **Assets are data products** managed by Dagster, defined using the asset decorator.
3. **Schedules and sensors automate** pipeline execution based on time or external triggers.
```