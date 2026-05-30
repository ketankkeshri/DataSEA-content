```markdown
# Looker LookML — Cheatsheet

## [Section 1: Core syntax]

| Thing               | Syntax                                         | Notes                                      |
|---------------------|------------------------------------------------|--------------------------------------------|
| Dimension           | `dimension: <name> { ... }`                   | Represents a field in your data model.    |
| Measure             | `measure: <name> { ... }`                     | Aggregates data (sum, average, etc.).     |
| View                | `view: <view_name> { ... }`                   | Defines a Looker view from a database table. |
| Explore             | `explore: <view_name> { ... }`                | Allows users to query data from the view. |
| Join                | `join: <view_name> { ... }`                   | Combines data from different views.       |
| Derived Table       | `derived_table: { ... }`                       | Creates a table from SQL queries.         |
| Persistent Table    | `persist_for: <duration>`                      | Caches results of derived tables.         |

## [Section 2: Common operations]

```lookml
view: orders {
  sql_table_name: orders ;;

  dimension: order_id {
    type: number
    sql: ${TABLE}.id ;;
  }

  measure: total_sales {
    type: sum
    sql: ${TABLE}.amount ;;
  }

  derived_table: {
    sql: SELECT customer_id, COUNT(*) as order_count FROM orders GROUP BY customer_id ;;
  }
}

explore: orders {
  join: customers {
    type: left
    sql_on: ${orders.customer_id} = ${customers.id} ;;
  }
}
```

## [Gotchas]

- ⚠️ Derived tables are recalculated each time the query runs — be mindful of performance.
- ⚠️ `sql_table_name` must reference an actual table in your database; otherwise, you'll get errors.

## [Mental model]

- **Views** are like blueprints for data.
- **Measures** aggregate the data.
- **Joins** link different datasets together for richer insights.
```