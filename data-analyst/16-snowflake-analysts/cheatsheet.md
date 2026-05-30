```markdown
# Snowflake for Analysts — Cheatsheet

## [Section 1: Data Warehouses and Credits]

| Thing                     | Syntax                                           | Notes                                                    |
|--------------------------|-------------------------------------------------|----------------------------------------------------------|
| Create Warehouse          | `CREATE WAREHOUSE my_warehouse WITH ( ... );`  | Define size, auto-suspend, etc.                          |
| Drop Warehouse            | `DROP WAREHOUSE my_warehouse;`                  | Deletes the specified warehouse.                         |
| Resize Warehouse          | `ALTER WAREHOUSE my_warehouse RESIZE TO XL;`   | Change the size of the warehouse.                        |
| Show Warehouses           | `SHOW WAREHOUSES;`                              | List all warehouses in the account.                     |
| Credits Per Hour         | `SELECT CURRENT_WAREHOUSE_CREDITS();`          | Get the credits consumed by the warehouse.              |

## [Section 2: Semi-Structured Data]

```sql
-- Load JSON data into a table
CREATE OR REPLACE TABLE my_table AS
SELECT
    PARSE_JSON(column_name) AS json_data
FROM @my_stage;

-- Query semi-structured data
SELECT
    json_data:field_name::string AS field_name
FROM my_table
WHERE json_data:field_name IS NOT NULL;
```

## [Section 3: Time Travel]

| Thing                     | Syntax                                           | Notes                                                    |
|--------------------------|-------------------------------------------------|----------------------------------------------------------|
| Enable Time Travel        | `ALTER TABLE my_table SET DATA_RETENTION_TIME_IN_DAYS = 7;` | Set retention period for time travel.                   |
| Query Historical Data    | `SELECT * FROM my_table AT (TIMESTAMP => '2023-01-01 10:00:00');` | Access data as it was at a specific time.              |
| Show Historical Versions  | `SELECT * FROM my_table VERSION AS OF (TIMESTAMP => '2023-01-01 10:00:00');` | List versions available at a timestamp.                |

## [Gotchas]

- ⚠️ Time travel is limited by the data retention period set on the table.
- ⚠️ Credits are consumed when warehouses are active, even if no queries are running.

## [Mental model]

- **Warehouses:** Resources that process queries.
- **Data Storage:** Tables can store structured and semi-structured data.
- **Time Travel:** Access past states of data for recovery or analysis.
```