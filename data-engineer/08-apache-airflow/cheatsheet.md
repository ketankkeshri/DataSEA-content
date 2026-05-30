```markdown
# Apache Airflow — Cheatsheet

## [Section 1: DAGs]

| Thing         | Syntax                           | Notes                                       |
|---------------|----------------------------------|---------------------------------------------|
| Define DAG    | `@dag(schedule_interval='@daily')` | Use to create a DAG with a schedule.       |
| Add Task      | `@task` or `PythonOperator`      | Use `@task` for task decorators or `PythonOperator` for traditional tasks. |
| Trigger DAG   | `airflow dags trigger <dag_id>`  | Manually trigger a DAG from the CLI.       |

## [Section 2: Operators]

```python
from airflow.operators.python import PythonOperator

def my_task():
    print("Hello, World!")

task = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    dag=dag,
)
```

## [Section 3: XComs]

| Thing         | Syntax                           | Notes                                       |
|---------------|----------------------------------|---------------------------------------------|
| Push XCom     | `task_instance.xcom_push(key='key', value='value')` | Send data between tasks.                    |
| Pull XCom     | `task_instance.xcom_pull(task_ids='task_id', key='key')` | Retrieve data from another task.            |

## [Section 4: Scheduling & Backfill]

```bash
# Backfill a specific DAG
airflow dags backfill <dag_id> -s <start_date> -e <end_date>
```

## [Section 5: Sensors]

| Thing         | Syntax                           | Notes                                       |
|---------------|----------------------------------|---------------------------------------------|
| File Sensor   | `FileSensor`                     | Waits for a file to exist.                  |
| Time Sensor   | `TimeDeltaSensor`                | Waits for a specific time to pass.          |

## [Section 6: TaskFlow API]

```python
from airflow.decorators import dag, task

@dag(schedule_interval='@daily')
def my_dag():
    @task
    def start_task():
        return "Start"

    @task
    def end_task(start):
        print(start)

    start = start_task()
    end_task(start)

dag_instance = my_dag()
```

## [Best Practices]

- ⚠️ Keep tasks small and focused to simplify debugging.
- ⚠️ Avoid using global variables within tasks; use XComs instead for data sharing.

## [Gotchas]

- ⚠️ Make sure your DAGs are idempotent; avoid side effects on retries.
- ⚠️ Be cautious with the task dependencies; cyclic dependencies can cause issues.

## [Mental model]

- **DAG**: Directed Acyclic Graph
  - Composed of **Tasks** (nodes)
  - **Edges** represent task dependencies
  - Schedule determines execution frequency
```