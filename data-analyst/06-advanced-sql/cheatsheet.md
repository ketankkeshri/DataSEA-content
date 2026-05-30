```markdown
# Advanced SQL — Cheatsheet

## [Section 1: Window Functions]

| Thing                     | Syntax                                       | Notes                                           |
|---------------------------|----------------------------------------------|-------------------------------------------------|
| Define a window           | `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` | Defines the range of rows in the window.        |
| Aggregate over a window   | `SELECT AVG(salary) OVER (PARTITION BY dept_id ORDER BY hire_date) AS avg_salary` | Calculate averages per department.              |
| Row numbering              | `ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank` | Assigns unique ranks within partitions.         |

## [Section 2: Common Table Expressions (CTEs)]

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT *
FROM cte_name;
```

## [Subqueries]

```sql
SELECT *
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM departments
    WHERE name = 'Sales'
);
```

## [Recursive CTEs]

```sql
WITH RECURSIVE cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE base_condition
    UNION ALL
    SELECT e.column1, e.column2
    FROM table_name e
    INNER JOIN cte_name c ON e.id = c.parent_id
)
SELECT *
FROM cte_name;
```

## [Pivot and Unpivot]

### Pivot

```sql
SELECT *
FROM (
    SELECT dept_id, month, sales
    FROM sales_data
) AS source_table
PIVOT (
    SUM(sales) FOR month IN ([January], [February], [March])
) AS pivot_table;
```

### Unpivot

```sql
SELECT dept_id, month, sales
FROM (
    SELECT dept_id, January, February, March
    FROM pivot_table
) AS p
UNPIVOT (
    sales FOR month IN (January, February, March)
) AS u;
```

## [Set Operations]

### UNION

```sql
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;
```

### INTERSECT

```sql
SELECT column1 FROM table1
INTERSECT
SELECT column1 FROM table2;
```

### EXCEPT

```sql
SELECT column1 FROM table1
EXCEPT
SELECT column1 FROM table2;
```

## [Gotchas]

- ⚠️ Remember that `UNION` removes duplicates; use `UNION ALL` if you want to keep them.
- ⚠️ Recursive CTEs can lead to infinite loops if not defined with a proper base condition.

## [Mental model]

1. **Window Functions**: Operate across a set of rows related to the current row.
2. **CTEs**: Temporary result set that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement.
3. **Set Operations**: Combine results from two or more queries, focusing on how data overlaps or diverges.
```