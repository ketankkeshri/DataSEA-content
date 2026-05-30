# Persistent Tables

Persistent tables in Looker allow you to store the results of your queries for faster access and improved performance. They’re crucial for data analysts and engineers who need to optimize their reporting workflows and ensure that complex queries don’t slow down dashboards.

## Understanding Persistent Tables

Persistent tables are physical tables created in your database from the results of LookML models or derived tables. Unlike derived tables that are temporary and only exist during the session, persistent tables store data permanently until they are manually refreshed or deleted. This is especially useful for large datasets where performance can be a concern.

### Creating a Persistent Table

To create a persistent table, you need to define it in your LookML model using the `persist_for` parameter. This parameter specifies how long the table should stay valid before it gets refreshed. Here’s a basic example:

```lookml
view: persistent_orders {
  derived_table: {
    sql:
      SELECT 
        order_id,
        customer_id,
        order_date,
        total_amount
      FROM 
        orders
      WHERE 
        order_date >= CURRENT_DATE - INTERVAL '30 days'
      ;;
    persist_for: "1 hour"  # Keep this table for 1 hour
  }

  dimension: order_id {
    type: number
    sql: ${TABLE}.order_id ;;
  }

  dimension: customer_id {
    type: number
    sql: ${TABLE}.customer_id ;;
  }

  measure: total_amount {
    type: sum
    sql: ${TABLE}.total_amount ;;
  }
}
```

In this example, the `persistent_orders` view pulls data from the `orders` table and keeps it cached for one hour. This caching allows for quicker access to recent orders without re-running the query every time.

## When to Use Persistent Tables

Persistent tables are ideal in scenarios where:

- **High Query Volume:** When multiple users are querying the same dataset frequently, caching results can drastically reduce load times.
- **Resource-Intensive Calculations:** For complex calculations that don’t change often, storing results in a persistent table can save computational resources.
- **Data Freshness Requirements:** If the underlying data doesn’t change frequently, a persistent table can provide a snapshot without needing to hit the database for every query.

💡 Tip: Use persistent tables for aggregated data or historical snapshots that require less frequent updates.

## Common pitfalls

- **Overusing Persistent Tables:** Creating persistent tables for every view can lead to unnecessary complexity and outdated data. Use them judiciously.
- **Improper Refresh Timing:** Setting an inappropriate `persist_for` duration might lead to stale data or excessive load on your database if refreshed too often.
- **Not Monitoring Performance:** It’s crucial to monitor the performance impact of persistent tables. If they’re not improving query times, consider alternative caching strategies.

## In a nutshell

- Persistent tables store query results in your database for improved performance.
- Use the `persist_for` parameter to define how long the data should be cached.
- Ideal for high query volumes and resource-intensive calculations.
- Avoid overusing them and ensure proper refresh timings.
- Monitor performance to ensure they meet your needs effectively.