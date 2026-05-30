```markdown
# Apache Hudi — Cheatsheet

## [Core Concepts]

| Thing                    | Syntax                                       | Notes                                                     |
|------------------------- |---------------------------------------------|-----------------------------------------------------------|
| Hudi Table Type          | `tableType = 'COPY_ON_WRITE'` or `tableType = 'MERGE_ON_READ'` | Choose based on read/write patterns.                      |
| Data Schema              | `schema = {...}`                            | Define the schema for the Hudi table.                     |
| Record Key               | `recordKey = 'your_record_key'`            | Unique identifier for records in the table.               |
| Precombine Field         | `precombineField = 'your_field'`           | Field used to resolve duplicates.                          |
| Partition Path           | `partitionPath = 'your_partition_path'`    | Specify partitioning strategy for data organization.      |

## [Write Paths]

```python
from hudi import HudiDataFrame
df.write \
  .format("hudi") \
  .option("hoodie.table.name", "your_table_name") \
  .option("hoodie.datasource.write.recordkey.field", "record_key") \
  .option("hoodie.datasource.write.precombine.field", "precombine_field") \
  .mode("overwrite") \
  .save("path/to/hudi_table")
```

## [Time Travel Queries]

```python
# Querying specific timestamp
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HudiTimeTravel").getOrCreate()
df = spark.read \
  .format("hudi") \
  .option("as.of.instant", "timestamp") \
  .load("path/to/hudi_table")
```

## [Compaction]

```python
# Trigger compaction on a Hudi table
spark.sql("CALL hoodie.compact('your_table_name')")
```

## [Gotchas]

- ⚠️ Ensure the `recordKey` is truly unique; duplicates can lead to data loss.
- ⚠️ Compaction may take time and affect query performance; plan accordingly.

## [Mental model]

- **COPY_ON_WRITE:** Updates create new files; ideal for read-heavy workloads.
- **MERGE_ON_READ:** Updates are merged at read time; suitable for write-heavy scenarios.
- **Time Travel:** Enables querying historical data versions based on timestamps or commits.
```