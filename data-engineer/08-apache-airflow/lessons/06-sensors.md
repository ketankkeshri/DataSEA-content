# Sensors

Sensors in Apache Airflow allow you to trigger tasks based on external conditions or events, adding a powerful layer of flexibility to your workflows. Understanding how to implement sensors can help you build data pipelines that react dynamically to changes in your data environment.

## What Are Sensors?

Sensors are a special type of operator in Apache Airflow designed to wait for a certain condition to be met before executing downstream tasks. They can monitor various sources like files, databases, or even HTTP endpoints. For example, if you have a task that processes data only when a new file is uploaded to a specific S3 bucket, a sensor can be configured to “watch” that bucket and trigger the processing task once the file appears.

### Types of Sensors

There are several built-in sensors in Airflow, including:

- **FileSensor**: Waits for a file or directory to be present in a specified path.
- **S3KeySensor**: Monitors an S3 bucket for the presence of specific keys (files).
- **HttpSensor**: Checks for a specific HTTP response from a web service.
- **SqlSensor**: Waits for a certain condition to be true in a database.

Here’s a simple example of how to set up a `FileSensor` to wait for a file to appear in a local directory:

```python
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
}

with DAG(dag_id='file_sensor_example', default_args=default_args, schedule_interval='@daily') as dag:
    wait_for_file = FileSensor(
        task_id='wait_for_file',
        filepath='/path/to/your/file.txt',
        poke_interval=30,  # check every 30 seconds
        timeout=600,       # timeout after 10 minutes
    )
```

In this example, the `FileSensor` checks for the presence of `file.txt` every 30 seconds, and will fail if the file isn't found within 10 minutes.

## Best Practices for Using Sensors

While sensors can greatly enhance your workflows, there are some best practices to keep in mind:

- **Use Poke Interval Wisely**: Set the `poke_interval` to a reasonable value. Too frequent checks can overload your system and waste resources.
- **Timeouts**: Always define a `timeout` to prevent sensors from running indefinitely, which could block your DAG’s execution.
- **Use ExternalTaskSensor for Inter-DAG Dependencies**: If you need to wait for tasks in another DAG to complete, consider using `ExternalTaskSensor` instead of building complex dependencies within a single DAG.
  
Here’s how to use `ExternalTaskSensor` to wait for a task in another DAG:

```python
from airflow.sensors.external_task import ExternalTaskSensor

wait_for_another_dag_task = ExternalTaskSensor(
    task_id='wait_for_another_task',
    external_dag_id='another_dag',
    external_task_id='another_task',
    timeout=600,
    poke_interval=30,
)
```

## Common pitfalls

- **Overusing Sensors**: Relying too heavily on sensors can lead to inefficiencies. Look for opportunities to use event-driven architecture or other patterns.
- **Ignoring Error Handling**: Ensure that you handle potential errors in sensors gracefully to avoid breaking your DAGs.
- **Not Monitoring Performance**: Keep an eye on sensor performance. Long-running sensors can delay other tasks and affect overall pipeline performance.

## In a nutshell

- Sensors are operators that wait for specific conditions to trigger downstream tasks.
- Common sensors include FileSensor, S3KeySensor, and HttpSensor.
- Use sensible poke intervals and set timeouts to avoid blocking DAGs.
- Consider using ExternalTaskSensor for dependencies between DAGs.
- Monitor sensor performance to prevent inefficiencies in your data pipelines.