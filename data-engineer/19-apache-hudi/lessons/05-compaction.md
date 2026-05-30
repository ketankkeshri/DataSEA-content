# Compaction

Compaction in Apache Hudi is crucial for optimizing storage and improving query performance. As a Data Engineer, understanding how and when to compact your datasets can save you time, money, and headaches down the road.

## What is Compaction?

Compaction is the process of merging smaller files into larger ones to reduce the number of files within a dataset. In Hudi, this is particularly important when using the Copy-on-Write (COW) storage type, where every update creates a new file. Over time, this can lead to numerous small files that degrade query performance and increase storage costs.

### How Compaction Works

When you compact, Hudi combines multiple smaller files into a single larger file, which reduces file system overhead and improves read performance. Here’s a simple example using Hudi to perform a compaction:

```python
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Hudi Compaction Example") \
    .getOrCreate()

# Read Hudi dataset
hudi_df: DataFrame = spark.read \
    .format("hudi") \
    .load("hdfs://path/to/hudi/table")

# Perform compaction
hudi_df.write.format("hudi") \
    .option("hoodie.compact.inline", "true") \
    .option("hoodie.compact.inline.max.delta.commits", "10") \
    .mode("overwrite") \
    .save("hdfs://path/to/hudi/table")
```

In this example, we read from an existing Hudi table and trigger an inline compaction. The `inline.max.delta.commits` option specifies how many commits should be merged in a single compaction run.

## Compaction Strategies

Hudi supports two main compaction strategies:

1. **Inline Compaction** - This occurs during the write process, merging small files as data is ingested. It’s useful for real-time use cases where you want to keep the dataset optimized continuously.
  
2. **Scheduled Compaction** - This is run as a separate job, usually at off-peak times, allowing you to manage resource usage better. You can configure the frequency and timing of these jobs based on your workload.

### Setting up Scheduled Compaction

To set up scheduled compaction, you would typically use a job scheduler like Apache Airflow. Here’s a pseudo-code example to illustrate this:

```python
# Pseudo-code for scheduling compaction in Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def compact_hudi_table():
    # Logic to trigger compaction on Hudi table
    pass

with DAG('hudi_compaction_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    compact_task = PythonOperator(
        task_id='compact_hudi_table',
        python_callable=compact_hudi_table,
    )
```

This DAG would run daily, triggering the `compact_hudi_table` function to compact your Hudi datasets.

## Common pitfalls

- **Ignoring Small Files Problem**: Not compacting regularly can lead to the small files problem, which degrades performance.
- **Resource Overhead**: Inline compaction can consume significant resources during peak times; consider scheduled compaction to avoid this.
- **Compaction Configuration**: Misconfiguring compaction parameters can lead to inefficient compaction processes and increased costs.

## In a nutshell

- Compaction reduces the number of small files, improving query performance.
- Hudi supports inline and scheduled compaction strategies.
- Regular compaction helps avoid the small files problem and optimizes storage.
- Use job schedulers like Airflow for efficient compaction management.
- Always monitor compaction performance to adjust parameters as needed.