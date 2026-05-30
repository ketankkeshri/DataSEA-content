```markdown
# SQL Foundations — Cheatsheet

## [Section 1: Core syntax]

| Thing          | Syntax                                      | Notes                                     |
|----------------|---------------------------------------------|-------------------------------------------|
| Select         | `SELECT column1, column2 FROM table;`     | Retrieves specified columns from a table.|
| Where          | `SELECT * FROM table WHERE condition;`     | Filters results based on condition.      |
| Order By       | `SELECT * FROM table ORDER BY column;`     | Sorts results by specified column.       |
| Limit          | `SELECT * FROM table LIMIT n;`            | Limits results to the first n rows.      |
| Distinct       | `SELECT DISTINCT column FROM table;`      | Removes duplicate values from results.    |
| Null Check     | `SELECT * FROM table WHERE column IS NULL;` | Finds rows where column value is NULL.   |

## [Section 2: Common operations]

```sql
-- Select with a WHERE clause
SELECT name, age 
FROM users 
WHERE age > 18;

-- Join two tables
SELECT a.name, b.department 
FROM employees a 
JOIN departments b ON a.dept_id = b.id;

-- Aggregations
SELECT department, COUNT(*) AS total_employees 
FROM employees 
GROUP BY department;

-- Ordering and limiting results
SELECT name 
FROM users 
ORDER BY created_at DESC 
LIMIT 5;

-- Distinct values
SELECT DISTINCT country 
FROM users;

-- Checking for NULL values
SELECT * 
FROM orders 
WHERE delivery_date IS NULL;
```

## [Gotchas]

- ⚠️ Remember: `SELECT *` retrieves all columns, which can be inefficient with large datasets.
- ⚠️ Joins can produce unexpected results if there are no matching rows; consider using `LEFT JOIN` for safety.

## [Mental model]

- **SELECT** retrieves data.
- **WHERE** filters it down.
- **JOIN** combines data from multiple tables.
```