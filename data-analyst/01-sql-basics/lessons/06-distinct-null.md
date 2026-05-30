# Distinct Null

Understanding how to handle NULL values in SQL is crucial for data analysts and engineers. This lesson dives into the `DISTINCT` keyword and its behavior with NULLs, ensuring you can cleanly extract unique records while accounting for missing data.

## The Basics of DISTINCT

The `DISTINCT` keyword is used in SQL to eliminate duplicate records from your query results. When you apply `DISTINCT`, SQL checks the values in the specified columns and only returns unique combinations. But what happens when NULLs are involved?

Consider a table named `users` that contains user information:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO users (id, name, email) VALUES
(1, 'Alice', 'alice@example.com'),
(2, 'Bob', NULL),
(3, 'Charlie', 'charlie@example.com'),
(4, 'David', NULL);
```

If you want to retrieve unique email addresses from this `users` table, you would write:

```sql
SELECT DISTINCT email
FROM users;
```

The result would be:

| email                |
|----------------------|
| alice@example.com    |
| charlie@example.com  |
| NULL                 |

Notice that `NULL` is considered a unique value in SQL. So, if you have multiple rows with NULL values, `DISTINCT` will treat them as one unique entry.

## Practical Implications

Handling NULLs properly is essential for accurate data analysis. If you don't account for NULLs, you might misinterpret your data. For example, if you're calculating the number of unique email addresses, you might think you have only two unique addresses, but including NULL as a unique entry gives you three distinct records.

To illustrate this:

```sql
SELECT COUNT(DISTINCT email) AS unique_emails
FROM users;
```

This query will return `3` instead of `2`, which could impact subsequent analyses or reports.

> 💡 Tip: Always be aware of NULLs when using `DISTINCT`, especially in aggregation functions.

## Common pitfalls

- **Ignoring NULLs**: Assuming NULLs are just ignored can lead to incorrect data interpretations.
- **Count confusion**: Misunderstanding how `COUNT(DISTINCT ...)` works with NULLs can skew your unique counts.
- **Inconsistent results**: Different SQL engines might handle NULLs differently, leading to unexpected results if you're not aware of the specifics.

## In a nutshell

- `DISTINCT` removes duplicate records, treating NULLs as unique.
- Use `DISTINCT` carefully with NULLs to avoid miscounting unique values.
- Understanding the behavior of NULLs is crucial for accurate data analysis.
- Always check your results when dealing with NULLs to ensure they align with expectations.