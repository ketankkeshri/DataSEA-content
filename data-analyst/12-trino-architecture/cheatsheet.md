```markdown
# Trino Architecture — Cheatsheet

## [Core Components]

| Thing               | Description                                                  | Notes                                  |
|---------------------|--------------------------------------------------------------|----------------------------------------|
| Coordinator         | Manages query planning and task distribution.               | Acts as the brain of the operation.   |
| Worker              | Executes tasks assigned by the coordinator.                 | Scales horizontally; add more workers for more power. |
| Connector           | Interfaces with data sources (e.g., Hive, MySQL).           | Each connector can handle different data formats. |
| Query Execution     | Process of running SQL queries across distributed data.      | Uses a distributed execution model.   |

## [Common Operations]

```sql
-- Example query to select data
SELECT customer_id, COUNT(*) AS order_count 
FROM orders 
WHERE order_date >= DATE '2023-01-01' 
GROUP BY customer_id 
ORDER BY order_count DESC;
```

## [Gotchas]

- ⚠️ **Data Source Compatibility:** Not all connectors support the same SQL features. Check documentation for limitations.
- ⚠️ **Resource Management:** Ensure workers have adequate resources; otherwise, queries may fail or timeout.
- ⚠️ **Network Latency:** Distributed queries can introduce latency; monitor performance when scaling.

## [Mental model]

- **Coordinator**: Distributes tasks ↓
- **Workers**: Execute tasks on data sources ↔️
- **Connectors**: Bridge between Trino and data sources 🔗
```