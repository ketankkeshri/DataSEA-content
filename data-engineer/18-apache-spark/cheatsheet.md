```markdown
# Apache Spark — Cheatsheet

## [Section 1: RDDs vs DataFrames]

| Thing                   | Syntax                          | Notes                                     |
|-------------------------|---------------------------------|-------------------------------------------|
| Create RDD              | `sc.parallelize(data)`          | `data` can be a list or collection.      |
| Create DataFrame        | `spark.createDataFrame(data)`  | `data` can be a list of Rows or a RDD.  |
| RDD Transformation       | `rdd.map(func)`                 | Applies `func` to each element.          |
| DataFrame Transformation | `df.select("column")`           | Selects specific columns.                 |

## [Section 2: Transformations & Actions]

```python
# Transformation example
transformed_df = df.filter(df.age > 18)

# Action example
count = transformed_df.count()
```

## [Section 3: Partitioning]

| Thing                 | Syntax                                   | Notes                              |
|-----------------------|------------------------------------------|------------------------------------|
| Repartition RDD       | `rdd.repartition(num_partitions)`       | Increases or decreases partitions. |
| Coalesce RDD          | `rdd.coalesce(num_partitions)`          | Decreases partitions without shuffle. |

## [Section 4: Shuffles]

```python
# Shuffle example
shuffled_df = df.groupBy("key").agg({"value": "sum"})
```

## [Section 5: Broadcast Joins]

```python
# Broadcast join example
broadcasted_df = spark.sparkContext.broadcast(small_df)
joined_df = large_df.join(broadcasted_df.value, "key")
```

## [Section 6: Tuning]

| Thing                | Syntax                              | Notes                                   |
|----------------------|-------------------------------------|-----------------------------------------|
| Set Executor Memory   | `spark-submit --executor-memory 4g` | Adjust memory allocation for executors. |
| Set Driver Memory     | `spark-submit --driver-memory 2g`   | Adjust memory allocation for the driver. |

## [Section 7: Structured Streaming]

```python
# Structured Streaming example
streamingDF = spark.readStream.format("csv").option("header", "true").load("path/to/stream")
query = streamingDF.writeStream.outputMode("append").format("console").start()
```

## [Gotchas]

- ⚠️ Avoid using too many partitions; it can lead to overhead.
- ⚠️ Always consider the order of operations; actions trigger computation.

## [Mental model]

- **RDD:** Immutable distributed collection, transformations produce new RDDs.
- **DataFrame:** Distributed data organized into named columns, supports SQL queries.
- **Structured Streaming:** Continuous stream processing, leverages DataFrames for real-time data.

```