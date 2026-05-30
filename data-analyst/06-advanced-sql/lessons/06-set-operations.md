# Set Operations

Set operations in SQL allow you to combine the results of two or more SELECT queries. As a data analyst, mastering these operations can help you manage and analyze data from different tables more effectively, enabling you to derive insights from complex datasets.

## Understanding Set Operations

SQL provides several set operations: `UNION`, `INTERSECT`, and `EXCEPT`. These operations are essential for combining datasets that share the same structure, making it easier to perform analyses that require data from multiple sources.

### UNION

The `UNION` operation combines the results of two or more SELECT queries into a single result set, removing duplicate rows by default. Here's how it works:

```sql
SELECT product_id, product_name 
FROM online_store.products 
WHERE category = 'Electronics'

UNION

SELECT product_id, product_name 
FROM retail_store.products 
WHERE category = 'Electronics';
```

This query retrieves a list of unique electronic products from both the `online_store` and `retail_store` tables.

### INTERSECT

The `INTERSECT` operation returns only the rows that are present in both SELECT queries. This is useful when you want to find common entries across datasets.

```sql
SELECT customer_id 
FROM online_store.orders 

INTERSECT 

SELECT customer_id 
FROM retail_store.orders;
```

This query gives you a list of customers who placed orders in both the online and retail stores.

### EXCEPT

The `EXCEPT` operation returns rows from the first SELECT query that are not present in the second SELECT query. It’s handy for identifying entries that exist in one dataset but not the other.

```sql
SELECT product_id, product_name 
FROM online_store.products 

EXCEPT 

SELECT product_id, product_name 
FROM retail_store.products;
```

This query will show you products available online that aren't sold in retail stores.

## Combining Set Operations

You can also combine set operations for more complex queries. For instance, you might want to find products that are either only in the online store or only in the retail store:

```sql
SELECT product_id, product_name 
FROM online_store.products 

EXCEPT 

SELECT product_id, product_name 
FROM retail_store.products

UNION

SELECT product_id, product_name 
FROM retail_store.products 

EXCEPT 

SELECT product_id, product_name 
FROM online_store.products;
```

This query retrieves products that are unique to each store.

## Common pitfalls

- **Mismatched Columns:** All SELECT queries in a set operation must return the same number of columns with compatible data types. Check your queries carefully.
- **Duplicates with UNION ALL:** If you want to include duplicates, use `UNION ALL` instead of `UNION`. This can improve performance when duplicates are expected.
- **Order of Execution:** The order of operations matters in complex queries. Ensure that you understand how SQL evaluates the set operations to avoid unexpected results.

## In a nutshell

- **Set operations** (`UNION`, `INTERSECT`, `EXCEPT`) combine results from multiple queries.
- Use **`UNION`** to merge datasets, **`INTERSECT`** to find common rows, and **`EXCEPT`** to find differences.
- You can combine these operations for **complex queries**.
- Watch for **mismatched columns** and the use of `UNION ALL` for duplicates.
- Understand the **order of execution** in your queries to avoid surprises.