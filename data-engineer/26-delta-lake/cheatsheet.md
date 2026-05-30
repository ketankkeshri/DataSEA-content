```markdown
# Delta Lake — Cheatsheet

## [Section 1: Core Concepts]

| Thing              | Syntax                            | Notes                                                   |
|--------------------|-----------------------------------|---------------------------------------------------------|
| Create Table       | `spark.sql("CREATE TABLE ...")`  | Use `USING DELTA` to create a Delta table.             |
| Read Delta Table   | `spark.read.format("delta").load(...)` | Load a Delta table for analysis.                        |
| Write to Delta     | `df.write.format("delta").mode("overwrite").save(...)` | Overwrites existing table data.                         |
| ACID Transactions   | `spark.sql("BEGIN TRANSACTION")` | Use for multi-step transactions.                        |
| Time Travel        | `spark.read.format("delta").option("timestampAsOf", "yyyy-MM-dd HH:mm:ss").load(...)` | Access previous states of the table.                   |

## [Section 2: Common Operations]

```python
# Time Travel Example
df = spark.read.format("delta").option("versionAsOf", 0).load("/path/to/delta/table")

# Optimize with Z-Ordering
spark.sql("OPTIMIZE delta.`/path/to/delta/table` ZORDER BY (column_name)")

# ACID Transaction Example
spark.sql("BEGIN TRANSACTION")
# Perform multiple operations
spark.sql("UPDATE ...")
spark.sql("DELETE ...")
spark.sql("COMMIT")
```

## [Gotchas]

- ⚠️ Ensure Delta Lake is enabled in your Spark session; otherwise, you'll get errors.
- ⚠️ Be cautious with time travel; accessing older versions can lead to performance hits if not managed well.

## [Mental model]

- **Delta Lake** operates on a **transaction log** that keeps track of every change.
- **ACID compliance** ensures reliable data operations.
- **Z-Ordering** improves query performance on specific columns by co-locating data.
```