```markdown
# End-to-End: Ecommerce Pipeline — Cheatsheet

## Section 1: Data Ingestion

| Thing                     | Syntax                                      | Notes                          |
|---------------------------|---------------------------------------------|--------------------------------|
| Batch Ingestion           | `spark.read.csv("path/to/data.csv")`      | Use for static datasets.       |
| Streaming Ingestion       | `spark.readStream.format("kafka")`        | Use for real-time data.       |
| Data Sources              | `["csv", "json", "parquet", "jdbc"]`      | Common formats for ingestion.  |
| Ingestion Options         | `.option("header", "true")`                | Customize read options.        |

## Section 2: Transformation Layer

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Ecommerce").getOrCreate()
df = spark.read.csv("path/to/data.csv", header=True)

# Transformation example: Filtering and renaming
transformed_df = df.filter(col("price") > 20).withColumnRenamed("oldName", "newName")
```

## Section 3: Serving Layer

| Thing                     | Syntax                                      | Notes                          |
|---------------------------|---------------------------------------------|--------------------------------|
| Write to Parquet         | `transformed_df.write.parquet("path/to/output")` | Efficient storage format.     |
| Write to Delta Lake      | `transformed_df.write.format("delta").save("path/to/delta")` | Supports ACID transactions.   |
| REST API Serving         | `from flask import Flask`                   | Use Flask to build APIs.      |

## Section 4: Observability

```python
from pyspark.sql import SparkSession

# Enable logging for monitoring
spark = SparkSession.builder \
    .appName("Ecommerce") \
    .config("spark.eventLog.enabled", "true") \
    .config("spark.eventLog.dir", "/path/to/logs") \
    .getOrCreate()
```

## Gotchas

- ⚠️ Always validate data after ingestion to catch schema drift.
- ⚠️ Monitor streaming jobs closely; they can fail silently if not handled.

## Mental model

1. **Ingestion**: Pull data from various sources (batch vs. streaming).
2. **Transformation**: Clean and prepare data for analysis.
3. **Serving**: Store and expose data to applications or users.
```