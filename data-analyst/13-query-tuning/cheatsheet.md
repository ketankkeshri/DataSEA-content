```markdown
# Query Tuning & Optimization — Cheatsheet

## [Explain Plans]

| Thing              | Syntax                                | Notes                                                  |
|--------------------|---------------------------------------|--------------------------------------------------------|
| View Explain Plan   | `EXPLAIN SELECT * FROM table;`       | Shows the execution plan for the query.                |
| Analyze Execution   | `EXPLAIN ANALYZE SELECT * FROM table;` | Executes the query and provides runtime statistics.    |
| Format Options      | `EXPLAIN (FORMAT JSON) SELECT ...;` | Output in JSON format for easier parsing.              |

## [Indexes - Advanced]

| Thing              | Syntax                                | Notes                                                  |
|--------------------|---------------------------------------|--------------------------------------------------------|
| Create Index       | `CREATE INDEX idx_name ON table (column);` | Improves query performance on specified columns.      |
| Unique Index       | `CREATE UNIQUE INDEX idx_name ON table (column);` | Ensures all values are unique in the column.          |
| Drop Index         | `DROP INDEX idx_name;`               | Removes an existing index.                             |

## [Partitioning]

| Thing              | Syntax                                | Notes                                                  |
|--------------------|---------------------------------------|--------------------------------------------------------|
| Create Partitioned Table | `CREATE TABLE table_name (id INT) PARTITION BY RANGE (id);` | Distributes data across partitions based on column values. |
| Add Partition      | `ALTER TABLE table_name ADD PARTITION FOR VALUES FROM (1) TO (100);` | Adds a new partition to the existing table.           |
| Drop Partition     | `ALTER TABLE table_name DROP PARTITION partition_name;` | Removes a specific partition.                          |

## [Caching Strategies]

| Thing              | Syntax                                | Notes                                                  |
|--------------------|---------------------------------------|--------------------------------------------------------|
| Enable Caching     | `SET enable_cache = true;`           | Activates the caching mechanism for queries.          |
| Cache Query        | `SELECT * FROM table WITH (NOLOCK);` | Caches the result set for faster access.              |
| Clear Cache        | `CACHE CLEAR;`                       | Clears the cached data for the session.               |

## [Gotchas]

- ⚠️ **Index Overhead:** Too many indexes can slow down write operations (INSERT/UPDATE).
- ⚠️ **Partitioning Limits:** Be aware of the maximum number of partitions supported by your DBMS.
- ⚠️ **Caching Staleness:** Cached results may not reflect the most current data; always consider fresh data needs.

## [Mental model]

- **Execution Plans**: Understand how queries are executed in the DB.
- **Indexing**: Think of indexes as shortcuts to speed up data retrieval.
- **Partitioning**: Visualize partitions as separate buckets for organizing large datasets, improving access time.
```