```markdown
# PostgreSQL Internals — Cheatsheet

## [Section 1: MVCC (Multi-Version Concurrency Control)]

| Thing                   | Syntax                          | Notes                                                       |
|-------------------------|---------------------------------|-------------------------------------------------------------|
| Transaction Isolation    | `SET TRANSACTION ISOLATION LEVEL <level>;` | Levels: READ COMMITTED, SERIALIZABLE, REPEATABLE READ.     |
| Current Transaction ID   | `SELECT txid_current();`       | Retrieves the current transaction ID.                       |
| Snapshot Visibility      | `SELECT * FROM pg_stat_activity;` | Shows visibility of transactions.                           |

## [Section 2: Vacuum and Bloat]

```sql
-- Check for table bloat
SELECT pg_size_pretty(pg_total_relation_size('your_table'));

-- Run VACUUM
VACUUM your_table;
```

## [Indexes Deep Dive]

| Index Type     | Syntax                                       | Notes                                           |
|----------------|----------------------------------------------|-------------------------------------------------|
| B-tree         | `CREATE INDEX index_name ON table_name (column_name);` | Default index type, great for equality and range queries. |
| Hash           | `CREATE INDEX index_name ON table_name USING HASH (column_name);` | Best for equality comparisons, less common.    |
| GIN            | `CREATE INDEX index_name ON table_name USING GIN (column_name);` | Useful for array and JSONB data types.         |
| GiST           | `CREATE INDEX index_name ON table_name USING GiST (column_name);` | Good for geometric data types.                  |

## [Replication Basics]

```sql
-- Check replication status
SELECT * FROM pg_stat_replication;

-- Set up replication
wal_level = replica
max_wal_senders = <number>
```

## [Gotchas]

- ⚠️ MVCC can lead to bloat if VACUUM isn't run regularly.
- ⚠️ Indexes can slow down writes; balance read vs. write performance.
- ⚠️ Ensure that replication settings are correctly configured to avoid lag.

## [Mental model]

- **MVCC**: Transactions see their own changes, helping avoid locks.
- **Vacuum**: Cleans up dead tuples; essential for performance.
- **Indexes**: Speed up reads but add overhead to writes; choose wisely.
```