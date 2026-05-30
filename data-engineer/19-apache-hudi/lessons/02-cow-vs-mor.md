# Cow Vs Mor

Understanding the differences between Copy-On-Write (CoW) and Merge-On-Read (MoR) in Apache Hudi is essential for data engineers who want to optimize data ingestion and querying performance. Let's dive into how these two storage mechanisms work and why they matter for your data pipelines.

## Copy-On-Write (CoW) Explained

Copy-On-Write (CoW) is a storage strategy that focuses on maintaining data integrity by creating a new version of a data file whenever changes are made. This means that instead of updating an existing file directly, CoW writes changes to a new file and maintains the previous version intact. 

### How CoW Works

1. **Write Operation**: When you perform a write operation, CoW creates a new file with the updated data.
2. **File Swap**: Once the new file is ready, it swaps out the old file and makes the new file the current version.
3. **Data Integrity**: This approach ensures that readers always access a consistent view of the data, even during write operations.

Here's a simple example:

```python
from pyspark.sql import SparkSession
from hudi import HudiDataFrame

spark = SparkSession.builder \
    .appName("Hudi CoW Example") \
    .getOrCreate()

# Sample DataFrame
data = [
    (1, "Alice", 34),
    (2, "Bob", 45),
]

df = spark.createDataFrame(data, ["id", "name", "age"])

# Write to Hudi in CoW mode
df.write.format("hudi") \
    .option("hoodie.table.name", "people") \
    .option("hoodie.datasource.write.recordkey.field", "id") \
    .option("hoodie.datasource.write.precombine.field", "age") \
    .option("hoodie.datasource.write.operation", "insert") \
    .mode("overwrite") \
    .save("/path/to/hudi/table")
```

In this code, we create a DataFrame and write it to a Hudi table in CoW mode. Each write operation results in a new version of the data file.

## Merge-On-Read (MoR) Explained

Merge-On-Read (MoR), on the other hand, is designed for scenarios where read performance is prioritized over write performance. With MoR, data is written in a more compact format, and the merging of data happens at read time.

### How MoR Works

1. **Write Operation**: Data is written directly to a base file without creating new versions.
2. **Query Time Merge**: When a query is executed, Hudi merges the base files with any delta files that contain updates.
3. **Read Performance**: This allows for faster writes but may result in slower reads since merging occurs at query time.

Here's how you can write data in MoR mode:

```python
# Write to Hudi in MoR mode
df.write.format("hudi") \
    .option("hoodie.table.name", "people_mor") \
    .option("hoodie.datasource.write.recordkey.field", "id") \
    .option("hoodie.datasource.write.precombine.field", "age") \
    .option("hoodie.datasource.write.operation", "insert") \
    .option("hoodie.table.type", "MERGE_ON_READ") \
    .mode("overwrite") \
    .save("/path/to/hudi/mor_table")
```

In this case, we specify `MERGE_ON_READ` to indicate that we're using MoR. This choice allows us to optimize for scenarios where we anticipate a high volume of writes.

## Common pitfalls

- **Understanding Use Cases**: Choosing CoW over MoR (or vice versa) without understanding your workload can lead to performance issues.
- **Data Consistency**: In MoR, the merging process can lead to stale reads if not properly managed, especially in high-concurrency environments.
- **Storage Overhead**: CoW can lead to increased storage usage due to the creation of multiple versions of data files.

## In a nutshell

- **CoW**: Creates new data files for each write, ensuring data consistency at the cost of write performance.
- **MoR**: Writes data directly to base files, merging at read time, optimizing for write-heavy workloads.
- **Choose Wisely**: Your choice between CoW and MoR should align with your specific data ingestion and querying requirements.