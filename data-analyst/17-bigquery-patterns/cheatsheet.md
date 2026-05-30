```markdown
# BigQuery Analytical Patterns — Cheatsheet

## [Section 1: Partitioning & Clustering]

| Thing                     | Syntax                                           | Notes                                                        |
|---------------------------|--------------------------------------------------|--------------------------------------------------------------|
| **Partitioning**          | `PARTITION BY column_name`                       | Divides table into segments based on the value of `column_name`. Use for large datasets. |
| **Clustering**            | `CLUSTER BY column_name`                         | Organizes data within partitions to improve query performance. Great for frequently filtered columns. |
| **Date Partitioning**     | `PARTITION BY DATE(column_name)`                 | Automatically partitions data by date, improving performance for time-based queries. |
| **Clustering Columns**    | `CLUSTER BY column1, column2`                   | Define multiple clustering columns to optimize data retrieval. |
| **Creating Partitioned Table** | `CREATE TABLE dataset.table_name (columns) PARTITION BY column_name` | Create a new partitioned table in one go. |

## [Section 2: Slot Management]

```sql
-- Set the maximum slots for a project
SET `project_id`.max_slots = 2000;

-- Check current slot usage
SELECT
  reservation_id,
  slots_used,
  slots_total
FROM
  `region-us`.INFORMATION_SCHEMA.RESERVATIONS;
```

## [Section 3: Cost Control]

| Thing                     | Syntax                                           | Notes                                                        |
|---------------------------|--------------------------------------------------|--------------------------------------------------------------|
| **Estimate Query Cost**   | `SELECT * FROM `project_id.dataset.table` WHERE condition` | Use the dry run feature to estimate costs before executing. |
| **Cost Control Strategies** | `WITH` clause for common subqueries | Reduces repeated calculations, thus lowering costs.          |
| **Use Approximate Functions** | `APPROX_COUNT_DISTINCT(column_name)`      | Use for large datasets to minimize costs while still getting near-accurate results. |

## [Gotchas]

- ⚠️ Partitioned tables can have performance hits if not queried correctly. Always filter on partitioned columns.
- ⚠️ Clustering doesn't improve performance for all queries. Test your queries to see if it helps.
- ⚠️ Slot limits can impact performance; monitor usage to avoid slowdowns.

## [Mental model]

- **Partitioning**: Think of it as dividing a pizza into slices; each slice is a partition.
- **Clustering**: Like arranging books by genre within each shelf (partition).
- **Cost Control**: Keep an eye on your spending like checking a budget. Use tools to estimate before committing.
```