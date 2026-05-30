```markdown
# Prefect Cloud — Cheatsheet

## [Section 1: Core Concepts]

| Thing             | Syntax                          | Notes                                      |
|-------------------|---------------------------------|--------------------------------------------|
| Flow              | `@flow` decorator               | Defines a Prefect flow.                    |
| Task              | `@task` decorator               | Defines a task that can be executed.       |
| Deployment        | `prefect.deploy`                | Deploys flows to Prefect Cloud.            |
| Work Pool         | `prefect.work_pool`             | Manages execution resources for tasks.     |

## [Section 2: Flows and Tasks]

```python
from prefect import flow, task

@task
def add(x, y):
    return x + y

@flow
def calculate_sum():
    return add(1, 2)

if __name__ == "__main__":
    print(calculate_sum())  # Output: 3
```

## [Deployments]

```python
from prefect.deployments import Deployment

# Define a deployment for the flow
deployment = Deployment.build_from_flow(
    flow=calculate_sum,
    name="sum-deployment",
    version="1.0",
    tags=["example"],
    work_pool="my-work-pool"
)
deployment.apply()  # Apply the deployment
```

## [Work Pools]

```python
from prefect import flow, task

@task
def multiply(x, y):
    return x * y

@flow
def calculate_product():
    return multiply(3, 4)

# Specify the work pool when running the flow
if __name__ == "__main__":
    calculate_product.set_run_config(
        run_config={"work_pool": "my-work-pool"}
    )
```

## [Gotchas]

- ⚠️ Ensure tasks are defined before they're called in flows to avoid circular dependencies.
- ⚠️ Deployments need valid work pools; otherwise, tasks won't execute.

## [Mental model]

- **Flow**: A sequence of tasks.
- **Task**: An atomic unit of work within a flow.
- **Deployment**: A specific instance of a flow that runs in a defined environment.
```