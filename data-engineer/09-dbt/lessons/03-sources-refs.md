# Sources Refs

Understanding how to effectively manage and reference sources in dbt is crucial for building robust data transformations. This lesson dives into the concept of source references and why they matter for data engineers and analysts alike.

## What are Source References?

Source references in dbt allow you to define and access raw data from your source systems. By declaring sources, you establish a clear lineage of your data, ensuring consistency and reliability across your transformations.

### Declaring Sources

To declare a source, you typically create a `sources.yml` file. Here’s how you can set it up:

```yaml
version: 2

sources:
  - name: ecommerce
    database: my_database
    schema: raw
    tables:
      - name: orders
      - name: customers
```

In this example, we define a source called `ecommerce`, which includes two tables: `orders` and `customers`. By organizing your sources this way, you can keep track of your raw data more effectively.

### Referencing Sources in Models

Once you’ve declared your sources, you can reference them in your dbt models using the `source` function. Here's how that looks in practice:

```sql
-- models/orders_summary.sql

SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(order_amount) AS total_revenue
FROM {{ source('ecommerce', 'orders') }}
GROUP BY customer_id
```

This SQL snippet pulls data from the `orders` table in your `ecommerce` source. The `source` function ensures that dbt recognizes this as a reference to the external data, maintaining your data lineage and making your models more readable.

## Benefits of Using Source References

Using source references comes with multiple advantages:

- **Data Lineage**: Easily track where your data originates, which is crucial for debugging and auditing.
- **Consistency**: Ensures that all models referencing a source pull data from the same location, reducing errors.
- **Documentation**: Automatically generates documentation for your sources, helping team members understand data flow.

## Common pitfalls

- **Neglecting Source Declaration**: Forgetting to declare sources can lead to confusion about where data is coming from, complicating debugging efforts.
- **Incorrect Source Names**: Typing errors in source names can result in broken models. Always double-check your references.
- **Source Changes**: If the underlying schema of your source changes (e.g., column names), you need to update your dbt models accordingly to avoid runtime errors.

## In a nutshell

- Source references help maintain data lineage and clarity.
- Declare sources in a dedicated `sources.yml` file.
- Use the `source` function to reference raw data in your models.
- Ensure source declarations are accurate to avoid pitfalls.
- Leverage source documentation for team collaboration and understanding.