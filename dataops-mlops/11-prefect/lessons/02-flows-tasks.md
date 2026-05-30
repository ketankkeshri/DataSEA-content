# Flows Tasks

Understanding how to create and manage tasks in Prefect Cloud is key for any Data Engineer or Data Scientist looking to streamline their workflows. Tasks are the building blocks of your data pipelines, and mastering them will help you orchestrate complex workflows with ease.

## What are Flows and Tasks?

In Prefect, a flow is a collection of tasks that define a data pipeline. Each task is a single unit of work, and flows orchestrate how these tasks run together. Think of a flow as a recipe: the tasks are the ingredients, and you need to combine them in the right order to create your final dish.

Here's how you can define a simple flow with tasks in Prefect:

```python
from prefect import flow, task

@task
def extract():
    return {"data": [1, 2, 3, 4]}

@task
def transform(data):
    return [x * 2 for x in data["data"]]

@task
def load(data):
    print(f"Loading data: {data}")

@flow
def etl_flow():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

if __name__ == "__main__":
    etl_flow()
```

This example outlines a basic ETL (Extract, Transform, Load) process. You define tasks for extracting data, transforming it, and loading it, then combine them into a single flow. When you run `etl_flow()`, Prefect orchestrates the execution of each task in the correct order.

## Task Configurations

Tasks in Prefect can be configured with various parameters to suit different use cases, such as retries, timeouts, and logging. Here’s how you can customize a task:

```python
@task(retries=3, timeout=10)
def fetch_data():
    # Simulating a data fetch that might fail
    import random
    if random.choice([True, False]):
        raise ValueError("Random failure!")
    return "Data fetched successfully!"
```

In this example, the `fetch_data` task will retry up to three times if it fails, with a timeout of 10 seconds. This makes your flows more resilient and capable of handling transient errors.

### Task Dependencies

You can also define dependencies between tasks explicitly. By default, tasks depend on the output of the tasks that precede them, but you can also set dependencies manually using the `upstream_tasks` parameter. Here’s how:

```python
@task
def clean_data(data):
    return [x for x in data if x is not None]

@flow
def data_pipeline():
    raw_data = extract()
    cleaned_data = clean_data(raw_data)
    transformed_data = transform(cleaned_data)
    load(transformed_data)
```

In the `data_pipeline` flow, `clean_data` depends on the output of `extract`. This allows for clear and manageable workflows, where you can easily see how tasks interact.

## Common pitfalls

- **Not handling task failures:** Always configure retries and timeouts to avoid manual intervention when tasks fail.
- **Cyclic dependencies:** Ensure that your tasks do not inadvertently reference each other in a cycle; Prefect cannot resolve those dependencies.
- **Ignoring logging:** Use Prefect's built-in logging features to keep track of task execution and troubleshoot issues effectively.

## In a nutshell

- Flows are collections of tasks that define a data pipeline.
- Tasks can be configured with retries, timeouts, and dependencies.
- Use Prefect's logging features for better observability.
- Avoid common pitfalls like cyclic dependencies and failure handling.

With these foundations in place, you're ready to build robust data workflows using Prefect Cloud!