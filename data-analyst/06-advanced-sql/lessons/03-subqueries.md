# Subqueries

Subqueries are powerful tools in SQL that allow you to nest queries within other queries. They can simplify complex queries, make them more readable, and optimize performance. Understanding how to use subqueries effectively is essential for any data analyst looking to get deeper insights from their data. 

## What is a Subquery?

A subquery, or nested query, is a query within another SQL query. It is typically used in the `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statements. Subqueries can return single values, a list of values, or even a complete result set. You can use them to filter results, perform calculations, or derive new insights based on existing data.

### Types of Subqueries

1. **Single-row subquery**: Returns one row and one column.
2. **Multiple-row subquery**: Returns multiple rows.
3. **Correlated subquery**: References columns from the outer query.

Here’s a quick example using a fictional `employees` table:

```sql
SELECT name
FROM employees
WHERE department_id = (
    SELECT id
    FROM departments
    WHERE name = 'Engineering'
);
```

In this example, the inner query fetches the department ID for "Engineering," and the outer query retrieves the names of employees in that department.

## Using Subqueries in `FROM` Clause

Subqueries can also be used in the `FROM` clause to create temporary tables. This approach can make your main query cleaner and more efficient.

### Example with `FROM` Clause

```sql
SELECT avg(salary) AS average_salary
FROM (
    SELECT salary
    FROM employees
    WHERE department_id = 2
) AS engineering_salaries;
```

In this case, the inner query retrieves salaries from the `employees` table for department ID 2 (let's say it's Engineering), and the outer query calculates the average salary from this temporary result.

## Common pitfalls

- **Performance Issues**: Correlated subqueries can be slow because the inner query runs for each row in the outer query. Consider using joins when possible.
- **Too Many Results**: Ensure your subquery returns a single value (when using `=`) or multiple values (`IN` or `ANY`) as needed. Using `=` with a multiple-row subquery will throw an error.
- **Syntax Errors**: Pay attention to parentheses and aliasing. Forgetting to alias a subquery can lead to confusion in larger queries.

## In a nutshell

- Subqueries allow for nesting queries to enhance SQL capabilities.
- They can be used in various clauses like `WHERE`, `FROM`, and `SELECT`.
- Avoid performance pitfalls by being mindful of correlated queries.
- Ensure your subqueries return the correct number of results to avoid errors.
- Use subqueries to simplify complex SQL statements and improve readability.