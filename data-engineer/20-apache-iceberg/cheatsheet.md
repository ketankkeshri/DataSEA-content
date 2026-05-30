```markdown
# Apache Iceberg — Cheatsheet

## [Section 1: Core Concepts]

| Thing                     | Syntax                         | Notes                                      |
|---------------------------|--------------------------------|--------------------------------------------|
| Create Table              | `CREATE TABLE table_name (...)`| Define schema with optional partitioning.  |
| Insert Data               | `INSERT INTO table_name VALUES (...)` | Append data to the table.                 |
| Query Table               | `SELECT * FROM table_name`    | Standard SQL query on Iceberg tables.     |
| Drop Table                | `DROP TABLE table_name`       | Removes the table and its metadata.       |
| Alter Table               | `ALTER TABLE table_name ...`  | Modify table schema or properties.        |

## [Section 2: Common Operations]

```sql
-- Create a new Iceberg table
CREATE TABLE my_table (
    id BIGINT,
    data STRING
) USING iceberg
PARTITIONED BY (data);

-- Inserting data
INSERT INTO my_table VALUES (1, 'example data');

-- Querying the table
SELECT * FROM my_table WHERE data = 'example data';

-- Dropping the table
DROP TABLE my_table;
```

## [Gotchas]

- ⚠️ Iceberg manages data files; be cautious with manual file manipulations outside of Iceberg.
- ⚠️ Ensure partitioning strategy aligns with query patterns to avoid performance bottlenecks.

## [Mental model]

- **Table Format**: Iceberg stores data in a columnar format like Parquet.
- **Hidden Partitioning**: Automatically manages partitions, simplifying queries.
- **Branching & Tagging**: Supports versioning and rollback of table states.
```