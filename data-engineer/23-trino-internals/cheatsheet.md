```markdown
# Trino Internals — Cheatsheet

## [Section 1: Query Planning]

| Thing                          | Syntax               | Notes                                 |
|--------------------------------|----------------------|---------------------------------------|
| Query Parsing                  | `parse(query)`       | Transforms SQL into an abstract tree. |
| Optimizer Invocation           | `optimize(tree)`     | Applies optimization rules to the tree. |
| Execution Plan Generation      | `plan(tree)`         | Creates an execution plan based on the optimized tree. |
| Query Execution                | `execute(plan)`      | Runs the execution plan on the cluster. |

## [Section 2: Cost-Based Optimizer]

```sql
-- Example of using CBO hints in a query
SELECT /*+ CBO */ *
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE orders.total > 100
```

## [Section 3: Fault-Tolerant Execution]

```language
-- Setting up fault tolerance in query execution
SET SESSION fault_tolerance.enabled = true;

SELECT *
FROM large_table
WHERE condition = 'value';
```

## [Section 4: Federation Patterns]

| Pattern                  | Description                                  | Example                                   |
|-------------------------|----------------------------------------------|-------------------------------------------|
| Data Source Federation   | Queries across multiple data sources         | `SELECT * FROM remote_db.table`          |
| Query Routing            | Directs queries to specific data sources     | `SELECT * FROM local_db.table UNION ALL SELECT * FROM remote_db.table` |
| Load Balancing           | Distributing queries across multiple nodes   | Implemented via the `connector` config.  |

## [Gotchas]

- ⚠️ Ensure data types match when federating sources to avoid runtime errors.
- ⚠️ Optimize join orders in large datasets to prevent performance hits.

## [Mental model]

1. **Query Parsing** converts SQL to an abstract syntax tree.
2. **Cost-Based Optimizer** evaluates multiple execution plans.
3. **Execution Planning** generates a plan that considers fault tolerance and federation.
```