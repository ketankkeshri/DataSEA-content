```markdown
# Lakehouse Architecture — Cheatsheet

## [Section 1: Bronze-Silver-Gold Layers]

| Layer  | Purpose                                    | Data Format         |
|--------|--------------------------------------------|---------------------|
| Bronze | Raw, unprocessed data.                     | Parquet, ORC        |
| Silver | Cleaned and transformed data.              | Delta Lake          |
| Gold   | Aggregated data for analytics and reporting.| Aggregated tables    |

## [Section 2: Table Format Choice]

| Format     | Pros                                   | Cons                                   |
|------------|----------------------------------------|----------------------------------------|
| Parquet    | Columnar storage, efficient for analytics | Not as fast for write-heavy operations |
| ORC        | Highly efficient for read operations   | Less flexible than other formats       |
| Delta Lake | ACID transactions, time travel support | More complexity in setup               |

```python
# Example of creating Delta table in PySpark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Lakehouse Example") \
    .getOrCreate()

data = [("Alice", 34), ("Bob", 45)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Write DataFrame to Delta format
df.write.format("delta").mode("overwrite").save("/path/to/delta_table")
```

## [Compute Engines]

| Engine        | Use Case                               | Notes                          |
|---------------|----------------------------------------|--------------------------------|
| Apache Spark  | Batch processing, ML workloads         | Supports both streaming and batch |
| Databricks    | Optimized Spark environment            | Managed service, collaborative notebooks |
| Presto        | Interactive analytics                  | Good for SQL queries on large datasets |

```python
# Querying Delta table using Spark SQL
spark.sql("SELECT * FROM delta.`/path/to/delta_table` WHERE Age > 30").show()
```

## [Gotchas]

- ⚠️ Ensure correct data types when writing to Delta tables to avoid schema mismatches.
- ⚠️ Be careful with null values in the Bronze layer; they can propagate and affect analytics.

## [Mental model]

- **Bronze**: Raw data → **Silver**: Cleaned data → **Gold**: Analytics-ready data
- Data flows through layers, getting progressively refined.
- Use Delta Lake for managing versions and schema evolution.
```