# Derived Tables

Derived tables in Looker allow you to create temporary tables on the fly, letting you manipulate data more flexibly and efficiently. As a data analyst, understanding derived tables is crucial for optimizing your data models and delivering insights faster.

## What are Derived Tables?

Derived tables are essentially tables that you define in LookML that are built on the fly from other tables. Unlike traditional tables, derived tables are not stored in the database but are created dynamically when queried. This means you can perform complex calculations, aggregations, and joins without cluttering your database with extra tables.

### Creating a Derived Table

To create a derived table, you use the `derived_table` parameter within a view. Here's a basic example where we create a derived table for sales data filtered by the last month:

```lookml
view: monthly_sales {
  derived_table: {
    sql: 
      SELECT 
        product_id,
        SUM(amount) AS total_sales,
        COUNT(*) AS total_orders
      FROM 
        orders
      WHERE 
        order_date >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
      GROUP BY 
        product_id
      ;;
  }

  dimension: product_id {
    type: string
    sql: ${TABLE}.product_id ;;
  }

  measure: total_sales {
    type: sum
    sql: ${TABLE}.total_sales ;;
  }

  measure: total_orders {
    type: count
    sql: ${TABLE}.total_orders ;;
  }
}
```

In this example, the `monthly_sales` view generates a table that shows the total sales and order count for each product in the last month. The SQL inside the `derived_table` block is executed whenever this view is queried.

## When to Use Derived Tables

Derived tables are fantastic for scenarios where:

- You need to perform calculations that are too complex for a simple view.
- You want to create aggregated data on-the-fly to reduce the load on your database.
- You are working with large datasets and need to filter or transform data dynamically.

However, keep in mind that derived tables can impact performance if overused or if they query large volumes of data. Always consider the trade-offs between complexity and efficiency.

## Common pitfalls

- **Overusing derived tables**: They can lead to slower query performance, especially with large datasets. Use them judiciously.
- **Not indexing underlying tables**: If the source tables aren't optimized, the derived table queries can be slow.
- **Complex SQL in derived tables**: Keeping SQL straightforward helps maintain readability and manageability. Break complex queries into smaller derived tables if needed.

## In a nutshell

- Derived tables allow dynamic data manipulation without creating permanent tables.
- Use them for complex calculations and aggregations on-the-fly.
- Be cautious of performance impacts and keep SQL simple for maintainability.
- Always optimize the underlying tables to improve derived table performance.