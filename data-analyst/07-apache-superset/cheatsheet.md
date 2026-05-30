```markdown
# Apache Superset — Cheatsheet

## [Section 1: Core Components]

| Thing           | Syntax                          | Notes                                      |
|-----------------|---------------------------------|--------------------------------------------|
| Create Dataset  | `superset import_datasource`   | Imports a dataset from a CSV or SQL query. |
| Create Dashboard | `superset create_dashboard`    | Generates a new dashboard.                 |
| SQL Lab Query   | `SELECT * FROM table_name;`    | Runs SQL queries on your datasets.         |
| Custom Visualization | `superset add_custom_viz` | Adds a custom visualization to a dashboard. |

## [Common Operations]

```sql
-- Basic SQL query
SELECT column1, COUNT(*)
FROM your_table
GROUP BY column1
ORDER BY COUNT(*) DESC;

-- Create a time series chart
SELECT time_column, SUM(value_column)
FROM your_table
GROUP BY time_column
ORDER BY time_column;

-- Filter data in SQL Lab
SELECT *
FROM your_table
WHERE condition_column = 'value';
```

## [Gotchas]

- ⚠️ Ensure that your database connection is set up correctly; otherwise, queries will fail.
- ⚠️ Remember to refresh your dataset after making changes to the underlying data source.
- ⚠️ Custom visualizations may require additional JavaScript libraries; check compatibility.

## [Mental model]

- **Datasets** hold your data.
- **SQL Lab** is for querying and exploring data.
- **Dashboards** visualize data using charts and graphs.
```